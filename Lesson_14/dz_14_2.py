from random import randint
def task_2(n):
    t_res = []
    t1 = tuple([randint(0, 10) for i in range(n)])
    t2 = tuple([randint(0, 10) for i in range(n)])
    t3 = tuple([randint(0, 10) for i in range(n)])
    print("Initial tuples", t1, t2, t3, sep="\n")
    for i in t1:
        if i not in t2 and i not in t3:
            if i not in t_res:
                t_res.append(i)
    for j in t2:
        if j not in t1 and j not in t3:
            if j not in t_res:
                t_res.append(j)
    for k in t3:
        if k not in t2 and k not in t1:
            if k not in t_res:
                t_res.append(k)
    return tuple(t_res)
n = int(input("Enter the length of the initial tuples\n"))
print("Tuple of unique elements\n", task_2(n))