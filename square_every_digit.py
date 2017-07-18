def square(n):
	return str(n * n)

def square_digits(num):
	result = []
	for n in str(num):
		result.append(square(int(n)))
	return int(''.join(result))

print(square_digits(9119))

# x = [str(1),str(2),str(3)]

# print ''.join(x)