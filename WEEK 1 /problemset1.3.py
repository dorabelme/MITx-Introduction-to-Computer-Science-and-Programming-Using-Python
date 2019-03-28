s = input('Input string: ')

alphabet = 'abcdefghijklmnopqrstuvwxyz'

prevChar = ""
currentString = ""
longestString = ""

for char in s:
	if prevChar <= char:
		currentString += char
		if len(currentString) > len(longestString):
			longestString = currentString
	else:
		currentString = char
	prevChar = char

print('Longest substring in alphabetical order is:', longestString)
