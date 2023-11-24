import requests
from bs4 import BeautifulSoup

# 定义目标URL
url = 'https://www.fanshawec.ca/programs/anc1-3d-animation-and-character-design/'

# 发送GET请求获取页面内容
response = requests.get(url)

# 检查请求是否成功
if response.status_code == 200:
    # 使用BeautifulSoup解析页面内容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 查找包含"ADMISSION REQUIREMENTS"信息的元素
    admission_requirements_element_h2 = soup.find('h2', {'id': 'admission-requirements'})
    admission_requirements = admission_requirements_element_h2.find_next('div')

    # 提取文本信息
    admission_requirements_text = admission_requirements.get_text(strip=True)

    # 打印提取的信息
    print(admission_requirements_text)

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
