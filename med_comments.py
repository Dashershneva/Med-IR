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


mystem = Mystem()
comment_lemma = []
n = 0
all_comments_list = []
for item in all_comments:
    all_comments_list.append(all_comments[n][0])
    lemma = mystem.lemmatize(all_comments[n][0])
    comment_lemma.append(''.join(lemma))
    n += 1


#print(comment_lemma)
print(len(medicine_list.med_list))

med_list = medicine_list.med_list

medicine_dict = dict.fromkeys(med_list)
"""
for text in comment_lemma:
    text_clean = re.sub(u"\W", ' ', text)
    text_split = text_clean.split(' ')
    for word in text_split:
        word_key = word in medicine_dict
        if word_key == True:
            print(word, text)

"""
"""
conn = sqlite3.connect('new_medicine_db.db')
c = conn.cursor()
c.execute('''CREATE TABLE comments (text_number, text, medicine)''')
conn.commit()

query = ("INSERT INTO comments (text_number, text, medicine) " \
                " VALUES (?,?,?)")
z
g = 0
while g < 14730:
    f = open('C:\\Users\\DariaLaptop\\PycharmProjects\\firstpy\\Questions\\questions_text_%s.txt' %g, 'r', encoding='utf-8')
    a = f.read()
    a = a.replace('\\n', '')
    a = a.replace('\\t', '')
    a = re.sub(u"\W", ' ', a)
    lemma = mystem.lemmatize(a)
    a_lem = ''.join(lemma)
    medicines = []
    for medicine in list(set(med_list)):
        if " " + medicine in a_lem.lower():
            relevant_file = open('C:\\Users\\DariaLaptop\\PycharmProjects\\firstpy\\Questions_relevant\\questions_original_text_%s.txt' % g, 'w', encoding='utf-8')
            relevant_file.write(a)
            relevant_file.close()
            medicines.append(medicine)
    if medicines != []:
        relevant_file = open('C:\\Users\\DariaLaptop\\PycharmProjects\\firstpy\\Questions_relevant\\questions_original_text_%s.txt' % g, 'w', encoding='utf-8')
        relevant_file.write(a)
        relevant_file.close()
        data = [(g, a, str(medicines))]
        c.executemany(query, data)
        conn.commit()
    print(g)
    g += 1
"""

