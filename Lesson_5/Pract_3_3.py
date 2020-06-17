





"""
Задание 1
Показать таблицу умножения для числа, введенного
пользователем. Например, если пользователь вводит
число 7, нужно показать:
7 * 1 = 7
7 * 2 = 14
7 * 3 = 21"""


chislo = int(input("Введите число, для которого хотите\nувидеть таблицу умножения"))
for el in range(11):
    rez = chislo * el
    print(chislo, "*", el, "=", rez )
    el += 1

"""
Задание 2
Написать программу – конвертер валют. Реализовать
общение с пользователем через меню."""

car_1 = input("""#Введите валюту, которую хотите обменять:
hrn - если хотите обменять украинскую гривну
dlr - если хотите обменять американский доллар
fun - если хотите обменять английский фунт
""")
val = float(input("Введите количество указанной валюты "))
car_2 = input("""#Введите валюту, которую хотите получить: 
hrn - если хотите получить украинскую гривну
dlr - если хотите получить американский доллар
fun - если хотите получить английский фунт
""")
if car_1 == "hrn":
    if car_2 == "hrn":
        exchange = val
        print("Вы получите ", exchange, car_2)
    elif car_2 == "dlr":
        exchange = val / 26.851
        print("Вы получите ", exchange, car_2)
    elif car_2 == "fun":
        exchange = val / 33.985
        print("Вы получите ", exchange, car_2)
elif car_1 == "dlr":
    if car_2 == "dlr":
        exchange = val
        print("Вы получите ", exchange, car_2)
    elif car_2 == "hrn":
        exchange = val * 26.575
        print("Вы получите ", exchange, car_2)
    elif car_2 == "fun":
        exchange = val * 0.787
        print("Вы получите ", exchange, car_2)
elif car_1 == "fun":
    if car_2 == "fun":
        exchange = val
        print("Вы получите ", exchange, car_2)
    elif car_2 == "hrn":
        exchange = val * 31.850
        print("Вы получите ", exchange, car_2)
    elif car_2 == "dlr":
        exchange = val * 1.271
        print("Вы получите ", exchange, car_2)


#Задание 3
#Пользователь вводит с клавиатуры две границы диапазона и число. Если число не попадает в диапазон,
#программа просит пользователя повторно ввести число,
#и так до тех пор, пока он не введет число правильно. Программа отображает все числа диапазона, выделяя число
#восклицательными знаками. Например:
#1 2 3 !4! 5 6 7.
#lis = ""
#grade = int(input("Введите начало диапазона "))
#grade_2 = int(input("Введите конец диапазона "))
#numb = int(input("Введите число, которое хотите выделить "))
#if grade > grade_2:
#    grade, grade_2 = grade_2, grade
#else:
#    pass
#while grade > numb or numb > grade_2 :
#    numb = int(input("Вы ввели неверное число. Повторите ввод "))
#for el in range(grade, grade_2+1):
#    if el != numb:
#        lis += (str(el) + " ")
#    elif el == numb:
#        el1 = ("!"+str(el)+"!")
#        lis = (lis + el1 + " ")
#    el+=1
#print(lis)


#Задание 4
#Написать игру «Угадай число». Программа загадывает
#число в диапазоне от 1 до 500. Пользователь пытается
#его угадать. После каждой попытки программа выдает
#подсказки, больше или меньше его число загаданного. 
#В конце программа выдает статистику: за сколько
#попыток угадано число, сколько времени это заняло.
#Предусмотреть выход по 0 в случае, если пользователю
#надоело угадывать число.

import random
numb = random.randint(1, 500)
yournumb = int(input("Введите число от 1 до 500"))
if yournumb == numb:
    print("Поздравляю, Вы выиграли, угадав число ", numb)
elif yournumb == 0:
    print("К сожалению, Вы проиграли, не угадав число ", numb)
else:
    while yournumb != numb or yournumb != 0:
        if yournumb == numb:
            print("Поздравляю, Вы выиграли, угадав число ", numb)
            break
        elif yournumb == 0:
            print("К сожалению, Вы не угадали число ", numb)
            break
        elif (yournumb - numb) >= 100:
            print("Вы сильно ошиблись. Ваше число более чем на 100 больше загаданного. Попробуйте еще раз")
            yournumb = int(input("Введите число от 1 до 500"))
        elif (yournumb - numb) >= 50:
            print("Вы ошиблись. Ваше число более чем на 50 больше загаданного. Попробуйте еще раз")
            yournumb = int(input("Введите число от 1 до 500"))
        elif (yournumb - numb) >= 10:
            print("Вы немного ошиблись. Ваше число более чем на 10 больше загаданного. Попробуйте еще раз")
            yournumb = int(input("Введите число от 1 до 500"))
        elif (yournumb - numb) >= 5:
            print("Вы уже близко. Ваше число более чем на 5 больше загаданного. Попробуйте еще раз")
            yournumb = int(input("Введите число от 1 до 500"))
        elif (yournumb - numb) >= 1:
            print("Совсем чуть-чуть. Ваше число более чем на 1 больше загаданного. Попробуйте еще раз")
            yournumb = int(input("Введите число от 1 до 500"))







