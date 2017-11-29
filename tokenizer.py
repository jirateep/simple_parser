class Tokenizer() :
	def __init__() :
		self.soul = 
		{
			'start' : 
			{
				'digit' : ['int',False],
				'letter' : ['id',False],
				'literal' : ['literal',True],
				'full_stop' : ['error',True],
				'white_space' : ['white_space',True],
				'error' : ['error',True]
			},
			'int' : 
			{
				'digit' : ['int',False],
				'letter' : ['int',True],
				'literal' : ['int',True],
				'full_stop' : ['before_real',False],
				'white_space' : ['int',True],
				'error' : ['int',True]
			},
			'id' : 
			{
				'digit' : ['id',False],
				'letter' : ['id',False],
				'literal' : ['id',True],
				'full_stop' : ['id',True],
				'white_space' : ['id',True],
				'error' : ['id',True]
			},
			'real' : 
			{
				'digit' : ['real',False],
				'letter' : ['real',True],
				'literal' : ['real',True],
				'full_stop' : ['real',True],
				'white_space' : ['real',True],
				'error' : ['real',True]
			},
			'before_real' : 
			{
				'digit' : ['real',False],
				'letter' : ['error',True],
				'literal' : ['error',True],
				'full_stop' : ['error',True],
				'white_space' : ['error',True],
				'error' : ['error',True]
			}
		}

	def tokenizing(self, sentence) :
		start_pos = stop_pos = 0
		end_pos = len(sentence) - 1
		now_status = 'start'
		is_cut = False
		while stop_pos <= end_pos :
			now_char = sentence[stop_pos]
			if ord('0') <= ord(now_char) <= ord('9') :
				status, is_cut = self.get_status(status, 'digit')
			elif ord('a') <= ord(now_char.lower()) <= ord('z') :
				status, is_cut = self.get_status(status, 'letter')
			elif now_char in ['-','+','*','/','(',')'] :
				status, is_cut = self.get_status(status, 'literal')
			elif now_char == '.' :
				status, is_cut = self.get_status(status, 'full_stop')
			elif now_char in [' ','\t','\n','\r'] :
				status, is_cut = self.get_status(status, 'white_space')
			else :
				status, is_cut = self.get_status(status, 'error')
