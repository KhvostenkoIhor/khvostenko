print("Реалізувати Шифр Цезаря")

def encrypt(s, k):
    s_crypt = ""
    s = s.upper()
    letters = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    #Для шифровки текста латиницы можно добавить латинский алфавит
    # и еще одно условие для шифровки букв латиницей
    dlina = len(letters)
    for bukva in s:
        if bukva in letters:
            ind_bukvy = (letters.find(bukva) + k) % dlina
            bukva_2 = letters[ind_bukvy]
        else:
            bukva_2 = bukva
        s_crypt += bukva_2
    return s_crypt

s = input("Введите фразу, которую нужно зашифровать ")
k = int(input("Введите число - ключ шифрования"))
rez1 = encrypt(s, k)
rez2 = encrypt(rez1, -k)
print(rez1)
print(rez2)