#two = lambda : 2
#print(two())

#def sqrt(x: int):
#    return x**2
#a = sqrt(4)
#print(a)

#b = lambda x: x ** 2
#print(b(4))

#def foo(x):      =====
#   return x **2  ===== lambda x: x ** 2

#lst  = [1, 2, 3, 4, 5]
#lst2 = []

#lst2 = map(lambda x: x**2, lst)
#print(lst)
#print(lst2)

#for i in lst2:
#    print(i)

#print(list(lst2))
#print(list(lst2))
#print(list(lst2))
#for i in lst:
#    print(i, end="\n")
#for i in lst:
#    print(i, end="\n")
#for i in lst:
#    print(i, end="\n")

#def helper(x):
#    return x ** 2

#print(lst)
#lst2 = map(helper, lst)
#print(list(lst2))
#print(list(lst2))

#ФУНКИЯ - ФИЛЬТР
#a = [1, 2, 3, 4, 5, 6, True, False, "Hello", "Python"]
#b = filter(lambda x : x % 2 == 0, a) 
#print(list(b))
#def foo(x):
#    if type(x) == int:
#        if x < 3 or x == 6:
#            return True
#    if type(x) == bool:
#        if not x:
#            return True
#    if type(x) == str:
#        if "n" in x:
#            return True
#    else:
#        return False
#b = filter(foo, a)
#print(list(b))

#ЗАМЫКАНИЕ

#Сохраняет значение даже того контекста,
#которого уже не существует

#if __name__ == "__main__":
#    print("Hello")

#def outer(par):
#    loc = par
#    def inner():
#        return loc
#    return inner()
#var = 1
#a = outer(var)
#print(a)

#def make_closure(some):
#    #pass
#    loc = some
#    def power(x):
#        return x ** some
#    return power#(2)
#cube = make_closure(3)
#print(cube(2))


# f(x) = x ** 2
# y = x ** 2

def parabola(x):
    return x ** 2

def get_point(y, x):
    return y(x)

if __name__ == "__main__":
    x1 = get_point(parabola, 2)
    print(x1)
