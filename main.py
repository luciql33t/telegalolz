import requests
import bs4 as bs
import time


url = 'https://t.me/'
t = 2000000

with open('list.txt', 'r') as f:
    ids = [line.strip() for line in f]


while True:
    for id in ids:
        page = requests.get(url + id)
        soup = bs.BeautifulSoup(page.text, 'html.parser')
        stat = soup.findAll('div', class_='tgme_page_title')
        if not stat:
            print(id + ' ----------------------------------------!!!')
            with open('file.txt', 'a') as file:
                file.write(id + '\n')
        else:
            print(id + ' ')
        time.sleep(1)
    time.sleep(t)






print(stat)