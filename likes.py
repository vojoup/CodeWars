def likes(names):
#     likes ["Max", "John", "Mark"] // must be "Max, John and Mark like this"
# 	  likes ["Alex", "Jacob", "Mark", "Max"] // must be "Alex, Jacob and 2 others like this"
	d = len(names)
	if d == 0:
		return 'no one likes this'
	elif d == 1:
		return('{} likes this').format(names[0])
	elif d == 2:
		return('{} and {} like this').format(names[0], names[1])
	elif d == 3:
		return('{}, {} and {} like this').format(names[0], names[1], names[2])
	# else:
		# print('{}, {} and').format(names[0], names[1]),


print(likes(['Peter', 'Anna', 'Blembulak', 'John']))