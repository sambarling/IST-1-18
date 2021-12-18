import csv

import requests as rq
from bs4 import BeautifulSoup

HOST = "https://www.reformagkh.ru"


def get_html(url):
    #    time.sleep(5) # it's can help with captcha, but time go too long
    headers = {
        'Cookie': 'route=5e3bd265ed8aaeccd1f9d1d9da8e97db; PHPSESSID=9c6ad4d4f9b035cfbaf7f03d8bd26cfd; _ym_uid=1639679206259492146; _ym_d=1639679206; _ym_isad=2; _ym_visorc=w; __cookieConfirm=1; tid=2283384',
    }
    return rq.get(url, headers=headers).text


def get_soup(url):  # parse url html
    return BeautifulSoup(get_html(url), "html.parser")


def getParamersOfHouseById(houseId):  # getParametrs by houseId
    allSquare = ""
    liveSquare = ""
    countFlat = ""
    countVillages = ""
    countExit = ""
    new_url = f"https://www.reformagkh.ru/myhouse/profile/view/{houseId}/"
    soup = get_soup(new_url)
    datas = soup.findAll("div", class_="house-specs d-flex fw-600 f-14 lh-19 align-items-start mb-3")
    for data in datas:
        if ("Общая площадь, кв.м" in data.text):
            allSquare = data.findAll("div")[-1].text
        if ("Общая площадь жилых помещений, кв.м" in data.text):
            liveSquare = data.findAll("div")[-1].text
        if ("Количество этажей, ед." in data.text):
            countFlat = data.findAll("div")[-1].text
        if ("Численность жителей, чел" in data.text):
            countVillages = data.findAll("div")[-1].text
        if ("Количество подъездов, ед." in data.text):
            countExit = data.findAll("div")[-1].text
    return [allSquare, liveSquare, countFlat, countVillages, countExit]


def parseHouses(url, writer):
    url += "&limit=100&view=list&sort=name&order=asc"
    page = 1
    while (True):  # check all pages
        newUrl = url + f"&page={page}"
        print(newUrl) # logs
        soup = get_soup(newUrl)
        table = soup.find("tbody")
        lines = table.findAll("tr")
        if (len(lines) == 0):
            break
        for line in lines:
            fields = line.findAll("td")
            insertEcsplation = fields[1].text.strip()  # Ввод в эксплатацию
            href = line.find("a", href=True)['href']
            href = HOST + "/myhouse" + href
            houseId = href.split('/')[-2]  # houseId
            houseStreet = line.find("a", href=True).text
            arrParametrs = getParamersOfHouseById(houseId)  # add parametrs
            arrParametrs.append(houseId)
            arrParametrs.append(houseStreet)
            arrParametrs.append(insertEcsplation)
#            print(arrParametrs) # logs
            writer.writerow(arrParametrs)
        page += 1


url = HOST + '/myhouse?tid=2215444'  # this our start point
with open("zhk.csv", 'w', encoding='utf-8', errors='replace', newline="") as file:  # save file
    writer = csv.writer(file, delimiter=',')
    writer.writerow(
        ["Общая площадь", "Общая площадь жилых помещений", "Количество этажей", "Кол-во жителей", "Кол-во подъездов",
         "Идентификационный номер дома", "Почтовый адрес", "Год ввода в эксплуатацию"])  # our headers csv
    parseHouses(url, writer)  # parse houses by url
