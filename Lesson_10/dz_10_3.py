
n = int(input("Введите предел заданного списка\n"))
def task_3_1(lst):
	simp = []
	for numb in range(2, n):
		var = True
		for i in range(2, numb):
			if (numb % i == 0):
				var = False
		if var is True:
			simp.append(numb)
	return simp
print(task_3_1(lst = [i for i in range(2, n)]))
