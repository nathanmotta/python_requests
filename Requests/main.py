import csv
from bs4 import BeautifulSoup
import requests
url = 'https://cve.mitre.org/'
r = requests.get(url)
# print(r.content)

soup = BeautifulSoup(r.content, 'html5lib')
print("*****HTML*****")
print(soup.prettify())
