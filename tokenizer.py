class Tokenizer :
	
	def set_tokenizer(self, sentence='') :
		self.sentence = sentence.rstrip()
		self.start_pos = 0
		self.stop_pos = 0
		self.end_pos = len(self.sentence)
		self.status = 'start'

	def __init__(self) :
		self.set_tokenizer()
		self.soul = {
			'start' : 
			{
				'digit' : ['int', False],
				'letter' : ['id', False],
				'literal' : ['literal', False],
				'full_stop' : ['error', False],
				'white_space' : ['white_space', False],
				'error' : ['error', False]
			},
			'int' : 
			{
				'digit' : ['int', False],
				'letter' : ['int', True],
				'literal' : ['int', True],
				'full_stop' : ['before_real', False],
				'white_space' : ['int', True],
				'error' : ['int', True]
			},
			'id' : 
			{
				'digit' : ['id', False],
				'letter' : ['id', False],
				'literal' : ['id', True],
				'full_stop' : ['id', True],
				'white_space' : ['id', True],
				'error' : ['id', True]
			},
			'real' : 
			{
				'digit' : ['real', False],
				'letter' : ['real', True],
				'literal' : ['real', True],
				'full_stop' : ['real', True],
				'white_space' : ['real', True],
				'error' : ['real', True]
			},
			'before_real' : 
			{
				'digit' : ['real', False],
				'letter' : ['error', True],
				'literal' : ['error', True],
				'full_stop' : ['error', True],
				'white_space' : ['error', True],
				'error' : ['error', True]
			},
			'white_space' : 
			{
				'digit' : ['white_space', True],
				'letter' : ['white_space', True],
				'literal' : ['white_space', True],
				'full_stop' : ['white_space', True],
				'white_space' : ['white_space', True],
				'error' : ['white_space', True]
			},
			'error' : 
			{
				'digit' : ['error', True],
				'letter' : ['error', True],
				'literal' : ['error', True],
				'full_stop' : ['error', True],
				'white_space' : ['error', True],
				'error' : ['error', True]
			},
			'literal' : 
			{
				'digit' : ['literal', True],
				'letter' : ['literal', True],
				'literal' : ['literal', True],
				'full_stop' : ['literal', True],
				'white_space' : ['literal', True],
				'error' : ['literal', True]
			}
		}

	def get_status(self, status, now_type) :
		return self.soul[status][now_type]

	def get_char_type(self, now_char) :
		if ord('0') <= ord(now_char) <= ord('9') :
			return 'digit'
		elif ord('a') <= ord(now_char.lower()) <= ord('z') :
			return 'letter'
		elif now_char in ['-', '+', '*', '/', '(', ')', ';', '='] :
			return 'literal'
		elif now_char == '.' :
			return 'full_stop'
		elif now_char in [' ', '\t', '\n', '\r'] :
			return 'white_space'
		else :
			return 'error'

	def is_end(self) :
		return self.stop_pos >= self.end_pos

	def name_literator(self, status, word) :
		return word if status == 'LITERAL' else status

	def name_error(self, status, word) :
		return 'ERROR' if status in ['BEFORE_REAL', 'START'] else status

	def edit_status(self, status, word) :
		status = self.name_literator(status.upper(),word)
		status = self.name_error(status.upper(),word)
		return status

	def get_token(self) :
		word = self.sentence[self.start_pos:self.stop_pos]
		return {'word' : word, 'status' : self.edit_status(self.status, word)}

	def is_return(self, status) :
		return status.lower() not in ['white_space']

	def next(self) :
		while not self.is_end() :
			now_char = self.sentence[self.stop_pos]
			char_type = self.get_char_type(now_char)
			self.status, is_cut = self.get_status(self.status, char_type)
			if is_cut :
				result = self.get_token() 
				self.start_pos = self.stop_pos
				self.status = 'start'
				if self.is_return(result['status']) :
					return result
			else :
				self.stop_pos += 1
		result = self.get_token()
		if self.is_return(result['status']) :
			return result
		return