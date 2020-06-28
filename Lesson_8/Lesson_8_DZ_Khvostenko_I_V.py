import random
#задаем пустые списки для дальнейшей работы
lst_1 = []
lst_2 = []
lst_rezult = []

#задаем размер списков и границы для генератора чисел
n = int(input("Cколько значений вы хотите добавить в каждый список? "))
a = int(input("Введите начало диапазона для генератора чисел: "))
b = int(input("Введите конец диапазона для генератора чисел: "))

#создаём набор псевдо-случайных чисел и заполняем ими исходные списки
for i in range(n):
	i = random.randint(a, b)
	lst_1.append(i)

for j in range(n):
	j = random.randint(a, b)
	lst_2.append(j)

#формируем выбор задания для выполнения
answ = -1
while int(answ) < 0 or answ > 5:
	answ = int(input("""Выберите действие для продолжения или нажмите 0 для окончания ввода
1 Сформировать третий список, содержащий элементы обоих списков
2 Сформировать третий список, содержащий элементы обоих списков без повторений	
3 Сформировать третий список, содержащий элементы общие для двух списков	
4 Сформировать третий список, содержащий только уникальные элементы каждого из списков	
5 Сформировать третий список, содержащий только минимальное и максимальное значение каждого из списков	
	"""))
#Выполняем одно из действий в зависимости от выбора пользователя
	if answ == 0:
		break
	elif answ == 1:
		#складываем списки
		lst_rezult = lst_1 + lst_2
	elif answ == 2:
		#элементы без повторений
		lst_tmp = lst_1[:]
		for i in lst_2:
			if i not in lst_tmp:
				lst_tmp.append(i)
		for i in lst_tmp:
		    if i not in lst_rezult:
		        lst_rezult.append(i)
	elif answ == 3:
		#элементы, общие для двух списков
		for i in lst_2:
			if i in lst_1 and i not in lst_rezult:
				lst_rezult.append(i)	
	elif answ == 4:
		#уникальные элементы
		#lst_rezult = lst_1[:]
		for i in lst_1:
			if i not in lst_2 and i not in lst_rezult:
				lst_rezult.append(i)
		for i in lst_2:
		    if i not in lst_1 and i not in lst_rezult:
		        lst_rezult.append(i)
	elif answ == 5:
		#минимальные и максимальные значения
		mini_1 = min(lst_1)
		maxi_1 = max(lst_1)
		mini_2 = min(lst_2)
		maxi_2 = max(lst_2)
		lst_rezult.append(mini_1)
		lst_rezult.append(maxi_1)
		lst_rezult.append(mini_2)
		lst_rezult.append(maxi_2)

#вывод результата
if lst_rezult == []:
	print("Исходный список 1", lst_1, "Исходный список 2", lst_2, "Нет ни одного совпадения", sep="\n")
else:
	print("Исходный список 1", lst_1, "Исходный список 2", lst_2, "Конечный список", lst_rezult, sep="\n")


# Some comment
