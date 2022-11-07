#!/usr/bin/env python
# coding: utf-8

# <img src="logo.png" height="200" width="900"> 
# 
# #  Сбор данных: грязная работа вашими руками 
# 
# Пришло время самостоятельно написать парсер! Мы будем собирать данные [о ценах на книги.](http://books.toscrape.com)
# 
# 
# > __ВНИМАНИЕ!__ Почему-то у Coursera после обновления на этом задании перестал работать грейдер. В связи с этим все ответы, которые вы получите при написании кода, придется перенести в тест, который идёт в курсе сразу после этого задания. 

# In[1]:


get_ipython().system('pip3 install lxml')


# In[189]:


### ╰( ͡° ͜ʖ ͡° )つ▬▬ι═══════  bzzzzzzzzzz
# will the code be with you
    
# Подгрузите все необходимые для работы пакеты.

# Если ваш код будет ругаться, что нет пакета lxml, установите его 
# Для этого выполните в одной из ячеек команду !pip3 install lxml
from typing import List
import lxml
import time

# your code here
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np


# In[3]:


# фиктивная проверка


# Прогуляйтесь на сайт http://books.toscrape.com/ и изучите его структуру.  
# 
# 
# # 1. Сбор ссылок на книги
# 
# Напишите функцию `get_soup`, которая по ссылке возвращает html-разметку страницы в формате `bs4` 

# In[284]:


def get_page_soup(url_link):
    
    ### ╰( ͡° ͜ʖ ͡° )つ▬▬ι═══════  bzzzzzzzzzz
    # will the code be with you
    
    response = get(url_link)
    html = BeautifulSoup(response.content, 'html.parser')
    
    #print(html.find_all('a'))
    
    
    return html


# In[341]:


main_url = 'http://books.toscrape.com/catalogue/'
page_number = 1

soup = get_page_soup(main_url + f'page-{page_number}.html')
soup


# Напишите функцию `get_books_links`, которая находит в html-разметке страницы ссылки на странички с отдельными книгами. 

# In[347]:


def get_book_links(page_soup) -> List[str]:
    
    ### ╰( ͡° ͜ʖ ͡° )つ▬▬ι═══════  bzzzzzzzzzz
    # will the code be with you
    final_list = []
    response = page_soup.find_all('a')
    for each_element in response:
        if each_element.get('href') != '../index.html' and 'category' not in each_element.get('href')        and 'page' not in each_element.get('href'):
            final_list.append(each_element.get('href'))
    
    return final_list

# your code here


# In[343]:


#soup.find_all('a')[2].get('href')


# In[348]:


def unique(list1):
  
    # initialize a null list
    unique_list = []
  
    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    # print list
    return unique_list


# С помощью цикла соберите в лист `book_links` первые 200 книг.

# In[349]:


### ╰( ͡° ͜ʖ ͡° )つ▬▬ι═══════  bzzzzzzzzzz
# will the code be with you

book_links = []

for i in range (1,51,1):
    page_number = i
    soup = get_page_soup(main_url + f'page-{page_number}.html')
    book_links += get_book_links(soup)

book_links = unique(book_links)
book_links = book_links[:200]

book_links
# your code here


# # 2. Сбор информации о книгах 
# 
# Напишите несколько небольших функций, которые собирают различные данные об одной книге, необходимые для ответов на вопросы ниже. Информацию о книге собирайте в виде словаря вида 
# 
# ```
# { 'name': 'Преступление и наказание', 'rating': 1, 'description': 'ужасно депрессивная книга', ... }
# 
# ```

# In[18]:


#описание, налог, звезды, цена


# In[377]:


df = pd.DataFrame(columns=['Name', 'Description', 'Product Type', 'Price (excl. tax)', 'Price (incl. tax)', 'Tax', 'Score'])


# In[378]:


### ╰( ͡° ͜ʖ ͡° )つ▬▬ι═══════  bzzzzzzzzzz
# will the code be with you

# your code here

