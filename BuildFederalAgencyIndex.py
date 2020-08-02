import requests
from bs4 import BeautifulSoup
from string import ascii_lowercase

print('Program Start')

savefile = open('currentaf.txt', 'a', encoding="utf-8")
base_url = 'https://www.usa.gov/federal-agencies/'
for letter in ascii_lowercase:
    url = '{}{}'.format(base_url, letter)
    print(url)
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')

    for ul in soup.find_all('ul', {'class': 'one_column_bullet'}):
#        print(ul)
        savefile.write(ul.text)

print('Program End')