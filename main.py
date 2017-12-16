from tokenizer import Tokenizer
from parsers import Parser

sentence = ' '
tokenizer = Tokenizer()
parser = Parser()
while True :
	sentence = input()
	if len(sentence) > 0 :
		check = True
		parser.set_parser()
		tokenizer.set_tokenizer(sentence)
		while not tokenizer.is_end() :
			result = tokenizer.next()
			# print(result)
			check = parser.parsing(result['status'])
			if not check :
				print('wrong syntax')
		if check :
			if parser.is_accept() :
				print('correct')
			else :
				print('wrong')