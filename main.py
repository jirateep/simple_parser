from tokenizer import Tokenizer

sentence = ' '
tokenizer = Tokenizer()
while True :
	sentence = input()
	if len(sentence) > 0 :
		result = tokenizer.tokenizing(sentence)
		print(result)