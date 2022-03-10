from re import search
import requests
from bs4 import BeautifulSoup

base_url = "https://www.agemys.com"
query = "/search?query=" + input("请输入搜索内容: ")

soup = BeautifulSoup(requests.get(base_url+query).text,'lxml')
result = soup.find("a",attrs={'calss','cell_imform_name'})['href']
print(base_url + result)