import bs4
import requests
print("Program Started")

def list_process():
    for para in webdata:  # type: object
        savefile.write(para.text)
 #       print(para)
        print("inside para")

urls = ['http://indiagktime.blogspot.com/2009/05/general-knowledge-99.html',
        'http://indiagktime.blogspot.com/2009/05/general-knowledge-98.html',
        'http://indiagktime.blogspot.com/2009/05/general-knowledge-97.html',
        'http://indiagktime.blogspot.com/2009/05/general-knowledge-96.html',
        'http://indiagktime.blogspot.com/2009/05/general-knowledge-100.html',
        'http://indiagktime.blogspot.com/2009/05/general-knowledge-95.html',
        'http://indiagktime.blogspot.com/2009/05/general-knowledge-94.html',
        'http://indiagktime.blogspot.com/2009/05/general-knowledge-93.html',
        'http://indiagktime.blogspot.com/2009/05/general-knowledge-92.html',
        'http://indiagktime.blogspot.com/2009/05/general-knowledge-91.html',
        'http://indiagktime.blogspot.com/2009/05/general-knowledge-90.html',
        'http://indiagktime.blogspot.com/2009/05/general-knowledge-89.html',
        'http://indiagktime.blogspot.com/2009/05/general-knowledge-88.html',
        'http://indiagktime.blogspot.com/2009/05/general-knowledge-87.html',
        'http://indiagktime.blogspot.com/2009/05/general-knowledge-86.html',
        'http://indiagktime.blogspot.com/2009/05/general-knowledge-85.html',
        'http://indiagktime.blogspot.com/2009/05/general-knowledge-84.html',
        'http://indiagktime.blogspot.com/2009/05/general-knowledge-83.html',
        'http://indiagktime.blogspot.com/2009/05/general-knowledge-82.html',
        'http://indiagktime.blogspot.com/2009/05/general-knowledge-81.html',
        'http://indiagktime.blogspot.com/2009/05/general-knowledge-80.html',
        'http://indiagktime.blogspot.com/2009/05/general-knowledge-79.html',
        'http://indiagktime.blogspot.com/2009/05/general-knowledge-78.html',
        'http://indiagktime.blogspot.com/2009/05/general-knowledge-77.html',
        'http://indiagktime.blogspot.com/2009/05/general-knowledge-76.html',
        'http://indiagktime.blogspot.com/2009/05/general-knowledge-75.html',
        'http://indiagktime.blogspot.com/2009/05/general-knowledge-74.html',
        'http://indiagktime.blogspot.com/2009/05/general-knowledge-73.html',
        'http://indiagktime.blogspot.com/2009/05/general-knowledge-72.html',
        'http://indiagktime.blogspot.com/2009/05/general-knowledge-71.html',
        'http://indiagktime.blogspot.com/2009/05/general-knowledge-70.html',
        'http://indiagktime.blogspot.com/2009/05/general-knowledge-69.html',
        'http://indiagktime.blogspot.com/2009/05/general-knowledge-68.html',
        'http://indiagktime.blogspot.com/2009/05/general-knowledge-67.html',
        'http://indiagktime.blogspot.com/2009/05/general-knowledge-66.html',
        'http://indiagktime.blogspot.com/2009/05/general-knowledge-65.html',
        'http://indiagktime.blogspot.com/2009/05/general-knowledge-64.html',
        'http://indiagktime.blogspot.com/2009/05/general-knowledge-63.html',
        'http://indiagktime.blogspot.com/2009/05/general-knowledge-62.html',
        'http://indiagktime.blogspot.com/2009/05/general-knowledge-61.html',
        'http://indiagktime.blogspot.com/2009/05/general-knowledge-60.html']
for url in urls:
     data = requests.get(url)
     soup = bs4.BeautifulSoup(data.text, 'html.parser')
     webdata = soup.find_all('div', {'class': 'post-body entry-content'})
     savefile = open('gk1.txt', 'w', encoding="utf-8")
     print("Before para loop")
     list_process()
     print("after para loop")

savefile.close()
print("Program closed")
