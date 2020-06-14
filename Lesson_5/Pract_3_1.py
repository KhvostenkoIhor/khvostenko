a = int(input("Введите первое число "))
b = int(input("Введите второе число "))
if a > b:
    a, b = b, a
else:
    pass

def vse_chisla(a, b):
    for x in range(a, b):
        print(x)
    return("Выведены все числа в диапазоне от "+ str(a)+" до "+str(b))

def nechetnye_chisla(a, b):
    for x in range(a, b):
        if x % 2 > 0:
            print(x)
    return("Выведены нечётные числа в диапазоне от "+ str(a)+" до "+str(b))

def chetnye_chisla(a, b):
    for x in range(a, b):
        if x % 2 == 0:
            print(x)
    return("Выведены чётные числа в диапазоне от "+ str(a)+" до "+str(b))
    
def obratnyy_poryadok(a, b):
    numbers = []
    for el in range(a, b):
        numbers.append(el)
    numbers.reverse()
    for x in numbers:
        print(x)      
    return("Выведены числа в диапазоне от "+ str(a)+" до "+str(b) + " в обратном порядке")

choise = int(input("""Что вы хотите отобразить на экране?
1 - Для решения задания 1
2 - Для решения задания 2
3 - Для решения задания 3
4 - Для решения задания 4
"""))
if choise == 1:
    print(vse_chisla(a, b))
elif choise == 2:
    print(nechetnye_chisla(a, b))
elif choise == 3:
    print(chetnye_chisla(a, b))
elif choise == 4:
    print(obratnyy_poryadok(a, b))
else:
    print("Вы сделали неправильный выбор. Повторите ввод данных")
print(input("Нажмите клавишу Enter для завершения программы"))