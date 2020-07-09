
def decor(func):   
    
    def add2(x):
        return (x + 2)
         
    def sqrt(x):       
        return x ** 2
        
    def price(x):
        n = int(input("Price: \n"))
        def disc():
            d = (n/100)*x
            return d       
        return (n - disc())
    
    def future(x):
        import datetime
        a = datetime.datetime.now()
        b = a.replace(year=a.year + 10)
        return b.strftime("%A %d:%m:%Y")
            
    mes = "What to do?\n"
    mes += "Enter:\n"
    mes += "1 if you want to add 2 to numb()\n"
    mes += "2 if you want to square numb()\n"
    mes += "3 if you want to know some price with numb() percent discount\n"
    mes += "4 if you want to know what will be the day numb() years later"
    answ = int(input(mes+"\n"))
    if answ == 1:
        return add2
    elif answ == 2:
        return sqrt
    elif answ == 3:
        return price
    else:
        return future

@decor
def numb(a):
    return a
print(numb(10))

