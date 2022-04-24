import chunk
from pprint import pprint
from urllib import response
import requests
from bs4 import BeautifulSoup
from os import sys
from parser_core.get_person_info import parse_user_info, get_user_info
import json
from progress.bar import IncrementalBar
from parserweb.config import BASE_URL
from db.model import db, Rsodata
import asyncio
import aiohttp

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.174 YaBrowser/22.1.3.856 (beta) Yowser/2.5 Safari/537.36"
}

def get_data_from_file(filename):
    # TODO: catch errors
    with open(filename, encoding='utf-8') as file:
        return file.read()
    
def get_data_from_url(url):
    try:
        response = requests.get(url, headers=headers)
    except Exception as e:
        print("Something went wrong, while ")
        print(e)
    if not response.status_code == 200:
        raise Exception("Status code should be 200")
    return response.text # check what should be returned

def get_data(source_type):
    source_types = ['url', 'file']
    if source_type not in source_types:
        sys.exit(1)    
    if source_type == 'url':
        url = f'{BASE_URL}/about/reestr/?member_lname=&organization='
        return get_data_from_url(url)
    if source_type == 'file':
        return get_data_from_file('registry.html')


async def get_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def get_data_from_url_list(url_list, chunk=50, pause=1):
    list_len = len(url_list)
    bar = IncrementalBar('Getting user info', max = list_len)
    start_range = 0
    end_range = chunk
    fetched_data_dict = {}
    while start_range != list_len:
        for idx in range(start_range, end_range):
            data = await get_url(url_list[idx])
            fetched_data_dict[url_list[idx]] = data
        bar.next(n=end_range-start_range)
        await asyncio.sleep(pause)
        start_range = end_range
        end_range = (end_range + chunk) if (end_range + chunk <= list_len) else list_len
    bar.finish()
    return fetched_data_dict

def parse_main_page():
    content = get_data('url')
    soup = BeautifulSoup(content, "html.parser")
    all_rows = soup.find_all('td', class_="left-td")
    # print(all_rows)
    # all_rows = table.find_all('tr')
    person_list = []
    all_rows_len = len(all_rows)
    
    url_list = []
    for row in all_rows:
        href_obj = row.find('a')
        url = BASE_URL+href_obj['href']
        url_list.append(url)
    
    all_data = asyncio.run(get_data_from_url_list(url_list))
    
    for url, user_data in all_data.items():
        # print(f"Getting data for persons {index+1}, remaining {all_rows_len-index-1} persons to get")
        user_parsed_data = parse_user_info(user_data, url)
        error_list = []
        if not user_parsed_data['lfm']:
            error_list.append(url)
            continue
        person_list.append(user_parsed_data)
    
    for error in error_list:
        print(f"Can't get user info from url {error}")
    return person_list

def return_parsed_data():
    with open('users.json', 'r', encoding='utf-8') as file:
        return json.load(file)
    
def save_data(row):
    rso = Rsodata(reestr_number=row.get('reestr_number'),
        satisfied = row.get('satisfied'), excluded = row.get('excluded'),
        stopped = row.get('stopped'), grade = row.get('grade'),
        ensurance = row.get('ensurance'),
        # user = User(#firstname = row.get('firstname'),
        # #lastname = row.get('lastname'),
        # #middlename = row.get('middlename'),
        lfm = row.get('lfm'),
        compensation = row.get('compensation'),
        experience = row.get('experience'),
        contacts = row.get('contacts'),
        # ensurance_id = row.get('ensurance_id'),
        # rso_id = row.get('rso_id'),
        url = row.get('url')
        )
    db.session.add(rso)
    db.session.commit()

if __name__ == '__main__':
    result = parse_main_page()
    with open('users.json', 'w', encoding='utf-8') as file:
       json.dump(result, indent=4, fp=file, ensure_ascii=False)
