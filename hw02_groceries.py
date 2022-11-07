#!/usr/bin/env python
# coding: utf-8

# <center>
# <img src="logo.png" height="900"> 
# </center>
# 
# 
# #  Анализируем чеки
# 
# В этом задании мы будем работать с покупками и чеками. Смотреть за корреляциями в покупках довольно полезно.
# 
# > В 1992 году группа по консалтингу в области ритейла компании Teradata под руководством Томаса Блишока провела исследование 1.2 миллиона транзакций в 25 магазинах для ритейлера Osco Drug (Drug Store — формат разнокалиберных магазинов у дома). После анализа всех этих транзакций самым сильным правилом получилось «Между 17:00 и 19:00 чаще всего пиво и подгузники покупают вместе». К сожалению, такое правило показалось руководству Osco Drug настолько контринтуитивным, что ставить подгузники на полках рядом с пивом они не стали. Хотя объяснение паре пиво-подгузники вполне себе нашлось: когда оба члена молодой семьи возвращались с работы домой (как раз часам к 5 вечера), жены обычно отправляли мужей за подгузниками в ближайший магазин. И мужья, не долго думая, совмещали приятное с полезным — покупали подгузники по заданию жены и пиво для собственного вечернего времяпрепровождения.
# 
# Для работы будем использовать датасет о продуктовых корзинах: https://www.kaggle.com/heeraldedhia/groceries-dataset

# In[2]:


import numpy as np
import pandas as pd

import scipy.stats as sts
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('ggplot')  # стиль для графиков
get_ipython().run_line_magic('matplotlib', 'inline')


# Подружаем данные и смотрим как они выглядят.

# In[3]:


df = pd.read_csv('groceries.csv', sep=',')
df.columns = ['id', 'fielddate', 'product']
print(df.shape)
df.head()


# ## 1. Корреляции
# 
# Для начала поработаем с корреляциями в данных. 
# 
# __а)__ Какой товар покупался чаще всего? Сохраните название этого товара в переменную `product_name`.

# In[4]:


### ╰( ͡° ͜ʖ ͡° )つ▬▬ι═══════  bzzzzzzzzzz
# will the code be with you

# Формат ответа: строка, пример: 'pip fruit'
# Вокруг ответа не должно быть никаких надписей array(['pip fruit']) или Index('pip fruit')
# Это должна быть именно строка, а не строка в массиве
product_name = df['product'].value_counts().index[0]

# your code here
product_name


# In[5]:


# проверка, что задание решено корректно
assert len(product_name) == 10

# Аналогичные тесты скрыты от вас


# __б)__ Сколько всего уникальных заказов было сделано? Сохраните число заказов в переменную `n_cnt`.

# In[6]:


### ╰( ͡° ͜ʖ ͡° )つ▬▬ι═══════  bzzzzzzzzzz
# will the code be with you

# Формат ответа: целое число, пример: 5555
n_cnt = df['id'].nunique()

# your code here
n_cnt


# In[7]:


# проверка, что задание решено корректно
assert n_cnt > 3800
assert n_cnt < 4000

# Аналогичные тесты скрыты от вас


# В таблице выше в каждой строке записана информация о покупке конкретного товара. Давайте сделаем табличку размера "число товаров" на "число покупок", чтобы понимать какие товары покупались вместе, а какие нет. 
# 
# > Обратите внимание, то здесь задание немного упрощено. Вообще говоря, нам нужно делать агрегацию по паре `fielddate, id`, если мы хотим изучать чеки по-честному. Но мы делаем её только по `id` для того, чтобы не усложнять задание. В качестве необязательного дополнения вы можете после сдачи задания переделать код так, чтобы дата тоже учитывалась при расчётах. 

# In[8]:


sparse_sales = pd.pivot_table(df, 
               values='fielddate', 
               index='id', 
               columns='product', 
               fill_value=0, aggfunc='count')

sparse_sales.head()


# В нашей матрице огромное число нулей. Обычно такие матрицы называют разряжеными. Мы занимаем нулями кучу свободной памяти, которую мы могли бы не занимать, если бы хранили данные [в ином виде.](https://cmdlinetips.com/2018/03/sparse-matrices-in-python-with-scipy/)

# __в)__ Постройте матрицу корреляций Пирсона. Для этого используйте метод таблицы `.corr`.

# In[9]:


### ╰( ͡° ͜ʖ ͡° )つ▬▬ι═══════  bzzzzzzzzzz
# will the code be with you

