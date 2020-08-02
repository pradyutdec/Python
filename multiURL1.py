import requests
from bs4 import BeautifulSoup
from string import digits
import datetime



print('Program Start')
#print(Date)
savefile = open('currentaf.txt', 'w', encoding="utf-8")
base_url = 'https://www.fresherslive.com/current-affairs/0'
for letter in digits:
    url = '{}{}'.format(base_url,letter +'-april-2019-quiz')
    print(url)
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')

    for para in soup.find_all('div', {'class': 'col span_2_of_3'}):
        print(para)
        savefile.write(para.text)

print('Program End')