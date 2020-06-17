def exer_3(x, y):
    for i in range(x, y+1):
        if i % 3 == 0 and i % 5 == 0:
            print("Fizz Buzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 3 != 0 and i % 5 != 0:
            print(i)

def exer_2(x, y):
    lis = []
    kr_7 = []
    kr_5 = []
    for i in range(x, y+1):
        lis.append(i)
        if i % 7 == 0:
            kr_7.append(i)
        if i % 5 == 0:
            kr_5.append(i)
    pervoe = "Все числа интервала: "
    vtoroe = "В обратном порядке: "
    trete = "Числа, кратные 7: "
    chetvertoe = "Количество чисел, кратных 5: "
    print(pervoe, lis, sep="\n")
    print(vtoroe, lis[::-1], sep="\n")
    print(trete, kr_7, sep="\n")
    print(chetvertoe, len(kr_5), sep="\n")

def exer_1(x, y):
    for i in range(x, y+1):
        if i % 7 == 0:
            print(i)

choice = int(input("""Какое задание вы хотите выполнить?
1 для Задания #1
2 для Задания #2
3 для задания #3
"""))

while choice < 1 or choice > 3:
    choice = int(input("""Вы сделали неправильный выбор. Повторите ввод 
Какое задание вы хотите выполнить?
1 для Задания #1
2 для Задания #2
3 для задания #3
"""))

x = int(input("""Введите начало интервала
"""))
y = int(input("""Введите конец интервала
"""))

if choice == 1:
    exer_1(x, y)
elif choice == 2:
    exer_2(x, y)
elif choice == 3:
    exer_3(x, y)

print(input("Нажмите клавишу Enter для завершения программы"))