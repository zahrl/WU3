def reflection(string):
	output = ''
	for i in range(len(string)-1, -1, -1):
		output += string[i]
	return output

assert(reflection('string') == 'gnirts')
assert(reflection('poem') == 'meop')