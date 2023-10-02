#line = ""
#for i in range(5):
 #       line += "*"
#print(line)

#tex = "В мягкой КомНоте ЖИл ЗЛОЙ кот"
# print (len(tex)) # погазывает сколько символов в тексте или еще гдето 
#print ("кот" in tex) # показывает есть ли в тексте эти слова 
#print (tex.replace("кот","собака")) # заменяяет выбронные символы на новые

#list_1 = [3, 2, 3, 4, 3]
#k = 3   list_1.append
#j = 0

#for i in list_1 :
   # if i == 3:
  #      j =j+1
#print (j)

#lis_1 =[1,5,9]
#lis_1.append(8) #добовляет в конц списка новый элеммент
#print(lis_1)


#lis_2 = []

#for i in range(5):
#    lis_2.append(i)
#print(lis_2)

#lis_3 = [3,6,8,9]
#lis_3.pop(0)
#print(lis_3)

#Срез списка
#Помните в конце первой лекции Вы прошли срезы строк? Также существует срез
#списка, давайте научимся изменять наш список
#● Отрицательное число в индексе — счёт с конца списка
#list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#print(list_1[0]) # 1
#print(list_1[1]) # 2
#print(list_1[len(list_1)-1]) # 10
#print(list_1[-5]) # 6
#print(list_1[:]) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#print(list_1[:2]) # [1, 2]
#print(list_1[len(list_1)-2:]) #[9, 10]
#print(list_1[2:9]) # [3, 4, 5, 6, 7, 8, 9]
#print(list_1[6:-18]) # []
#print(list_1[0:len(list_1):6]) # [1, 7]
#print(list_1[::6]) # [1, 7]

"""
Кортежи
💡 Кортеж — это неизменяемый список.
Тогда для чего нужны кортежи, если их нельзя изменить? В случае защиты
каких-либо данных от изменений (намеренных или случайных). Кортеж занимает
меньше места в памяти и работают быстрее, по сравнению со списками
t = () # создание пустого кортежа
print(type(t)) # class <'tuple'>
t = (1,)
print(type(t))
t = (1)
print(type(t))
t = (28, 9, 1990)
print(type(t))
colors = ['red', 'green', 'blue']
print(colors) # ['red', 'green', 'blue']
t = tuple(colors)
print(t) # ('red', 'green', 'blue')
t = tuple(['red', 'green', 'blue'])
print(t[0]) # red
print(t[2]) # blue
for e in t:
print(e) # red green blue
t[0] = 'black' # TypeError: 'tuple' object does not support(нельзя изменять
кортеж

"""


# list_1 =[1, 1, 2, 0, -1, 3, 4, 4]




"""
list = [1, 2, 3, 8, 6]
print(list)
x = int(input("Введите искомое число "))
index_element = 0
min_element = abs(x - list[0])
for i in range(1, len(list)):
    buffer_element = abs(x -list[i])
    if buffer_element < min_element:
        min_element = buffer_element
        index_element = i

print(f"Самый близкий по величине элемент к заданному числу {list[index_element]}")

"""

"""
a = [1, 2, 3, 4, 5]
k = 3

lis = a[-k:] + a[:-k]
print (lis)

"""
"""

slov = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},{"VI": "S005"}, {"VII": "S005"}, {" V ":" S009 "}, {" VIII ":" S007 "}] 
slov2 = []

for  i in slov:
    for (j,l) in i.items():
      slov2.append(l)

slov3 = slov2
slov3 = set(slov3)
print(slov3)
"""


"""
list_1 = [1, 2, 3, 4, 5,6,7,10]


k = 9
m = abs(k - list_1[0]) 

number = list_1[0]
for i in range(1, len(list_1)):
    if m >= abs(list_1[i] - k):
        m = abs(list_1[i] - k)
        number = list_1[i]
print(f' Ближайшее число к элементу {k} - {number}')
"""
"""
k = 'ноутбук'
slov = k.upper()

num = 0

lis_1 = {1:"AEIOULNSTRАВЕИНОРСТ" , 2:"DGДКЛМПУ" , 3:"BCM, P, Б, Г, Ё, Ь, Я" , 4:"F, H, V, W, Y,Й, Ы " , 5:"K,Ж, З, Х, Ц, Ч", 8:"J, X, Ш, Э, Ю", 10:"Q, Z,Ф, Щ, Ъ"}
for i in slov:
    for g,j in lis_1.items():
          if i in j :
              num = num + g
print(num)


 a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

"""

