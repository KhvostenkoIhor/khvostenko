metr = int(input("Vvedite kolichestvo metrov: "))
dm = str(metr * 10)
cm = str(metr * 100)
mm = str(metr * 1000)
mile = str(metr / 1609.34)
sea_mile = str(metr / 1852)
print(("dm="+dm), ("cm="+cm), ("mm="+mm), ("mile="+mile), ("sea_mile="+sea_mile), sep="\n")