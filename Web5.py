import requests, bs4, csv

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
page = requests.get("https://www.investing.com/currencies/eur-usd-historical-data", headers=headers)

soup = bs4.BeautifulSoup(page.content, 'html.parser')

results_table = soup.find(id='results_box')

dates = results_table.find_all(class_="first left bold noWrap")

#=values = results_table.find_all(class_="noWrap pointer") #pradyut

length = len(dates)
#length1 = len(values)
info = results_table.find_all('td')

cost = info[1:length * 6 + 1:6]
opens = info[7:length * 6 + 1:6]
high = info[13:length * 6 + 1:6]
low = info[19:length * 6 + 1:6]
changes = info[25:length * 6 + 1:6]
final = []

#print(lenght)

with open('finaly.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)

    for i in range(length):
        filewriter.writerow([dates[i].get_text(), cost[i].get_text(), opens[i].get_text(), high[i].get_text(), low[i].get_text(), changes[i].get_text()])


