import random
def task_6(lst, n):
    rez = [i**n for i in lst]
    return rez
lst = [(random.randint(1, 6)) for i in range(5)]
n = int(input("Введите степень\n"))
print(lst, task_6(lst, n), sep="\n")

