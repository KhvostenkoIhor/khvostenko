###КОРТЕЖИ####
#a  = 1, 2, 3
#b = (1, 2, 3)
#print(type(a))
#print(type(b))
# l = []
# print(type(l))
# d = {}
# print(type(d))
# set = set()
# print(type(set))
# t = ()
# print(type(t))
# tt = 1, 
# print(type(tt))
# a = "10"
# b = "10"
# print(id(a))
# print(id(b))
#class tuple([iter])
# t = (2.3, "Hello", False)
# tt = 2.3, "qwe", (1, 2, 3, "asd"), False
# t3 = (1, 2, [1, 2, 3], False)
# print(t)
# print(tt)
# print(t3[2])
# for i in range(len(t3[2])):
#     #print(t3[2][i])
#     t3[2][i] *= 2
# #t3[2][1] = 15
# print(t3[2])
# a = (2,)
# a = (1, 2, 3)
# l = ["Hello", "Dima"]
# print(type(l))
# t = tuple(l)
# print(type(t))
# from random import randint
# a = tuple([randint(0, 10) for i in range(5)])
# print(a)
# #############################################
# lst = [randint(0, 10) for i in range(5)]
# a = tuple(lst)
# a = ('ab', 'abcd', 'cde', 'abc', 'def')
# b = input()
# for i in a:
#     if b == i:
#         print(True)
#     else:
#         continue
# print(len(a))
# ss = "Hello"
# # ss = tuple(ss)
# # print(ss)
# tt = ("Hello",)
# print(tt[0][3])
# tt = tuple(ss)
# print(tt[1:2])
# t1 = (1, 2, 3, 4,)
# t2 = (5, 6, 7, 8)
# # print(t1+t2)
# # t2 += t1
# # print(t2)
# for i in range(len(t2)):
#     print(i)
# s = 'def'
# tt = ('asfdsad', 'adsad', 12, 'def', [1, 2, 3])
# print(s in tt)
# if s in tt:
#     print('Its here')
# print(tt.index(12))
# print(tt.count('def'))
# t1 = 1, 2, 3, 4, 5
# print(min(t1), max(t1))
# t2 = 1, 2, 3, 4, 5

############РЕКУРСИЯ##############
#for room in ITStep:
#   if ball in room:
#       we will play
#    else:
#        we will go back

#def find(ball):
#    if ball:
#        return ball
#    else:
#        find(ball)
#####Числа Фибоначчи######
# a = 1
# b = 1
 
# n = 5
# i = 0
# while i < n - 2:
#     fib_sum = a + b
#     a = b
#     b = fib_sum
#     i = i + 1 
# print(b)  
def fact(n):
    fa = 1
    for i in range(1, n+1):
        fa *= i
    return (fa)
    
f5 = fact(5)
print(f5)
## РЕКУРСИЯ ##
def fac(n):
    if n == 1:
        return 1
    return n * fac(n-1)

f5 = fac(5)
print(f5)

def fac1(x, n=1):
    return n if x == 1 else fac1(x -1, n * x)
print(fac1(5))