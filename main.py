from tokenizer import Tokenizer
from parsers import Parser

sentence = ' '
tokenizer = Tokenizer()
parser = Parser()
accept_nb = reject_nb = 0
while True :
	sentence = input()
	if len(sentence) > 0 :
		parser.set_parser()
		tokenizer.set_tokenizer(sentence)
		while not tokenizer.is_end() :
			result = tokenizer.next()
			# print(result)
			if not parser.parsing(result['status']) :
				break
		if parser.is_accept() :
			# print('accept')
			accept_nb += 1
		else :
			# print('reject')
			reject_nb += 1
		print('accept: %d, reject: %d' %(accept_nb, reject_nb))