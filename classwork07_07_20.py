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

#def make_code_better(foo):
#    def wrapper():
#        print("wrapper is started")
#        foo()
#        print("wrapper is ended")
 #       #print("hello world")      
#    return wrapper 
#@make_code_better
#def foo():
 #   print("My code is executing")

#foo()
# def connection(ip: str, port: int):
#     def make_connection(printer_funk):
#         print("*" * 10)
#         print("Connect to IP: ", ip)
#         print("Connect to port: ", port)
#         def wrapper(model: str, color: str):
#             print("*" * 10)
#             print(model, "Connection")
#             printer_func(model = model, color = color)
#             print("*" * 10)
#         return wrapper
#     return make_connection

# @connection(ip = "192.168.10.2", port = 5433)
# def hp_printer(model: str, color: str):
#    print("Model:", model)
#    print("Color: ", color)
   
#    print("HP Printer Connection")

# if __name__ == "__main__":
#     # ! printer_models = ["hp", "samsung", "xiaomi"]
#     hp = hp_printer
#     hp(model = "HP", color="red")

def bench(iters):
    def decorator(func):
        import time

        def wrapper(*args, **kwargs):
            total = 0
            for i in range(iters):
                start_time = time.time()
                return_value = func(*args, **kwargs)
                end_time = time.time()
                total = total + (end_time - start_time)

            print("The avarage of exec: ", total/iters)
            return(return_value)
        return wrapper
    return decorator

@bench(iters = 10)
def fetch_webpage(url):
    import requests
    #a = "URL: " + url
    webpage = requests.get(url)
    return webpage.text

webpage = fetch_webpage("https://google.com")
print(webpage)



#___Алгоритмы сортировки