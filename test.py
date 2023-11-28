import re
import requests
from bs4 import BeautifulSoup

from api import get_detail_of_course

url = 'https://www.fanshawec.ca/programs/anc1-3d-animation-and-character-design'

response = requests.get(url)
datas = [{'name': '3D Animation and Character Design'}]

if response.status_code == 200:
    get_detail_of_course(url, '3D Animation and Character Design', datas)
    print(datas)

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")