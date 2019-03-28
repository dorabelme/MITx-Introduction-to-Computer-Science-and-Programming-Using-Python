s = input('Input string: ')

BOB = 'bob'
total_bobs = 0
for i in range(0,len(s)-2):
	start = i
	end = i + 2

	substring = s[start:end+1]

	print(substring)
	if substring == BOB:
		total_bobs += 1
		
print('Number of times bob occurs is: ', total_bobs)