#-*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
from tqdm import tqdm

count=0
for piNo in tqdm(range(1,50),colour="#4a3356",desc="İstek Atılıyor..."):
    url= requests.get("https://www.trendyol.com/sr?wc=109460&pa=true&pi="+str(piNo))
    soup=BeautifulSoup(url.content,"lxml")
    phoneCode=soup.find_all("div",attrs={"class":"p-card-chldrn-cntnr"})
    for phone in phoneCode:
        f=open("outputForPhoneDetails.txt","a",encoding="utf-8")
        productName=phone.find("span",attrs={"class":"prdct-desc-cntnr-ttl"}).text
        try:
            productFullName =phone.find("span",attrs={"class":"prdct-desc-cntnr-name hasRatings"}).text
        except Exception:
            print("İsim bulunamadı..",file=f)
        productLink=phone.a.get("href")
        try:
            productPrice=phone.find("div",attrs={"class":"prc-box-dscntd"}).text
        except Exception:
            print("Fiyat Girilmemiş",file=f)
        # print(productLink)
        link="http://www.trendyol.com"
        productHref=link+productLink
        productHref.replace("[]","")
        productHref.replace("200","")
        # print(productLink)
        print("Marka = ",productName,file=f)
        print("İsim = ",productFullName,file=f)
        print("Fiyat = ",productPrice,file=f)

        # # print("Link = ",productLink)
        # # print()
        productDetail=requests.get(productHref)
        count+=1
        # print(productDetail.status_code)
        pd=BeautifulSoup(productDetail.content,"lxml")
        try:
            attributes=pd.find("div",attrs={"class":"starred-attributes"}).select("li")
            bar=tqdm(attributes,unit=" product",desc="Ürünler Çekilmeye Başlandı..",colour="#f8f4ff")
            for product in bar:
                productFirstTitle=product.span.text
                productSecondTitle=product.find("span", attrs={"class": "attribute-value"}).text
                print(productFirstTitle," - ",productSecondTitle,file=f)
        except Exception:
            print("Ürün detayı alınamadı..",file=f)
        print("#"*80,file=f)
    print("---***-***-***-***-***--- Toplam Özelliği Getirilen Ürün : ",count,"---***-***-***-***-***---",file=f)