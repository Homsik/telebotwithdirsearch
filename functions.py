# -*- coding: utf-8 -*-
import re
import os
import urllib.request
from bs4 import BeautifulSoup

def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read() #Получение данных на сайте
def parse(html = get_html('https://yandex.ru/pogoda/perm/')):
    soup = BeautifulSoup(html, features = "html.parser")
    temperature = (soup.find('span', class_ = 'temp__value'))
    return re.sub(u"[<>a-zA-Z\"=/_\n ]", '', temperature.prettify())
def main():
    parse()
if __name__ == '__main__':
    main()
