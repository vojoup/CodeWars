def remove_smallest(numbers):
	if len(numbers) == 0:
		return []
	res = numbers
	minimum = min(numbers)
	for i in numbers:
		if i == minimum:
			numbers.remove(i)
			break
	return res

print(remove_smallest([1, 2, 3, 1, 1]))