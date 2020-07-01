import random
def task_2(lst):
    print(lst)
    return min(lst)
a = (task_2(lst = [random.randint(0, 30) for i in range(10)]))
print("Минимальное число в списке: ", a)