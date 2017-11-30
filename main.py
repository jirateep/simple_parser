from tokenizer import Tokenizer

sentence = ' '
tokenizer = Tokenizer()
while True :
	sentence = input()
	if len(sentence) > 0 :
		tokenizer.set_tokenizer(sentence)
		while not tokenizer.is_end() :
			result = tokenizer.next()
			print(result)