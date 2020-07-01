
n = int(input("Введите предел заданного списка\n"))
def task_3(lst):
    simp = []    
    for numb in lst:
        if numb == 2:
            simp.append(numb)
        for i in range(2, numb):
            if numb % i == 0:
                break
            else:
                simp.append(numb)
                break
    return simp
print(task_3(lst = [i for i in range(2, n)]))

#######################

def task_3(lst):
    for numb in range(2, n):
        var = True
        for i in range(2, numb):
            if (numb % i == 0):
                var = False
        if var is True:
            print(numb)
