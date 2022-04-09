from bs4 import BeautifulSoup
import requests
import re
from pprint import pprint

headers = {}
def get_user_info(url, headers):
    response = requests.get(url, headers=headers)
    return response.text

def parse_table(soup):
    try:
        data = soup.find('div', class_ = 'reestr').find_all('table')
        temp_dict = {}
        for row in data:
            # print(row)
            key = row.find('td').text.strip()
            try:
                value = ' '.join(row.find('td', class_ = 'posrel').get_text(strip=True, separator='\n').split('\n')[:-1]).strip()
            except:
                value = None
            temp_dict[key] = value
        return temp_dict
    except:
        return {}

def get_current_person(soup):
    temp_dict = parse_table(soup)
    return {
        'bilet': temp_dict.get('Членский билет'),
        'grade': temp_dict.get('Степень членства'),
        'satisfied': temp_dict.get('Соответствие условиям членства в СРО, предусмотренным законодательством Российской Федерации и (или) внутренними документами СРО'),
        'reestr_number': temp_dict.get('Номер в Реестре РОО'),
        'contacts': temp_dict.get('Контакты'),
        'organization': temp_dict.get('Организация (место работы)'),
        'experience': temp_dict.get('Стаж'),
        'ensurance': temp_dict.get('Страхование деятельности'),
        'compensation': temp_dict.get('Компенсационный фонд')
    }

def get_uncurrent_person(soup):
    temp_dict = parse_table(soup)
    return {
        'excluded': temp_dict.get('Исключен'),
        'stopped': temp_dict.get('Приостановка права осуществления оценочной деятельности'),
        'bilet': temp_dict.get('Членский билет'),
        'grade': temp_dict.get('Степень членства'),
        'reestr_number': temp_dict.get('Номер в Реестре РОО'),
        'contacts': temp_dict.get('Контакты'),
        'organization': temp_dict.get('Организация (место работы)'),
        'experience': temp_dict.get('Стаж'),
        'compensation': temp_dict.get('Компенсационный фонд')
    }    
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
        expanded_dict = get_uncurrent_person(soup)
    else:
        expanded_dict = get_current_person(soup)
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
    url = 'http://sroroo.ru/about/reestr/379972/'
    #url = 'http://sroroo.ru/about/reestr/806693/'
    # with open("index.html", "w") as file:
    #     data = get_user_info(url, headers)
    #     file.write(data)
    with open('index.html', encoding='utf-8') as file:
        data = file.read()
    parsed_data = parse_user_info(data, url)
    pprint(parsed_data)
    