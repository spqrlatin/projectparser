from bs4 import BeautifulSoup
import requests
import re
from pprint import pprint

headers = {}
def get_user_info(url, headers):
    response = requests.get(url, headers=headers)
    return response.text

def get_currnet_person(soup):
    # Реализовать парсинг для действующих членов
    return {}

def get_uncurrnet_person(soup):  
    try:
        posrel_all = soup.find_all("td", class_="posrel")
        exclusion_data =  posrel_all[0].get_text(strip=True, separator='\n').split('\n')
        exclusion_date = exclusion_data[1]
        exlusion_reason = exclusion_data[3]
    except:
        exclusion_date = None
        exlusion_reason = None
    try: 
        reestr_number = re.search('[0-9]+', posrel_all[4].get_text(strip=True, separator='\n').split('\n')[0]).group(0)    
    except:
        reestr_number = None
    contacts = cleanup_changed(posrel_all, 6)
    organization = cleanup_changed(posrel_all, 7)
    experience = cleanup_changed(posrel_all, 8)
    try:
        ensurance_orgs_list = []
        ensurance_orgs = posrel_all[9].get_text(strip=True, separator='\n').split('Страховая организация')
        for ensurance_org in ensurance_orgs:
            if ensurance_org:
                ensurance_orgs_list.append(' '.join(ensurance_org.split('\n')[:-1]).strip())
    except:
        ensurance_org = None
    compensation = cleanup_changed(posrel_all, 14)
    uncurrent_person_dict = {'exlusion_reason': exlusion_reason,
        'exclusion_date': exclusion_date,
        'reestr_number': reestr_number,
        'contacts': contacts,
        'organization': organization,
        'experience': experience,
        'ensurance_org': ensurance_orgs_list,
        'compensation': compensation
    }
    return uncurrent_person_dict
    
def cleanup_changed(content, idx):
    if idx > len(content):
        return None
    try:
        return ' '.join(content[idx].get_text(strip=True, separator='\n').split('\n')[:-1])
    except:
        return None

def parse_user_info(content, url):
    soup = BeautifulSoup(content, "html.parser")
    try:
        lfm = soup.find("h3").text
    except:
        lfm = None
    try:
        date_and_city_of_birth = soup.find("div", class_="reestr").find('p').text.strip()
        city_of_birth = date_and_city_of_birth.split(',')[1].strip()
        date_of_birth = date_and_city_of_birth.split(',')[0].split('-')[1].strip()
    except:
       city_of_birth = None
       date_of_birth = None 
    try:
        status = soup.find("table", class_="top").find('td').text.strip()
    except:
        status = "Действующий"
    if status != 'Действующий':
        expanded_dict = get_uncurrnet_person(soup)
    else:
        expanded_dict = get_currnet_person(soup)
    return {
        'lfm': lfm,
        'birth_date': date_of_birth,
        'birth_city': city_of_birth,
        'status': status,
        'url': url,
        **expanded_dict
    }


if __name__ == '__main__':
    from parser import headers
    # url = 'http://sroroo.ru/about/reestr/379972/'
    url = 'http://sroroo.ru/about/reestr/806693/'
    # with open("index.html", "w") as file:
    #     data = get_user_info(url, headers)
    #     file.write(data)
    with open('index.html', encoding='utf-8') as file:
        data = file.read()
    parsed_data = parse_user_info(data, url)
    pprint(parsed_data)
    