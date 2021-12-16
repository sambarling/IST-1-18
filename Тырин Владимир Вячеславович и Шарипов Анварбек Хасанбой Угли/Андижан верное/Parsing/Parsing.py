#Добовляем библиотеки 
from bs4 import BeautifulSoup
import requests
import csv

#Парсинг

#Задаем ссылку 
URL='https://data.gov.uz/ru/datasets/13521'
#Используем Юзер-Агента от обхода Проверок
HEADERS={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 OPR/80.0.4170.91'
    }
response=requests.get(URL,headers=HEADERS)
soup=BeautifulSoup(response.content,'html.parser')
#Задаем атрибуты контейнера в котором содержится элементы парсинга 
items=soup.find('div',class_='table-responsive')
#Comps- пустой словарь, в который сохраняются все полученные данные
comps=[]

#Задаем атрибуты поиска парсинга
for item in items:
    comps.append({

    'title':item.find('tbody').get_text(strip=True)
    })
for comp in comps:
    print (comp['title'])

#Сохраняем информацию в csv расшерении  
with open('pars.csv', 'w', encoding='UTF-8', newline='') as file:
    writer = csv.writer(file, delimiter='\n')
    writer.writerow(comps)








