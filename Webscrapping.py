import bs4
import requests

print("Program started")
savefile = open('scrappe08122019.txt', 'a', encoding="utf-8")
url = "http://indiagktime.blogspot.com/2009/05/general-knowledge-43.html"
data = requests.get(url)
soup = bs4.BeautifulSoup(data.text, 'html.parser')
webdata = soup.find_all('div', {'class': 'post-body entry-content'})
#webdata = soup.find_all('table', {'id': 'Table1'})
# webdata = soup.find_all('div', {'id': 'gvQuestionPaper'})
# with open("tech.txt", 'w') as outfile:
for para in webdata:
    savefile.write(para.text)
    print(para)
savefile.close()
print("Program ends")
#    print(para.text)
