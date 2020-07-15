from random import randint
def task_3(n):
    t_ind = []
    t_elem = []
    t1 = tuple([randint(0, 3) for i in range(n)])
    t2 = tuple([randint(0, 3) for i in range(n)])
    t3 = tuple([randint(0, 3) for i in range(n)])
    print("Initial tuples", t1, t2, t3, sep="\n")
    for a, b in enumerate(t1):
        for i, j in enumerate(t2):
            for y, z in enumerate(t3):
                if a == i == y and b == j == z:
                    t_ind.append(a)
                    t_elem.append(b)
    print("Index of common elements", t_ind, "Common elements", t_elem, sep="\n")       

n = int(input("Enter the length of the initial tuples\n"))
task_3(n)