for each_link in book_links:
    #time.sleep(2)
    response = get('http://books.toscrape.com/catalogue/' + each_link)
    html = BeautifulSoup(response.content, 'html.parser')


    dictionary = {}

    #Name
    name = html.title.text.strip()
    print(name)
    dictionary['Name'] = name


    #Description
    description = html.findAll("meta")
    print(description[2])
    dictionary['Description'] = str(description[2])


    rows = html.findAll('tr')
    for i in df.columns:
        for item in rows:
            column_name = item.find('th').text
            #print(i, item, column_name)
            if column_name == i:
                value = item.find('td')
                value = value.text
                array.append(value)

                dictionary[column_name] = value

                print(column_name, value)

    #Score
    try: 
        field = html.find('div', {'class':"col-sm-6 product_main"})
        score = field.find('p', {'class':"star-rating Five"})
        print(score)
        dictionary['Score'] = score

    except:
        print(np.nan)
        dictionary['Score'] = np.nan


    df = df.append(dictionary, ignore_index=True)


# In[379]:


df


# In[152]:


#description = html.findAll("meta")
#array.append(description)
#array


# In[87]:


#html.find("article", class_="product_page").findAll('p')


# In[313]:


'''rows = html.findAll('tr')
for row in rows :
    print(row.findAll('td'))'''


# In[314]:


'''for item in rows:
    print(item.find('th').text)
    
    p_tag = item.find('td')
    #print(p_tag.text)
    text = p_tag.text
    print(text)'''


# In[315]:


#t = html.find('p', {'class':"star-rating One"})
'''t = html.find('div', {'class':"col-sm-6 product_main"})
t.find('p', {'class':"star-rating Five"})'''


# Пройдите циклом по всем сыслкам из списка `book_links` и соберите данные о книгах в вектор `book_info`. 

# In[316]:


### ╰( ͡° ͜ʖ ͡° )つ▬▬ι═══════  bzzzzzzzzzz
# will the code be with you

'''main_url = 'http://books.toscrape.com/catalogue/'
book_info = []

for each_link in book_links:
    response = get(main_url+each_link)
    html = BeautifulSoup(response.content, 'html.parser')
    print(html)
    time.sleep(3)'''
    
    
    
# your code here


# Превратим вектор из информации в полноценную таблицу с данными. 

# In[380]:


book_info_df = df
print(book_info_df.shape)
book_info_df.head() 


# Теперь, когда все данные собраны, настало время ответить на несколько вопросов:

# - У скольких книг отсутствует описание? Ответ на этот вопрос вбейте в тест, который идёт после лабораторной работы. 

# In[381]:


### ╰( ͡° ͜ʖ ͡° )つ▬▬ι═══════  bzzzzzzzzzz
# will the code be with you

ans1 = 0
for i in range(0,200):
    if len(df['Description'][i])<55:
        ans1+=1
        #print(i)

# your code here
ans1
#1


# In[386]:


df['Tax'].unique


# - Сколько раз в данных встречается налог, больший нуля?  Ответ на этот вопрос вбейте в тест, который идёт после лабораторной работы. 

# In[384]:


### ╰( ͡° ͜ʖ ͡° )つ▬▬ι═══════  bzzzzzzzzzz
# will the code be with you

ans2 = sum(df[df['Tax']!='£0.00'])

# your code here
ans2
#0


# - Сколько раз рейтинг книги составлял пять звезд?  Ответ на этот вопрос вбейте в тест, который идёт после лабораторной работы. 

# In[366]:


### ╰( ͡° ͜ʖ ͡° )つ▬▬ι═══════  bzzzzzzzzzz
# will the code be with you

ans3 = 200 - sum(df['Score'].isna())

# your code here
ans3

#37


# - Какова средняя цена книг (без учета налога)?  Ответ на этот вопрос вбейте в тест, который идёт после лабораторной работы. 

# In[376]:


### ╰( ͡° ͜ʖ ͡° )つ▬▬ι═══════  bzzzzzzzzzz
# will the code be with you

#df['Price (excl. tax)'] = df['Price (excl. tax)'].map(lambda x: float(x.lstrip('£')))
ans4 = df['Price (excl. tax)'].mean()

# your code here
ans4
#34.79


#  
