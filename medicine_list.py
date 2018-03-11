import requests
from urllib.request import urlopen
import urllib.request
from lxml import html
from bs4 import BeautifulSoup
import re
import csv
from pymystem3 import  Mystem

main_url = 'https://www.rlsnet.ru/tn_alf.htm'
html_main = urllib.request.urlopen(main_url).read()
soup_main = BeautifulSoup(html_main, 'lxml')
get_links = soup_main.find('table', {'class' : 'alf_letters alphabet__rustable'}).find_all('a')

#print(get_links)

m = 0
links = []
for item in get_links:
    link = get_links[m].get('href')
    links.append(link)
    m += 1

i = 0
med_list = []
for item in links:
    if links[i].startswith('//www'):
        links[i] = links[i].replace('//', 'https://')
        html_link = urllib.request.urlopen(links[i]).read()
        soup_link = BeautifulSoup(html_link, 'lxml')
        get_med = soup_link.find('div', {'class' : 'tn_alf_list'}).find_all('a')
        n = 0
        for med in get_med:
            medicine = get_med[n].contents[0]
            if not str(medicine).startswith('<'):
                med_list.append(str(medicine))
                #csv_writer.writerow(str(medicine))
            n +=1
    else:
        links[i] = 'https://www.rlsnet.ru' + links[i]
        html_link = urllib.request.urlopen(links[i]).read()
        soup_link = BeautifulSoup(html_link, 'lxml')
        get_med = soup_link.find('div', {'class': 'tn_alf_list'}).find_all('a')
        n = 0
        for med in get_med:
            medicine = get_med[n].contents[0]
            if not str(medicine).startswith('<'):
                med_list.append(str(medicine).lower())
                #csv_writer.writerow(str(medicine))
            n += 1
        #print(links[i])
    i += 1
"""
csv_file = open('med_list.csv', 'a', encoding='utf-8')
csv_writer = csv.writer(csv_file)
t = 0
for item in med_list:
    csv_writer.writerow(med_list[t].replace(',', ''))
    t += 1
"""
print(len(med_list))

drug_list = []
for drug in sorted(set(med_list)):
    drug_list.append(drug.lower())
