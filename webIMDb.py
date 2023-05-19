from csv import writer
from bs4 import BeautifulSoup
import requests


try:
    source=requests.get('https://www.imdb.com/chart/top/')
    source.raise_for_status()
    
    soup=BeautifulSoup(source.text,'html.parser')
    #print(soup)
    movies=soup.find('tbody',class_="lister-list").find_all('tr')
    #print(len(movies))

    with open('IMDB Top 250 Movies.csv','w',encoding='utf8',newline='')as f:
        thewriter=writer(f)
        header=['Rank of Movie','Movie Name','Year of Release','Rating of Movie']
        thewriter.writerow(header)

        
           
        for movie in movies:

            name=movie.find('td',class_="titleColumn").a.text

            rank=movie.find('td',class_="titleColumn").get_text(strip=True).split('.')[0]

            #year=movie.find('span',class_="secondaryInfo").text

            year=movie.find('td',class_="titleColumn").span.text.strip("()")

            rating=movie.find('td',class_="ratingColumn imdbRating").strong.text

            #print(rank,name,year,rating)
            info=[rank,name,year,rating]
            thewriter.writerow(info)

        



except Exception as e:
    print(e)
