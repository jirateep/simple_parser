from tokenizer import Tokenizer
from parsers import Parser

sentence = ' '
tokenizer = Tokenizer()
parser = Parser()
accept_nb = reject_nb = 0
check = True
while True :
	sentence = input()
	if len(sentence) > 0 :
		parser.set_parser()
		tokenizer.set_tokenizer(sentence)
		while not tokenizer.is_end() :
			token = tokenizer.next()
			# print(result)
			if token['status'] == 'ERROR' or not parser.parsing(token['status']) :
				break
		if tokenizer.is_end() and parser.is_accept() :
			# print('accept')
			accept_nb += 1
		else :
			# print('reject')
			reject_nb += 1
		print('accept: %d, reject: %d' %(accept_nb, reject_nb))