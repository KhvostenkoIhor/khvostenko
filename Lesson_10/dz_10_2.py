import random
def task_2(lst):
    """Выводит минимально число в списке"""
    print(lst)
    return min(lst)
a = (task_2(lst = [random.randint(0, 50) for i in range(10)]))
print("Минимальное число в списке: ", a)
