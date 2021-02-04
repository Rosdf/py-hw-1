#!/usr/bin/env python
# coding: utf-8

# In[3]:


#задание 1
phrase_1 = "dfsgsd"
phrase_2 = "fgedrfsdfg"
if phrase_1 > phrase_2:
    print("Фраза 1 длиннее фразы 2")
elif phrase_1 < phrase_2:
    print("Фраза 2 длиннее фразы 1")
else:
    print("Фразы равной длины")


# In[5]:


#задание 2
year = 2001
if year % 400:
    print("Високосный год")
elif year % 100:
    print("Обычный год")
elif year % 4:
    print("Високосный год")
else:
    print("Обычный год")


# In[24]:


#задание 3
month_arr = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь",]
print("Введите месяц:\n(строчными буквами)")
max_day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] #максимальное число дней в месяце
month = input()
if month not in month_arr:
    print("такого месяца нет")
else:
    print("введите день")
    day = int(input())
    if day < 1 or day > 31:
        print("такого дня нет")
    else:
        i = 0
        while month != month_arr[i]:
            i +=1
        i +=1
        if day > max_day[i]:
            print("такого дня нет")
        elif (i == 1 and day > 19) or (i == 2 and day < 19):
            print("Водолей")
        elif (i == 2 and day > 18) or (i == 3 and day < 21):
            print("Рыбы")
        elif (i == 3 and day > 20) or (i == 4 and day < 20):
            print("Овен")
        elif (i == 4 and day > 19) or (i == 5 and day < 21):
            print("Телец")
        elif (i == 5 and day > 20) or (i == 6 and day < 21):
            print("Близнецы")
        elif (i == 6 and day > 20) or (i == 7 and day < 23):
            print("Рак")
        elif (i == 7 and day > 22) or (i == 8 and day < 23):
            print("Лев")
        elif (i == 8 and day > 22) or (i == 9 and day < 21):
            print("Дева")
        elif (i == 9 and day > 20) or (i == 10 and day < 23):
            print("Скорпион")
        elif (i == 10 and day > 22) or (i == 11 and day < 22):
            print("Стрелец")
        else:
            print("Козерог")
            


# In[28]:


#задание 4
width = 16
length = 205
height = 5
if max(width, length, height) < 15:
    print("Коробка №1")
elif (width >= 15 and width < 50) or (length >= 15 and length < 50) or (height >= 15 and height < 50):
    print("Коробка №2")
elif length > 200:
    print("Упаковка для лыж")
else:
    print("Стандартная коробка №3")


# In[45]:


#Задание 5
number = 123456
n1 = 0
n2 = 0
i = 1
while i < 4:
    n1 += number % 10 #берем последнюю цифру числа
    number //= 10 #убираем последнюю цифру числа из числа
    i += 1
i = 1
while i < 4:
    n2 += number % 10
    i += 1
if n1 == n2:
    print("Счастливый билет")
else:
    print("Неасчастливый билет")


# In[55]:


#задание 6
print("Выберете фигуру:\nвведите 1 - круг, 2 - треугольник, 3 - прямоугольник")
shape = int(input())
if shape == 1:
    print("введите радиус:")
    r = float(input())
    if r < 0:
        print("некоректный радиус")
    else:
        print(3.1416 * (r ** 2))
elif shape == 2:
    print("введите первую сторону:")
    a1 = float(input())
    print("введите вторую сторону:")
    a2 = float(input())
    print("введите третью сторону:")
    a3 = float(input())
    if min(a1, a2, a3) < 0:
        print("некоректная длинна")
    else:
        if a1 >= a3 + a2 or a2 >= a1 + a3 or a3 >= a1 + a2:
            print("не выполнено неравенство треугольника")
        else:
            p = (a1 + a2 + a3) / 2 #полупериметр для формулы Герона
            print((p * (p - a1) * (p - a2) * (p - a3)) ** 0.5)
elif shape == 3:
    print("введите первую сторону:")
    a1 = float(input())
    print("введите вторую сторону:")
    a2 = float(input())
    if min(a1, a2) < 0:
        print("некоректная длинна")
    else:
        print(a1 * a2)
else:
    print("некоректный ввод")

