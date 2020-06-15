





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
lis = ""
grade = int(input("Введите начало диапазона "))
grade_2 = int(input("Введите конец диапазона "))
numb = int(input("Введите число, которое хотите выделить "))
if grade > grade_2:
    grade, grade_2 = grade_2, grade
else:
    pass
while grade > numb or numb > grade_2 :
    numb = int(input("Вы ввели неверное число. Повторите ввод "))
for el in range(grade, grade_2+1):
    if el != numb:
        lis += (str(el) + " ")
    elif el == numb:
        el1 = ("!"+str(el)+"!")
        lis = (lis + el1 + " ")
    el+=1
print(lis)    








