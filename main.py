from tokenizer import Tokenizer

sentence = ' '
tokenizer = Tokenizer()
while sentence != '' :
	sentence = input()
	result = tokenizer.tokenizing()
	print(result)