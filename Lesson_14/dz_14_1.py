from random import randint
def task_1(n):
    t_res = []
    t1 = tuple([randint(0, 6) for i in range(n)])
    t2 = tuple([randint(0, 6) for i in range(n)])
    t3 = tuple([randint(0, 6) for i in range(n)])
    print("Initial tuples", t1, t2, t3, sep="\n")
    for i in t1:
        if i in t2 and i in t3:
            if i not in t_res:
                t_res.append(i)
    return tuple(t_res)
n = int(input("Enter the length of the original tuples\n"))
print("Tuple of common elements\n", task_1(n))