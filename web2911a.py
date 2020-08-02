import bs4

import requests

#import csv

url = "http://www.deled.co.in/up-tet-answer-key-primary-child-psychology-19-dec-2016/"
data = requests.get(url)
page_soup = bs4.BeautifulSoup(data.text, 'html.parser')

containers = page_soup.find_all('ol')

filename = "question1.csv"
f = open(filename, "w")

headers = "question, option1, option2, option3, option4\n"

f.write(headers)

for container in containers:
    brand = container.ol
#    question_Name = brand[0].text.strip()

    print("container: " + question)

    f.write(question)

f.close()
