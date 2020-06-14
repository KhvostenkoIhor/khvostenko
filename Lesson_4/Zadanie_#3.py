metr = float(input("Vvedite kolichestvo metrov:\n"))
choise = input("""Vvedite
mm dlya perevoda v milimetry
cm dlya perevoda v santimetry
km dlya perevoda v kilometry
""")
if choise == "mm":
    mm = metr * 1000
    print(metr, "metrov =", mm, "milimetrov")
elif choise == "cm":
    cm = metr * 100
    print(metr, "metrov =", cm, "santimetrov")
elif choise == "km":
    km = metr / 1000
    print(metr, "metrov =", km, "kilometrov")