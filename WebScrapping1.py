import bs4
import requests
# import csv
#url = "http://www.withoutbook.com/Technology.php?tech=42&subject=JDBC%20Interview%20Questions%20and%20Answers"
url = "http://www.withoutbook.com/Technology.php?tech=42&page=6&subject=JDBC%20Interview%20Questions%20and%20Answers"
data = requests.get(url)
soup = bs4.BeautifulSoup(data.text, 'html.parser')
#webdata = soup.find_all('div', {'align': 'justify'})
webdata = soup.find_all('div', {'class': 'news'})
#webdata = soup.find_all('div', {'dir': 'ltr'})
#webdata = soup.find_all('div', {'id': 'gvQuestionPaper'})
for para in webdata:
#=    outp.write(para.txt)
    print(para.text)

