s = input('Input string: ')

VOWELS = 'aeiou'
total_vowels = 0
for char in s:
    if char in VOWELS:
       total_vowels += 1

print('Number of vowels: ', total_vowels)