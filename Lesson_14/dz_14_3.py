from random import randint
def task_3(n):
    t_ind = []
    t_elem = []
    t1 = tuple([randint(0, 3) for i in range(n)])
    t2 = tuple([randint(0, 3) for i in range(n)])
    t3 = tuple([randint(0, 3) for i in range(n)])
    print("Initial tuples", t1, t2, t3, sep="\n")
    for i in range(len(t1)):
        for j in range(len(t2)):
            for k in range(len(t3)):
                if t1[i] == t2[j] == t3[k] and i == j == k:
                    t_ind.append(i)
                    t_elem.append(t1[i])
    print("Index of common elements", t_ind, "Common elements", t_elem, sep="\n")        
n = int(input("Enter the length of the initial tuples\n"))
task_3(n)