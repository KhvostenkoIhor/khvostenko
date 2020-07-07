print("Що таке lambda-функція?")

def foo1(x):
    a = (x * 2) ** 0.5  
    return ('%.2f' % a)
    
la1 = lambda x: (x * 2) ** 0.5

print(foo1(3))
print('%.2f' % la1(3))

def foo2(x):
    return x ** 2
    
la2 = lambda x: x ** 2

print(foo2(3))
print(la2(3))

def foo3(name):
    a = "Здравствуй, учитель " + name + "! Моё кунг-фу сильнее, чем твоё!"
    return a

la3 = lambda name: "Здравствуй, учитель " + name + "! Моё кунг-фу сильнее, чем твоё!"

print(foo3("Dmytro"))
print(la3("Dmytro"))