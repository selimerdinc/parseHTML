from bs4 import BeautifulSoup
import requests
from tqdm import tqdm,trange
url = requests.get("https://www.imdb.com/chart/top/?ref_=nv_mv_250")   #Sitemize istek attık

# #status_code succes
#
# statusCode=url.status_code  #status_code sorgulaması attığımız istek başarılı mı değil mi öğrenmek için
# print(statusCode) #200 yani attığımız istek başarılı olarak döndü
#
# #page source code
#
# sourceCode=url.content #Sayfa Kaynağını Çektik
# print(sourceCode) #Sayda kaynağı başarılı bir şekilde terminalde gözüküyor.

#parse page code's
soup = BeautifulSoup(url.content , "lxml")
# print(soup)


# #Film Data's on separately
# filmListe=soup.find_all("div",attrs={"class":"titleColumn"})
# filmRating = soup.find_all("td", attrs={"class": "ratingColumn imdbRating"})
# filmYear = soup.find_all("span", attrs={"class": "secondaryInfo"})
# for film in filmListe:
#     print(film.a.text)
# for filmrate in filmRating:
#     print(filmrate.strong.text)
# for year in filmYear:
#     print(year.text)

#film Data's Full Column

filmData=soup.find("tbody",attrs={"class":"lister-list"}).select("tr")
for film in trange(0,250):
    f = open("outputForFilmDetails.txt", "a", encoding="utf-8")
    filmListe = filmData[film].find("td", attrs={"class": "titleColumn"}).select("a")[0].text
    filmRating = filmData[film].find("td", attrs={"class": "ratingColumn imdbRating"}).select("strong")[0].text
    filmYear = filmData[film].find("span", attrs={"class": "secondaryInfo"}).text
    print("\nFilm Adı : {}\nFilm IMDB Rating : {}\nFilm Yayınlanma Tarihi : {}".format(filmListe , filmRating , filmYear),file=f)
    print("-"*40,file=f)
