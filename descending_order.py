def Descending_Order(num):
	num = reversed(sorted(str(num)))
	return int(''.join(num))

print(Descending_Order(12))