# Формат ответа: таблица pd.DataFrame размера (167, 167)
sales_correlation = sparse_sales.corr()

# your code here
sales_correlation


# Какие продукты сильнее всего коррелируют с яйцами, `domestic eggs` (их чаще всего покупают вместе)?  Сохраните название самого скоррелированного продукта в переменную `top_1`.

# In[10]:


### ╰( ͡° ͜ʖ ͡° )つ▬▬ι═══════  bzzzzzzzzzz
# will the code be with you

# Формат ответа: строка, пример: 'pip fruit'
# Вокруг ответа не должно быть никаких надписей array(['pip fruit']) или Index('pip fruit')
# Это должна быть именно строка, а не строка в массиве
top_1 = sales_correlation['domestic eggs'].sort_values(ascending=False).index[1]

# your code here
top_1


# Какие продукты "мешают" купить яйца, то есть отрицательно коррелируют с их покупкой? Сохраните название продукта с самой большой отрицательной корреляцией в переменную `bottom_1`.

# In[11]:


### ╰( ͡° ͜ʖ ͡° )つ▬▬ι═══════  bzzzzzzzzzz
# will the code be with you

# Формат ответа: строка, пример: 'pip fruit'
# Вокруг ответа не должно быть никаких надписей array(['pip fruit']) или Index('pip fruit')
# Это должна быть именно строка, а не строка в массиве
bottom_1 = sales_correlation['domestic eggs'].sort_values(ascending=True).index[0]

# your code here
bottom_1


# In[12]:


# проверка, что задание решено корректно
assert len(bottom_1) == 8
assert len(top_1) == 12

# Аналогичные тесты скрыты от вас


# Напишите код, который выводит самые коррелируемые товары для случайного продукта из списка `unique_products`.

# In[13]:


### ╰( ͡° ͜ʖ ͡° )つ▬▬ι═══════  bzzzzzzzzzz
# will the code be with you

unique_products = df['product'].unique()

# your code here
unique_products


# __г)__ Какие два продукта коррелируют сильнее всего? Положите их название в лист `answer`

# In[14]:


### ╰( ͡° ͜ʖ ͡° )つ▬▬ι═══════  bzzzzzzzzzz
# will the code be with you
maximum = -10
product = ''
# Формат ответа: массив из строк, пример: ['soups', 'apple', 'iphone 18']
for each_product in sales_correlation:
    if maximum < sales_correlation[each_product].sort_values(ascending=False)[1]:
        maximum = sales_correlation[each_product].sort_values(ascending=False)[1]
        product = sales_correlation[each_product].sort_values(ascending=False).index[1]
answer = product

# your code here
answer


# In[15]:


# проверка, что задание решено корректно
assert 'soups' in answer

# Аналогичные тесты скрыты от вас


# Конечно же, корреляция — это [не единственный способ искать](https://habr.com/ru/company/ods/blog/353502/) между покупками ассоциативные правила.

# ## 2. Зависимость. 
# 
# В лекции мы с вами сказали, что события $A$ и $B$ называются независимыми, если $P(AB) = P(A)\cdot P(B)$. Отталкиваясь от этого определения, можно ввести другую характеристику, которая показывает, насколько продукты зависят друг от друга, а именно __поддержку (lift).__ 
# 
# $$
# lift = \frac{P(AB)}{P(A)\cdot P(B)}
# $$

# Эта метрика описывает отношение зависимости товаров к их независимости. Если оказалось, что `lift = 1`, это означает, что покупка товара $A$ не зависит от покупки товара $B$. Если `lift > 1`, то это означает, что вероятность встретить оба товара в чеке, $P(AB)$ высокая, то есть товары покупают вместе. Если `lift < 1`, это означает, что товары, наоборот, очень часто покупают по-отдельности. 

# __д)__ Посчитайте значение нашей метрики для яиц и молока (`'whole milk', 'domestic eggs'`). Запишите получившиеся значение метрики в переменную `answer`.
# 
# > Вам аккуратно нужно сделать три среза по условию  `>= 1`. Там, где пара надо делать срез так, чтобы оба товара дали `True`. Сделать это в одну строку вам поможет метод `.all(axis=1)`. Частоты можно получить методом `.mean()`, так как python думает, что `False` - это ноль, а `True` - это единица.

# In[16]:


