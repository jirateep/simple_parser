from tokenizer import Tokenizer

def printing(result) :
	for tmp in result :
		print(tmp['status'] + '\t' + tmp['word'])
sentence = ' '
tokenizer = Tokenizer()
while True :
	sentence = input()
	if len(sentence) > 0 :
		tokenizer.set_tokenizer(sentence)
		result = tokenizer.tokenizing()
		printing(result)