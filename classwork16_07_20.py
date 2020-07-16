#######МНОЖЕСТВА#######

# a = {"q": 3, 3: "3", 5: "set", "fg": [1, 3, 4], "klu=10": 12312}
# print(type(a))
# a = {"1", 1, "efewf", }
# print(type(a))

# months = set(["Jan", "Feb", "March", "Apr", "May", "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec"])
# for m in months:
#     print(m)

# set_1 = {'a', 4, 'text'}
# print(set_1)
# print(type(set_1))
# set_1 = {1, 2, 3, 4, 5, 6}
# print(set_1)
# print(type(set_1))
# set_1 = {}
# print(set_1)
# print(type(set_1))

# set_1 = set()
# print(type(set_1))

# set_1 = {3, 4, 7, 2, 8}
# set_2 = {7, 6, 3, 1, 12, 2}
# print(3 in set_1)
# print(4 in set_2)
# print(set_1, set_2, sep="\n")
# print(set_1 - set_2)
# print(set_2 - set_1)
# print(set_1 | set_2)
# print(set_1 & set_2)
# #print(set_1 set_2)
# # #x = int(input('Enter text \n'))
# # if x in set_1 or x in set_2:
# #     print('found')
# # else:print('not found')

# # if x in (set_1 | set_2):
# #     print('found')
# # else:
# #     print('not found')

# from random import randint
# lst_1 = [randint(1, 1000) for i in range(1000)]
# lst_2 = [randint(1, 1000) for i in range(1000)]
# A = set(lst_1)
# B = set(lst_2)
# print(A, B, sep="\n")
# if 472 in (set_1 | set_2):
#     print('found')
# else:
#     print('not found')

# from random import choice
# alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# # lst_1 = [choice(alph)*3 for i in range(100)]
# # lst_2 = [choice(alph)*3 for i in range(100)]
# # A = set(lst_1)
# # B = set(lst_2)
# #print(A, B, sep="\n")
# def get_random_string(length: int):
#     r = ""
#     for i in range(length):
#         r += choice(alph)
#     return r
# lst_1 = [get_random_string(length=len(alph)) for i in range(1000)]
# lst_2 = [get_random_string(length=len(alph)) for i in range(1000)]
# print(lst_1)

# A = set(lst_1)
# B = set(lst_2)
# text = 'asd'
# if text in (A & B):
#     print("Found")
# else:
#     print("Not found")
A = {1, 2, 3, 4, 5, 7, 8, 9}
B = {6, 7, 8}
C = {1, 2, 3, 1223}
D = C = {1, 2, 3}
# C = A | B # то же самое  C = A.union(B)
# C = A & B # то же самое С = A.intersection(B)
# C = A ^ B # то же самое C = symmetric_difference(B) уникальные элементы
# flag = A #< (>) B # чи є множина надмножиною над заданою
# flag = A > C #то же самое  C.issubset(A)  A.issuperset(C)
# print(flag)
# flag = A.isdisjoint(B)# наявність або відсутність спільніх елементів у множинах
# flag = A.difference(C)#повертає множину А - С
# flag = A.symmetric_difference(C)
# B |= D #то же самое  B.update(C)
# K = B.copy()
#print(K)
#A.intersection_update(C)# то же самое что A &= C
#A.difference_update(C)# то же самое что A -= C
A.add(19)
print(A)
A.remove(19)
print(A)
A.discard(22)
a = A.pop()
print(a)
print(A)
C = frozenset([1, 2, 3, 4, 5])
print(C)
print(type(C))

###ГЕНЕРАТОРЫ МНОЖЕСТВ####
from random import randint
a = {randint(1, 100) for i in range(10)}
print(a, type(a), sep='\n')
