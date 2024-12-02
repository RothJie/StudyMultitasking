import requests
from bs4 import BeautifulSoup

url_li = [f'https://www.cnblogs.com/#p{n}' for n in range(10) ]

def get_data(url):
    resp_ = requests.get(url)
    return resp_.text

def parse_data(html):
    # post-item-title
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all("a",class_='post-item-title')
    return [(link['href'],link.get_text()) for link in links]


if __name__ == '__main__':
    for re in parse_data(get_data(url_li[0])):
        print(re)
