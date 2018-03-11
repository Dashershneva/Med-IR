import requests
from urllib.request import urlopen
import urllib.request
from lxml import html
from bs4 import BeautifulSoup
import re
from pymystem3 import Mystem
import  medicine_list
import sqlite3

main_url = 'https://health.mail.ru/disease/rubric/gastroenterology/'
html_main = urllib.request.urlopen(main_url).read()
soup_main = BeautifulSoup(html_main, 'lxml')
get_links = soup_main.find('div', {'class' : 'column column_content'}).find_all('a')
m = 0
links = []
for item in get_links:
    link = get_links[m].get('href')
    links.append(link)
    m += 1

all_comments = []
n = 0
for item in links:

    url = 'https://health.mail.ru%scomments/' %links[n]

    html = urllib.request.urlopen(url).read()

    soup = BeautifulSoup(html, 'lxml')
    comments = soup.find_all('div', {'class': 'comment__text'})
    #print(comments)
    i = 0
    for item in comments:
        try:
            all_comments.append(comments[i].contents)
        except AttributeError:
            pass
        i += 1
    n += 1

print(len(medicine_list.med_list))

med_list = medicine_list.med_list

reg = 'PR=|CONJ=|APRO=*|PART='

mystem = Mystem()

word_form_dict = {}
g = 0
while g < 5000:
    f = open('C:\\Users\\DariaLaptop\\PycharmProjects\\firstpy\\Questions\\questions_text_%s.txt' %g, 'r', encoding='utf-8')
    print(type(f))
    a = f.read()
    a = a.replace('\\n', '')
    a = a.replace('\\t', '')
    a = re.sub(u"\W", ' ', a)
    lemma = mystem.lemmatize(a)
    a_lem = ''.join(lemma)
    medicines = []
    for medicine in list(sorted(set(med_list))):
        try:
            if " " + medicine in a_lem.lower():
                t = re.search('%s .*' % medicine, a_lem.lower())
                p = t.group(0)
                p = p.split(' ')
                p = mystem.analyze(' '.join(p))
                p_clean = []
                # print(p)
                i = 0
                for item in p:
                    if type(p[i]) == dict:
                        analysis_key = 'analysis' in p[i]
                        if analysis_key == True:
                            word = p[i]['analysis']
                            if word != [] and not re.search(reg, word[0]['gr']):
                                word_form = word[0]['lex']
                                p_clean.append(word_form)
                    i += 1
                if len(p) > 15:
                    p = p_clean[1:16]
                else:
                    p = p_clean[1:len(p)]
                m = mystem.analyze(' '.join(p))
                i = 0
                for item in m:
                    if type(m[i]) == dict:
                        analysis_key = 'analysis' in m[i]
                        if analysis_key == True:
                            word = m[i]['analysis']
                            if word != [] and not re.search(reg, word[0]['gr']):
                                word_form = word[0]['lex']
                                if word_form in word_form_dict:
                                    word_form_dict[word_form] += 1
                                else:
                                    word_form_dict[word_form] = 1
                    i += 1
        except AttributeError:
            pass
    print(g)
    print(type(f))
    g += 1

file = open('C:\\Users\\DariaLaptop\\PycharmProjects\\firstpy\\dict_all.txt', 'w', encoding='utf-8')
file.write(str(word_form_dict))
file.close()

print(word_form_dict)