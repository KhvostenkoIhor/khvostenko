#x = input("Vvedite 4-znachnoe chislo: ")
#print(int(x[0]) * int(x[1]) * int(x[2]) * int(x[3]))

value = int(input())
num = ""
num_1 = 1
while value:
    num+=str(value%10)
    num_1 = num_1 * (value%10)
    value = int(value/10)
print(num)
print(num_1)