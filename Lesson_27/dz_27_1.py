
a = [x * 2 for x in range(2, 20)]
print(a)

b = map(lambda x: x * 2, range(2, 20))
print(list(b))

def foo():
	for i in range(2, 20):
		yield i * 2

print(list(foo()))

for i in foo():
	print(i)
