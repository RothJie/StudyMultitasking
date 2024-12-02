import csv

import requests
import datetime
from bs4 import BeautifulSoup

today_ = datetime.date.today().strftime('%Y-%m-%d')

startdate_li = [(datetime.date.fromisoformat(today_)-datetime.timedelta(29*i)).strftime('%Y-%m-%d') for i in range(24)]
url_li = [(f"https://www.wentian123.com/history/?location=%E6%88%90%E9%83%BD&"
           f"{startdate_li[o+1]}&enddate={startdate_li[o]}") for o in range(len(startdate_li)-1)]

def dowload(url):
    print(f"正在加载html：{url}")
    resp_ = requests.get(url)
    html_ = resp_.text
    return html_

def parse(html):
    soup = BeautifulSoup(html, 'html.parser')
    tr_elements = soup.find_all('tr')

    resluts = []

    for tr in tr_elements[1:]:
        week = tr.find_all("p")[0].get_text()
        date = tr.find_all("p")[1].get_text()
        weather_condition =  (tr.find_all("p")[3].get_text()).strip('\n')
        temperature = tr.find_all("p")[4].get_text()
        high_temp,low_temp = (temperature[:3]).strip(''),temperature[5:]
        wind_force = tr.find_all("p")[5].get_text()
        resluts.append([date,week,high_temp,low_temp,weather_condition,wind_force])
    return resluts


if __name__ == '__main__':
    print(url_li[0])
    html = dowload(url_li[0])
    print(parse(html))
    data = parse(html)
    headers = ['date','week','high_temp','low_temp','weather_condition','wind_force']
    with open('weather.csv', 'a', newline='\n',encoding='utf-8') as f_csv:
        writer = csv.writer(f_csv)
        writer.writerow(headers)
        writer.writerows(data)