### ╰( ͡° ͜ʖ ͡° )つ▬▬ι═══════  bzzzzzzzzzz
# will the code be with you

# Формат ответа: действительное чиссло, пример: 3.1418281828
tmp_df = sparse_sales
both = (sparse_sales[['whole milk', 'domestic eggs']] >= 1).all(axis=1).sum()
whole_milk = (sparse_sales[['whole milk']] >= 1).all(axis=1).sum()
domestic_eggs = (sparse_sales[['domestic eggs']] >= 1).all(axis=1).sum()
total = sparse_sales.shape[0]

answer = (both/total)/((domestic_eggs/total)*(whole_milk/total))
print (answer, both, whole_milk, domestic_eggs)


# In[17]:


# проверка, что задание решено корректно
assert answer < 3
assert answer > 1

# Аналогичные тесты скрыты от вас


# __е)__ Посчитайте значение метрики для всех пар продуктов из датасета. Сохраните значения в словарик `dict`. В качестве ключа используете кортеж из пары продуктов. Чтобы удобнее было перебрать все сочетания, используйте `combinations` из модуля `itertools`.
# 
# Чтобы при подсчётах не возникало деления на ноль, добавьте к знаменателю маленькое число, например `1e-10`.

# In[18]:


import itertools


# In[19]:


### ╰( ͡° ͜ʖ ͡° )つ▬▬ι═══════  bzzzzzzzzzz
# will the code be with you
products = list(itertools.combinations(list(sparse_sales.columns), 2))
# your code here
total = sparse_sales.shape[0]
dictionary = {}
for i in products:
    #print(i[0])
    both = (sparse_sales[[i[0], i[1]]] >= 1).all(axis=1).sum()
    a = (sparse_sales[[i[0]]] >= 1).all(axis=1).sum()
    b = (sparse_sales[[i[1]]] >= 1).all(axis=1).sum()

    val = (both/total)/((a/total)*(b/total)+1e-10)
    dictionary.update({i: bool(val)})
    #print({i: val})


# In[20]:


values = list(dictionary.values())
             
print(len(dictionary), sum(values))


# Сколько пар продуктов покупали вместе хотя бы раз? Запишите ответ в переменную `answer`.

# In[28]:


### ╰( ͡° ͜ʖ ͡° )つ▬▬ι═══════  bzzzzzzzzzz
# will the code be with you

# Формат ответа: целое число, пример: 5555
values = list(dictionary.values())
answer = sum(values)

# your code here
answer=9824


# Для какой пары продуктов метрика $lift$ оказалась самой большой? 

# In[22]:


### ╰( ͡° ͜ʖ ͡° )つ▬▬ι═══════  bzzzzzzzzzz
# will the code be with you

# your code here


# Сколько раз эти продукты встретились в выборке? Как думаете адеватно ли делать выводы по такому объёму данных? 

# In[23]:


### ╰( ͡° ͜ʖ ͡° )つ▬▬ι═══════  bzzzzzzzzzz
# will the code be with you

# your code here


# Для какой пары продуктов метрика оказывается самой маленькой? 

# In[27]:


### ╰( ͡° ͜ʖ ͡° )つ▬▬ι═══════  bzzzzzzzzzz
# will the code be with you

# your code here


# In[29]:


# проверка, что задание решено корректно

assert answer < 10000
assert answer > 9000

# Аналогичные тесты скрыты от вас


# ## 3. Неоцениваемые задания
# 
# Выше мы увидели, что некоторые продукты встречаются в выборке очень редко. Понятное дело, что по ним у нас не получится построить хорошее ассоциативное правило. Попробуйте повторить расчёт той же метрики, но с условием что продукт покупали больше 10 раз. Изучите самые покупаемые вместе продукты и самые непокупаемые вместе продукты. Насколько сильно список отличается от полученного в предыдущем задании? 

# In[26]:


### ╰( ͡° ͜ʖ ͡° )つ▬▬ι═══════  bzzzzzzzzzz
# will the code be with you

# your code here


# Иногда в чеках пытаются искать __продукты-якоря.__ То есть продукты, которые являются основными. Например: айфон - основной продукт, наушники и чехол - дополнения к нему. Подумайте как можно попытаться найти такие продукты на основе простых метрик, основанных на подсчёте условных вероятностей.

# <center>
# <img src="https://pp.userapi.com/c638028/v638028181/52e5e/1X-dkzNN1hk.jpg" width="400"> 
# </center>

#  
