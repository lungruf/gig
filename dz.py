
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
 elif play == 5:
    print("by")
playmenu()