"""
new = "a a a b c a a d c d d"
new = new.split()
dict_1 = {}
print(new)
for leteer in new:
    if leteer in dict_1:
        dict_1[leteer] = dict_1[leteer] + 1
        print(leteer + "_" +  str(dict_1[leteer]),end = " ")
    else : 
        dict_1[leteer] = 0
        print(leteer , end=" ")
  
  
  
  Пользователь вводит текст(строка). Словом считается 
последовательность непробельных символов идущих 
подряд, слова разделены одним или большим числом 
пробелов. Определите, сколько различных слов 
содержится в этом тексте.
Input: She sells sea shells on the sea shore The shells
that she sells are sea shells I'm sure.So if she sells sea
shells on the sea shore I'm sure that the shells are sea
shore shells
Output: 13

"""
"""
stroc = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
stroc = stroc.lower()
stroc = stroc.split()
stroc = set(stroc)
print(len(stroc))

"""
"""
n = 1
max_number = 0

while n != 0:
    n = int(input("Ведите цифру "))
    if max_number < n:
        max_number = n
print(max_number)

"""
"""
num1 =int(input("Ведите количество элементов 1 "))

def ylim  (a):
    mnoj = set()
    b = 0
    for i in range(a):
        b = int(input("Ведите цифру"))
        mnoj.add(b)
    return mnoj


nat = ylim(num1)
             
num2 =int(input("Ведите количество элементов 2 "))

nat2 = ylim(num2)

scrat = set()
scrat = nat.intersection(nat2)
print(scrat)


Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
"""
"""
a = 3
b = 5

def f (g,h):
    if h == 0:
        return 1
    return a * f(g, h - 1)
print(f(a,b))
Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
"""
"""
def sum(a,b):
   if b == 0:
       return a
   return  sum(a + 1,b - 1)
print (sum(5,3))
"""
"""
pervy = int(input("Ведите количество элементов "))

def otb (a):
    b = set()
    d = 0
    for i in range(a):
        d = int(input("ведите элемент "))
        b.add(d)
    return b

otb1 = otb(pervy)
print(otb1)
pervy2 = int(input("Ведите количество элементов "))
otb2 = otb(pervy2)
print(otb2)

otvet = otb1.difference(otb2)
print(otvet)

from random import lan
"""
"""
'''Задача 30: Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество
элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: a
n = a1 + (n-1) * d.
Каждое число вводится с новой строки.
Ввод: 7 2 5
Вывод: 7 9 11 13 15'''

per = int (input("Ведите первый элемент "))
raz = int (input("Ведите разность "))
n = int (input("Ведите количество элементов "))
for i in range(n):
    print(per + i * raz, end=" ")
    
'''Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше заданного максимума)
Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
Вывод: [1, 9, 13, 14, 19]'''


spisk1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
spisk2 = []
min = 5
max = 9
for i in range(len(spisk1)):
    if min <= spisk1[i] <= max:
      spisk2.append(i)
print(spisk2)
"""
"""

num1 =int(input("Ведите количество элементов  "))

def ylim  (a):
    mnoj = []
    b = 0
    for i in range(a):
        b = int(input("Ведите цифру"))
        mnoj.append(b)
    return mnoj


nat = ylim(num1)

print(nat)

count = 0

for i in range(len(nat)):
    for g in range(nat[i - 1]):
        print(nat[g],end=" ")
"""
"""
transformation = lambda x : x + x
values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
transormed_values = list(map(transformation, values))
if values == transormed_values:
    print("ok")
else:
   print(transormed_values)
""" 
def username ():
   return input("Ведите имя ").title()

def tow_name ():
   return input("Ведите фамилию ").title()

def three_name ():
   return input("Ведите отчество ").title()

def tel ():
   return input("Веддите телефон ").title()

def dat ():
    name = username()
    surname =  tow_name()
    tree_name = three_name()
    telefon = tel()
    with open ('contacts.txt','a',encoding = 'utf-8') as fail:
        fail.write(f'{name} {surname}\n{tree_name}\n{telefon}\n\n')
        
def prin_contact():
    with open('contacts.txt','r') as dart:
     asur = dart.read()
     print(asur)
    menu()
    playmenu()

def poisc ():
    serch = input("Ведите имя ").title()
    with open('contacts.txt','r',encoding = 'utf-8') as dart:
        ime = dart.read().split("\n\n")
        for i in ime:
            if serch in i:
                print("")
                print (i)
                print("")
    menu()
    playmenu()
        
def delit ():
    print("Выбирите индекс контакта который хотите удалить")
    with open('contacts.txt','r',encoding = 'utf-8') as dart:
         dart.seek(0)
         ime = dart.read().split("\n\n")
         alert= list(enumerate(ime,1))
         for i in alert:
             for j in i:
                 print(j)
         delit = int(input("Ведите индекс контакта который надо удалить ")) - 1
         alert.pop(delit)
         for v in alert:
             for x in v:
                 print(x)
    menu()
    playmenu()
    


def menu(): 
    print("  Menu  ")
    print("_____________________________")
    print(" (1) -- Показать контакты ")
    print(" (2) -- Добавить контакт")
    print(" (3) -- Найти контакт")
    print(" (4) -- Удалить контакт")
    print(" (5) --  Exit")
    print("_____________________________")

menu()
def playmenu():
 play = int(input(""))
 if play == 1:
    prin_contact()
 elif play == 2:
    dat()
 elif play == 3:
     poisc()
 elif play == 4:
     delit()
playmenu()