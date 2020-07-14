lst = [9, 3, 7, 4, 6, 9, 3, 13, 5, 0]
a = {}

for i in range(len(lst)):
    a[i] = []

for i in range(len(a)):
    a[i] = [lst[i]]
    for j in range(i+1, (len(lst)-1)):
        if lst[j] >= a[i][0]:
            a[i].append(lst[j])

for i in range(len(a)):
    print(a[i])
    for j in range(1, (len(a[i]))):
        #print(a[i][j])
        if a[i][j-1] > a[i][j]:
            a[i].remove(a[i][j-1])


