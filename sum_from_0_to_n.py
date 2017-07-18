def sum(n):
	res = 0
	for i in range(n + 1):
		res += i
	return res

def show_sequence(n):
    if n == 0:
        return '0=0'
    elif n <= 0:
        return str(n) + '<0' 
    else:
    	res = [ str(x) for x in range(n + 1)]
    	return '+'.join(res) + ' = ' + str(sum(n))

print(show_sequence(6))
    