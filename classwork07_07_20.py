#def hello_world():
#    print("Hello world")

#def dec_func(foo):
#    def wrapper():
#        print("Wrapper func!!!\n")
#        print("Wrapped func: {}\n".format(foo))
#        print("Doing wrapped func...\n")
#        foo()
#        print("Exit from wrapper")
#    return wrapper

#@dec_func
#def hello_world():
#    print("Hello world\n")

#hello_world()


##########ДЕКОРАТОРЫ#######

#import sys
#def get_ip_or_none(IP: str):
#    try:
#        octats = IP.split(".")
#                return None
#                continue
 #       return IP
#    except:
#        print("Error")
#a = "192.168.0.asd"
#print(get_ip_or_none(a))

#if __name__ == "__main__":
#    IP = sys.argv[1]
#    print(IP)
#    new_IP = get_ip_or_none(IP)
#    print(new_IP)




#print(sys.argv[1])
#print("Test")

#def foo(*args):
#    print(args[0])
#    print(args[1])
#    print(args[2])
#    print(args)
#    print(*args,"\n")

#def bar(lst):
#    print(*lst)
#    print(lst)

#foo(1, "Hello", 5, "python")

#ll = [1, 2, 3, "hello"]
#bar(ll)

#def foo2(key1, **kwargs):
#    print(key1, kwargs)

#dd = {
#    "key1" : 1,
#    "key2" : "Hello",
 #   "key3" : "3"
#}
#foo2(10, key2 = "Hel", key3 = "356+")

#ДЕКОРАТОРЫ



#def foo(a, b):
#    return (a + b)**2
#print(foo(2, 3))

def make_code_better(foo):
    def wrapper():
        print("wrapper is started")
        foo()
        print("wrapper is ended")
        #print("hello world")      
    return wrapper 
@make_code_better
def foo():
    print("My code is executing")

foo()




#___Алгоритмы сортировки