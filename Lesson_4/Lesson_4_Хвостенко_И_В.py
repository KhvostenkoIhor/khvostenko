print("""Завдання 1
Користувач вводить 3 числа. Далі в залежності від вибору користувача потрібно знайти суму або добуток цих чисел. 
(Тобто програма запитує в користувача, що потрібно зробити)""")

x = int(input("Pervoe chislo: "))
y = int(input("Vtoroe chislo: "))
z = int(input("Trete chislo: "))
choise = int(input("""Vvedite 
1 dlya rascheta summy ili 
2 dlya rascheta proizvedeniya:
"""))
if choise == 1:
    print("Summa =", (x+y+z), "\n"*2)
else:
    print("Proizvedenie =", (x*y*z), "\n"*2)


print("""Завдання 2
Користувач вводить 3 числа. Далі в залежності від вибору користувача потрібно знайти найбільше з 3-х, 
найменше, або середнє арифметичне. (Подібно до 1-го)""")

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
        print("Max=", x, "\n"*2)
    elif x < y < z:
        print("Max=", z, "\n"*2)
    else:
        print("Max=", y, "\n"*2)
elif choise > 2:
    print("Average=", ((x+y+z)/3), "\n"*2)
else:
    if x > y > z:
        print("Min=", z, "\n"*2)
    elif x < y < z:
        print("Min=", x, "\n"*2)
    else:
        print("Min=", y, "\n"*2)


print("""Завдання 3
Користувач вводить з клавіатури кількість метрів. В залежності від вибору - 
програма конвертує їх в сантиметри, міліметри, або кілометри.""")

metr = float(input("Vvedite kolichestvo metrov:\n"))
choise = input("""Vvedite
mm dlya perevoda v milimetry
cm dlya perevoda v santimetry
km dlya perevoda v kilometry
""")
if choise == "mm":
    mm = metr * 1000
    print(metr, "metrov =", mm, "milimetrov", "\n"*2)
elif choise == "cm":
    cm = metr * 100
    print(metr, "metrov =", cm, "santimetrov", "\n"*2)
elif choise == "km":
    km = metr / 1000
    print(metr, "metrov =", km, "kilometrov", "\n"*2)

print(input("Nazhmite klavishu Enter dlya zaversheniya programmy"))
