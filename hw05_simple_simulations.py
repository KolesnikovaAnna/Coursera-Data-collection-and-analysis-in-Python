#!/usr/bin/env python
# coding: utf-8

# <center>
# <img src="logo.png" height="900"> 
# </center>
# 
# 
# #  Простые симуляции
# 
# В этом задании мы решим несколько простых задачек на симуляции. 

# In[1]:


import numpy as np
import scipy.stats as sts
import matplotlib.pyplot as plt


# ## Упражнение 1 (распределение Пуассона)
# 
# Случайная величина $X$ имеет распределение Пуассона с $\lambda = 2$,  $X \sim Pois(2)$. С помощью $10^6$ симуляций оцените: 
# 
# * $P(X > 6)$
# * $P(X > 6 \mid X > 5)$
# * $P(X > 5, X < 7)$
# * $E(X^3)$ 
# * $E(X \mid X > 5)$
# 
# __Под чёрточками имеется в виду условная вероятность!!!__
# 
# Вбейте получившиеся ответы в переменные `ans1`, `ans2`, $\ldots$, `ans5`. 

# In[14]:


### ╰( ͡° ͜ʖ ͡° )つ▬▬ι═══════  bzzzzzzzzzz
# will the code be with you

n_obs = 10**6

poisson_rv = sts.poisson(2)
x_1 = poisson_rv.rvs(n_obs)
x_2 = poisson_rv.rvs(n_obs)
x_3 = poisson_rv.rvs(n_obs)
x_4 = poisson_rv.rvs(n_obs)
x_5 = poisson_rv.rvs(n_obs)



ans1 = np.sum(x_1 > 6)/n_obs
print(ans1)


uslovie = x_2 > 5
ans2 = np.sum(x_2[uslovie] > 6)/np.sum(uslovie)
print(ans2)


uslovie = x_3 < 7
ans3 = np.sum(x_3[uslovie] > 5)/n_obs
print(ans3)


ans4 = np.mean(x_4**3)
print(ans4)


uslovie = x_5 > 5
ans5 = np.mean(x_5[uslovie])
print(ans5)


# your code here


# In[15]:


# проверка, что задание решено корректно
assert np.abs(ans3 - 0.01) < 1e-2

# Похожие тесты скрыты от вас


# ## Упражнение 2 (нейросети)
# 
# Юра завёл себе две нейронные сетки и два сервера для их обучения. Две нейросети обучаются независимо на двух серверах. Время их обучения $T_1$ и $T_2$ равномерно распределено на отрезке $[1;3]$ (обучение измеряется в часах). В процессе обучения сервер может упасть. Момент падения сервера $T$ распределён экспоненциально с параметром $\lambda = 0.3$. Он не зависит от времени обучения нейросеток. 
# 
# Известно, что одна из нейросетей успела обучиться, а вторая не успела. Какова вероятность того, что $T \le 1.5$? Ответ вбейте в переменную `ans6`. При симуляциях для генерации момента подения используйте для обоих серверов одну и ту же случайную величину. 
# 
# **Hint:** при решении задачи помните о том, что у вас две нейросетки!

# In[25]:


### ╰( ͡° ͜ʖ ͡° )つ▬▬ι═══════  bzzzzzzzzzz
# will the code be with you

uniform_rv = sts.uniform(1, 3)
exp_rv = sts.expon(0.3)

t1 = uniform_rv.rvs(n_obs)
t2 = uniform_rv.rvs(n_obs)
T = exp_rv.rvs(n_obs)

uslovie = (t1 > 3) & (t1 > t2)

ans6 = np.sum(T[uslovie] <= 1.5)/np.sum(n_obs)




ans6 

# your code here


# In[26]:


# проверка, что задание решено корректно
assert ans6 < 0.2
assert ans6 > 0.1

# Похожие тесты скрыты от вас


# ## Упражнение 3 (квантильное преобразование)
# 
# Случайная величина $X$ описывается функцией распределения: 
# 
# $$
# F(x) = \left( \frac{\ln x}{\ln \theta} \right)^{\alpha},  \quad x \in [1; \theta]
# $$
# 
# Сгенерируйте из такого распределения выборку объёма $10^6$ и оцените математическое ожидание данной случайной величины. Запишите его в переменную `ans7`. В качестве параметров возьмите $\alpha=2, \theta = 10$.

# In[55]:


### ╰( ͡° ͜ʖ ͡° )つ▬▬ι═══════  bzzzzzzzzzz
# will the code be with you

theta = 10
alpha = 2

n_obs = 10**6

y = sts.uniform(1, 10)
y = y.rvs(n_obs)

x = np.exp((y**(1/alpha))*np.log(theta))

ans7 = y.mean()
print(ans7)
# your code here


# Нарисуйте для получившегося распределения гистограмму. Найдите в аналитическом виде плотность распределения. Нанесите её на картинку с гистограммой. 

# In[ ]:


### ╰( ͡° ͜ʖ ͡° )つ▬▬ι═══════  bzzzzzzzzzz
# will the code be with you

# your code here


# In[56]:


# проверка, что задание решено корректно
assert ans7 < 6
assert ans7 > 2

# Похожие тесты скрыты от вас


# ## Упражнение 4 (сходимость по вероятности)
# 
# __Это задание никак не оценивается.__ У распределения хи-квадрат есть следующее свойство: если $X_1, \ldots, X_n \sim iid~N(0,1)$, тогда имеет место следующая сходимость по веротяности:
# 
# $$
# \frac{\chi^2_n}{n} = \frac{X_1^2 + \ldots + X_n^2}{n} \to  1
# $$
# 
# Продемонстрируйте с помощью симуляций, что это именно так. От вас требуется построить ту же картинку, что мы строили при иллюстрации ЗБЧ в лекции. Не забудьте построить для нескольких разных $\varepsilon$ коридоры и убедиться, что последовательность с некоторого момента начинает пробивать их довольно редко.

# In[ ]:


### ╰( ͡° ͜ʖ ͡° )つ▬▬ι═══════  bzzzzzzzzzz
# will the code be with you


#  
