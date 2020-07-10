from time import time
from random import randint
lst = [randint(1, 1000) for n in range(1000)] #[4, 1, 6, 3, 2, 7, 8]
print(lst)
print("="*50, "\n"*2)

def decor(func):
	def wrapper(x):
		start = time()
		func(x)
		stop = time()
		print("Wrapper timer: ", stop - start)
		print(" "*50)
		print(x)
		print("="*50, "\n"*3)		
	return wrapper
	
@decor
def bubble(lst):
	start = time()
	flg = True
	while flg == True:
		flg = False
		for i in range(len(lst)-1):
			if lst[i] > lst[i+1]:
				flg = True
				lst[i], lst[i+1] = lst[i+1], lst[i]
			else:
				continue
	stop = time()
	print("Bubble Func timer: ", stop - start)
	return lst
bubble(lst)

@decor
def select(lst):
	start = time()
	for i in range(len(lst)):
		#print(i)
		min_elem_ind = i
		for j in range(i+1, len(lst)):
			#print(j)
			if lst[j] > lst[min_elem_ind]:
				continue
			else:
				min_elem_ind = j
		lst[i], lst[min_elem_ind] = lst[min_elem_ind], lst[i]
	stop = time()
	print("Select Func timer: ", stop - start)
	return lst
select(lst)

@decor
def inser(lst):
	start = time()
	for i in range(1, len(lst)):
		x = lst[i]
		if x > lst[i-1]:
			continue
		else:
			lst[i], lst[i-1] = lst[i-1], lst[i]
			x = lst[i]
	stop = time()
	print("Insert Func timer: ", stop - start)
	return lst
inser(lst)

# ! Почему-то я не смог прикрутить сюда декоратор
# ! Есть вероятность, что это из-за рекурсии в конце
start = time()
def fast(lst):	
	if len(lst) <= 1:
		return lst
	else:
		start = time()
		supp_elem = lst[int(len(lst)/2)]
		min_lst = []
		equal_lst = []
		max_lst = []
		for i in lst:
			if i > supp_elem:
				max_lst.append(i)
			elif i < supp_elem:
				min_lst.append(i)
			else:
				equal_lst.append(i)
		return fast(min_lst) + equal_lst + fast(max_lst)
stop = time()
print("Fast Func timer: ", stop - start)
print(fast(lst))

# ! С сортировкой кучей я так и не смог разобраться.
# ! Вообще не понимаю, что написано. Ни в алгоритме, ни в коде
# ! Надеюсь, она нам не сильно пригодится в будущем!












