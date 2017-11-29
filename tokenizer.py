class Tokenizer :
	def __init__(self) :
		self.soul = {
			'start' : 
			{
				'digit' : ['int',False],
				'letter' : ['id',False],
				'literal' : ['literal',False],
				'full_stop' : ['error',False],
				'white_space' : ['white_space',False],
				'error' : ['error',False]
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
			},
			'white_space' : 
			{
				'digit' : ['white_space',True],
				'letter' : ['white_space',True],
				'literal' : ['white_space',True],
				'full_stop' : ['white_space',True],
				'white_space' : ['white_space',True],
				'error' : ['white_space',True]
			},
			'error' : 
			{
				'digit' : ['error',True],
				'letter' : ['error',True],
				'literal' : ['error',True],
				'full_stop' : ['error',True],
				'white_space' : ['error',True],
				'error' : ['error',True]
			}
		}

	def get_status(self, status, now_type) :
		return self.soul[status][now_type]

	def tokenizing(self, sentence) :
		start_pos = stop_pos = 0
		end_pos = len(sentence) - 1
		now_status = 'start'
		is_cut = False
		while stop_pos <= end_pos :
			now_char = sentence[stop_pos]
			if ord('0') <= ord(now_char) <= ord('9') :
				now_status, is_cut = self.get_status(now_status, 'digit')
			elif ord('a') <= ord(now_char.lower()) <= ord('z') :
				now_status, is_cut = self.get_status(now_status, 'letter')
			elif now_char in ['-','+','*','/','(',')'] :
				now_status, is_cut = self.get_status(now_status, 'literal')
			elif now_char == '.' :
				now_status, is_cut = self.get_status(now_status, 'full_stop')
			elif now_char in [' ','\t','\n','\r'] :
				now_status, is_cut = self.get_status(now_status, 'white_space')
			else :
				now_status, is_cut = self.get_status(now_status, 'error')

			if is_cut :
				print(now_status, sentence[start_pos:stop_pos])
				start_pos = stop_pos
				now_status = 'start'
			else :
				stop_pos += 1

		print(now_status, sentence[start_pos:stop_pos])