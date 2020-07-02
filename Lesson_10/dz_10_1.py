
import random
def task_1(lst):
    """Выводит произведение всех чисел в списке"""
    prod = 1
    print(lst)
    for i in lst:
        prod *= i
    return prod
a = (task_1(lst = [random.randint(0, 10) for i in range(5)]))
print("Произведение всех чисел списка равно\n", a)
