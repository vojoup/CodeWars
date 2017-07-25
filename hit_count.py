def counter_effect(hit_count):
	# [[0, 1], [0, 1, 2], [0, 1, 2, 3, 4, 5], [0]]
	num = str(hit_count)
	res = []
	tmp = []
	for n in num:
		cislo = range(int(n) + 1)
		tmp.append(cislo)
		res.append(tmp)
	return res[0]
print(counter_effect(1250))