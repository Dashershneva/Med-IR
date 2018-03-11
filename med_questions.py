import requests
from urllib.request import urlopen
import urllib.request
from lxml import html
from bs4 import BeautifulSoup

main_url = 'https://health.mail.ru/consultation/list/rubric/gastro/'
main_links_list = []
main_links_list.append(main_url)
links = []
n = 2
while n < 738:
    new_url = 'https://health.mail.ru/consultation/list/rubric/gastro/?page=%s' %n
    main_links_list.append(new_url)
    n += 1
i = 0
for item in main_links_list:
    html_links = urllib.request.urlopen(main_links_list[i]).read()
    soup_main = BeautifulSoup(html_links, 'lxml')
    get_links = soup_main.find_all('a', {'class': 'entry__link link-holder'})
    m = 0
    for link in get_links:
        link = get_links[m].get('href')
        if link.startswith('/'):
            links.append(link)
        m += 1
    i += 1
#f = open('questions_text.txt', 'a', encoding = 'utf-8')
#print(main_links_list)
print(len(main_links_list))
#print(links)
print(len(links))
t = 12781
questions = []
for item in links:
    url = 'https://health.mail.ru%s' %links[t]
    url_read = urllib.request.urlopen(url).read()
    soup_url = BeautifulSoup(url_read, 'lxml')
    get_question = soup_url.find('div', {'class': 'entry__description'})
    questions.append(str(get_question.contents))
    #f = open('C:\\Users\\DariaLaptop\\PycharmProjects\\firstpy\\Questions\\questions_text_%s.txt' %t, 'w', encoding='utf-8')
    #f.write(str(get_question.contents))
    #f.close()
    print(t)
    t += 1


print(len(questions))
print(questions[5:7])
