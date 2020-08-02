# import libraries
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import csv

#specify the url
urlpage = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"

#Query the website and return the html to the variable 'page'
#page = urllib2.urlopen(wiki)
page = urllib.request.urlopen(urlpage)

#Parse the html in the 'page' variable, and store it in Beautiful Soup format
soup = BeautifulSoup(page,"lxml")

all_tables=soup.find_all('table')

right_table=soup.find('table', class_='wikitable sortable plainrowheaders')

print(right_table.text)

A = []
B = []
C = []
D = []
E = []
F = []
G = []

for row in right_table.find_all("tr"):
    cells = row.find_all('td')
    states = row.find_all('th') #To store second column data
    if len(cells) == [6]:  #Only extract table body not heading
        A.append(cells[0].find(text=True))
        B.append(states[0].find(text=True))
        C.append(cells[1].find(text=True))
        D.append(cells[2].find(text=True))
        E.append(cells[3].find(text=True))
        F.append(cells[4].find(text=True))
        G.append(cells[5].find(text=True))
        print(row.text)

df = pd.DataFrame(A, columns=['Number'])

df['State/UT'] = B

df['Admin_Capital'] = C

df['Legislative_Capital'] = D

df['Judiciary_Capital'] = E

df['Year_Capital'] = F

df['Former_Capital'] = G


