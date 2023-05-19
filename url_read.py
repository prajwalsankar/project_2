from bs4 import BeautifulSoup
import requests


url = "https://web.saumag.edu/housing/options/"
page = requests.get(url)
page.raise_for_status()
#print(page)
soup=BeautifulSoup(page.content,'html.parser')
#print(soup)

body = soup.find_all('div', class_="search-filter-results")
print(body)
houses=body[0].find_all('div',class_='dp-title')
#print(houses)

#rows = soup.a()
#print(rows)
'''
for row in body:
    hello={}
    hello['room']=row.find('div',class_="size").text
    print(hello)
'''
