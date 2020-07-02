import random
def task_5(l1, l2):
    """Формирует третий список из двух заданных
    без повторяющихся элементов"""
    rez = []
    for i in l1:
        if i not in rez:
            rez.append(i)
    for j in l2:
        if j not in rez:
            rez.append(j)
    print(l1, l2, sep="\n")
    return rez
l1 = [random.randint(0, 10) for i in range(5)]
l2 = [random.randint(0, 10) for i in range(5)]
print(task_5(l1, l2))

