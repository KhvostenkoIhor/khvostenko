x = int(input("Pervoe chislo: "))
y = int(input("Vtoroe chislo: "))
z = int(input("Trete chislo: "))
choise = int(input("""Vvedite: 
1 dlya maksimal'nogo chisla ili 
2 dlya minimal'nogo chisla ili 
3 dlya rascheta srednego arifmeticheskogo:
"""))
if choise < 2:
    if x > y > z:
        print("Max=", x)
    elif x < y < z:
        print("Max=", z)
    else:
        print("Max=", y)
elif choise > 2:
    print("Average=", (x+y+z)/3)
else:
    if x > y > z:
        print("Min=", z)
    elif x < y < z:
        print("Min=", x)
    else:
        print("Min=", y)