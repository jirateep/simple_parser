from tokenizer import Tokenizer
from parsers import Parser

sentence = ' '
tokenizer = Tokenizer()
parser = Parser()
while True :
	sentence = input()
	if len(sentence) > 0 :
		parser.set_parser()
		tokenizer.set_tokenizer(sentence)
		while not tokenizer.is_end() :
			result = tokenizer.next()
			# print(result)
			parser.new_token(result['status'])
		check = parser.is_correct()