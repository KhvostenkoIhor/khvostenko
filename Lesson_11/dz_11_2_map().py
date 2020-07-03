print("Що таке функція map() на прикладі")

#Функция map() принимает аргументами какую-то
#функцию и например список (итерируемый объект)
lst = [i for i in range(5)]

def foo1(x):
    a = (x * 2) ** 0.5   
    return ('%.2f' % a)

def foo2(x):
    if x % 2 == 0:
        return int((x / 2) ** 2)
    else:
        return x
        
names = ["Dmytro", "Ihor", "Olena", "Natalya", "John"]
def foo3(name):
    if name == "John":
        return(name + " Ты кто такой? Давай до свидания!")
    else:
        return ("Привет, " + name +"! Как дела?")
       
#Функция map() в качестве х (аргумента функции
#foo) подставляет каждый элемент из списка lst
f1 = list(map(foo1, lst))
#и возвращает результат выполнения функции foo
#для каждого х
print(f1)

f2 = list(map(foo2, lst))
print(f2)

f3 = list(map(foo3, names))
print("\n".join(f3))
