from pprint import pprint
import requests
from bs4 import BeautifulSoup
from os import sys
from parsers.get_person_info import get_user_info, parse_user_info
import json
from progress.bar import IncrementalBar
from config import BASE_URL
from db.model import db, Rsodata

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
        raise Error
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

def parse_main_page():
    content = get_data('url')
    soup = BeautifulSoup(content, "html.parser")
    all_rows = soup.find_all('td', class_="left-td")
    # all_rows = table.find_all('tr')
    person_list = []
    all_rows_len = len(all_rows)
    bar = IncrementalBar('Getting user info', max = all_rows_len)

    for index, row in enumerate(all_rows):
        href_obj = row.find('a')
        url = BASE_URL+href_obj['href']
        bar.next()
        # print(f"Getting data for persons {index+1}, remaining {all_rows_len-index-1} persons to get")
        user_data = get_user_info(url, headers=headers)
        user_parsed_data = parse_user_info(user_data, url)
        if not user_parsed_data['lfm']:
            print(f"There is no user data {href_obj.text}, skipping")
            continue
        person_list.append(user_parsed_data)
    bar.finish()
    
    return person_list

def return_parsed_data():
    with open('users.json', 'r', encoding='utf-8') as file:
        return json.load(file)
    
def save_data(row):
    rso = Rsodata(reestr_number=row.get('reestr_number'),
    satisfied = row.get('satisfied'), excluded = row.get('excluded'),
    stopped = row.get('stopped'), grade = row.get('grade'))
    # ensurance = Ensurance(ensurance_org=row.get('ensurance_org'))
    # user = User(#firstname = row.get('firstname'),
    # #lastname = row.get('lastname'),
    # #middlename = row.get('middlename'),
    # lfm = row.get('lfm'),
    # compensation = row.get('compensation'),
    # experience = row.get('experience'),
    # contacts = row.get('contacts'),
    # ensurance_id = row.get('ensurance_id'),
    # rso_id = row.get('rso_id'),
    # url = row.get('url'))
    print(db.session.add(rso))
    print(db.session.commit())

if __name__ == '__main__':
    result = parse_main_page()
    #with open('users.json', 'w', encoding='utf-8') as file:
    #    json.dump(result, indent=4, fp=file, ensure_ascii=False)
    for row in return_parsed_data():
             save_data(row)
