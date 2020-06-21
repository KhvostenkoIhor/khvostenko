print("""
Задание 2
Пользователь вводит с клавиатуры некоторый текст,
после чего пользователь вводит список зарезервированных
слов. Необходимо найти в тексте все зарезервированные
слова и изменить их регистр на верхний. Вывести на
экран измененный текст.
""")

fraza = input("Введите необходимый текст\n")
fraza = fraza.lower().split()

znaki = [".", ",", "!", "?"]
for i, slovo in enumerate(fraza):
    if slovo[-1] in znaki:
        fraza[i] = slovo[:-1]
        slovo = fraza[i]

rez = []
x = ""
while x != "0":
    x = input("Введите по очереди слова, которые хотите найти или 0 для завершения ввода\n")
    rez.append(x)

for i, el in enumerate(fraza):
    if el in rez:
        el = el.upper()
        fraza[i] = el

print(" ".join(fraza))