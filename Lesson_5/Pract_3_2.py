def exer_1(a, b):
    summ = 0
    for x in range(a, b+1):
        summ += x
    aver = summ/((b+1)-a)
    return(("Сумма = "+str(summ))+"\n"+"Среднее арифметическое = "+str(aver))

def exer_2(n):
    fact = 1
    for el in range(n):
        fact = fact * (el+1)
    return("Факториал числа " + str(n)+ " равен " + str(fact))

choise = int(input("""Какое задание вы хотите выполнить?
1
2
3
4
"""))
if choise == 1:
    print(exer_1(a = int(input("Ввелите первое число ")), b = int(input("Введите второе число "))))
elif choise == 2:
    print(exer_2(n = int(input("Введите число "))))
elif choise == 3 or choise == 4:
    print((input("Введите желаемый символ "))*(int(input("Введите длину линии "))))
else:
    print("Вы сделали неправльный выбор. Повторите ввод данных")
print(input("Нажмите клавишу Enter для завершения программы"))