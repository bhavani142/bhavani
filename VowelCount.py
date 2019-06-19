def vowelCount(str):
    #ADD YOUR CODE HERE
	vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
	count = 0
	for i in str:
		if i in vowel:
			count += 1
	return count





