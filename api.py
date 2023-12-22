import re
import requests
from bs4 import BeautifulSoup

# Define target URL
url = 'https://www.fanshawec.ca/programs-and-courses'
url_index = 'https://www.fanshawec.ca'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}


def get_count_of_pages():
    # Send a GET request to obtain page content
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Use BeautifulSoup to parse page content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Get the page number of the last page
        href_last_button = soup.find('div', {'class': 'pager__item pager__item--last'}).find('a').get('href')
        number_last_page = int(re.findall(r'\d+', href_last_button)[0])
        return number_last_page

    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return ''


def get_detail_of_course(detail_url, name, datas):
    response = requests.get(detail_url)
    # Check if the request was successful
    if response.status_code == 200:
        # Use BeautifulSoup to parse page content
        soup = BeautifulSoup(response.text, 'html.parser')

        for data in datas:
            if data['name'] == name:
                # Find elements containing "ADMISSION REQUIREMENTS" information
                admission_requirements_element_h2 = soup.find('h2', {'id': 'admission-requirements'})
                if admission_requirements_element_h2 is not None:
                    admission_requirements = admission_requirements_element_h2.find_next('div').text
                    data['admission requirements'] = admission_requirements

                # Find elements containing "PROGRAM OVERVIEW" information
                program_overview_list_element_h2 = soup.findAll('h2', {'class': 'block__title'})
                for i in program_overview_list_element_h2:
                    if i.text == 'Program Overview':
                        data['program overview'] = i.find_next('div').text

                # Find elements containing 'cost' information
                cost_div = soup.find('div', {'class': 'international-cost-block cost-block'})
                if cost_div is not None:
                    cost = cost_div.find('div', {'class': 'fees-cost'})
                    if cost is not None:
                        data['cost'] = cost.text

                # Find elements containing 'LEARNING OUTCOMES' information
                learning_outcomes_title = soup.find('div', {'class': 'details-wrapper'})
                if learning_outcomes_title is not None:
                    data['learning outcomes'] = learning_outcomes_title.text

                # Find elements containing Academic School information
                academic_school = soup.find('div', {'class': 'academic-school'})
                if academic_school is not None:
                    data['academic school'] = academic_school.text

    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return ''
    return 0


def get_dict_of_course(page, datas):
    # Send a GET request to obtain page content
    params = {'page': str(page)}
    response = requests.get(url, params=params, headers=headers)

    # Use BeautifulSoup to parse page content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Get the div of each course
    list_course = soup.findAll('a', {'class': 'field--title'})

    for course in list_course:
        # Get name of course
        name_course = course.find('span').text
        datas.append({'name': name_course})

        # Get uri
        href = course.get('href')
        get_detail_of_course(url_index + href, name_course, datas)
