x = int(input("Pervoe chislo: "))
y = int(input("Vtoroe chislo: "))
z = int(input("Trete chislo: "))
choise = int(input("Vvedite 1 dlya rascheta summy ili 2 dlya rascheta proizvedeniya: "))
if choise == 1:
    print("Summa =", (x+y+z))
else:
    print("Proizvedenie =", (x*y*z))
