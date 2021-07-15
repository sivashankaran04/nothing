# Take any webpage, Scrape the data and try to insert only the class data and save it in excel

from bs4 import BeautifulSoup
import requests

class_list = set()
url = 'https://en.wikipedia.org/wiki/python'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
tags = {tag.name for tag in soup.find_all()}

for tag in tags:
    for i in soup.find_all(tag):
        if i.has_attr("class"):
            if len(i['class']) != 0:
                class_list.add(" ".join(i['class']))

print(f'CLASS:\n{class_list}')

class_dict = {'Class': [],
              'Text': []}
for clas in class_list:
    content = soup.find('div', {"class": clas})
    text = ''
    try:
        for i in content.findAll('p'):
            text = text + ' ' + i.text
        class_dict['Class'].append(clas)
        class_dict['Text'].append(text)
    except:
        class_dict['Class'].append(clas)
        class_dict['Text'].append('None')

import pandas as pd

df = pd.DataFrame(class_dict)

print(df.head(10))
print(df.tail(10))

df.to_excel('Scraped_class.xlsx')
