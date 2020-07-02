import random
def task_4():
    """Возвращает количество удалённых
    одинаковых элементов списка"""
    lst = [random.randint(0, 10) for i in range(10)]
    n = int(input("Введите число\n"))
    m = 0
    print(lst)
    for i in lst:
        if i == n:
            m += 1
            lst.remove(i)            
    print(lst)
    return m
print("Количество удалённых элементов =", task_4())
            