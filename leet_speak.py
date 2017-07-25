def find_in_alpha(letter):
	alpha = {'A' : '@', 'B' : '8','C' : '(','D' : 'D','E' : '3','F' : 'F','G' : '6','H' : '#','I' : '!','J' : 'J','K' : 'K',
	'L' : '1','M' : 'M','N' : 'N','O' : '0','P' : 'P','Q' : 'Q','R': 'R','S' : '$','T' : '7','U' : 'U','V' : 'V',
	'W' : 'W','X' : 'X','Y' : 'Y','Z' : '2'
	}
	return alpha.get(letter, ' ')

def to_leet_speak(str):
	res = []
	for letter in str:
		res.append(find_in_alpha(letter))
	return ''.join(res)

print(to_leet_speak('AHOJ KLAJSD'))