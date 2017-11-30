class Parser :

	def set_parser(self) :
		self.stack = ['S']
		self.tokens = []

	def __init__(self) :
		self.set_parser()
		self.soul = {
			'S' : 
			{
				'ID' :	['ID','S1'],
				'INT' : ['error'],
				'REAL' : ['error'],
				'+' : ['error'],
				'-' : ['error'],
				'/' : ['error'],
				'*' : ['error'],
				'(' : ['error'],
				')' : ['error'],
				'=' : ['error'],
				';' : ['error'],
				'' : []
			},
			'S1' : 
			{
				'ID' :	['error'],
				'INT' : ['error'],
				'REAL' : ['error'],
				'+' : ['error'],
				'-' : ['error'],
				'/' : ['error'],
				'*' : ['error'],
				'(' : ['error'],
				')' : ['error'],
				'=' : ['=','E','S2'],
				';' : ['error'],
				'' : []
			},
			'S2' : 
			{
				'ID' :	['error'],
				'INT' : ['error'],
				'REAL' : ['error'],
				'+' : ['error'],
				'-' : ['error'],
				'/' : ['error'],
				'*' : ['error'],
				'(' : ['error'],
				')' : ['error'],
				'=' : ['error'],
				';' : [';','S'],
				'' : []
			},
			'E' : 
			{
				'ID' : ['T','E1'],
				'INT' : ['T','E1'],
				'REAL' : ['T','E1'],
				'+' : ['T','E1'],
				'-' : ['T','E1'],
				'/' : ['T','E1'],
				'*' : ['T','E1'],
				'(' : ['T','E1'],
				')' : ['T','E1'],
				'=' : ['T','E1'],
				';' : ['T','E1'],
				'' : ['T','E1']
			},
			'E1' : 
			{
				'ID' : [],
				'INT' : [],
				'REAL' : [],
				'+' : ['+','T','E1'],
				'-' : ['-','T','E1'],
				'/' : [],
				'*' : [],
				'(' : [],
				')' : [],
				'=' : [],
				';' : [],
				'' : []
			},
			'T' : 
			{
				'ID' : ['F','T1'],
				'INT' : ['F','T1'],
				'REAL' : ['F','T1'],
				'+' : ['F','T1'],
				'-' : ['F','T1'],
				'/' : ['F','T1'],
				'*' : ['F','T1'],
				'(' : ['F','T1'],
				')' : ['F','T1'],
				'=' : ['F','T1'],
				';' : ['F','T1'],
				'' : ['F','T1'],
			},
			'T1' : 
			{
				'ID' : [],
				'INT' : [],
				'REAL' : [],
				'+' : [],
				'-' : [],
				'/' : ['/','F','T'],
				'*' : ['/','F','T'],
				'(' : [],
				')' : [],
				'=' : [],
				';' : [],
				'' : []
			},
			'F' : 
			{
				'ID' : ['ID','A'],
				'INT' : ['INT','A'],
				'REAL' : ['REAL','A'],
				'+' : ['error'],
				'-' : ['error'],
				'/' : ['error'],
				'*' : ['error'],
				'(' : ['(','E',')'],
				')' : ['error'],
				'=' : ['error'],
				';' : ['error'],
				'' : []
			},
			'A' : 
			{
				'ID' : [],
				'INT' : [],
				'REAL' : [],
				'+' : [],
				'-' : [],
				'/' : [],
				'*' : [],
				'(' : ['(','E',')'],
				')' : [],
				'=' : [],
				';' : [],
				'' : []
			},
		}

	def get_list(self, token) :
		#print(self.stack[len(self.stack)-1])
		#print(token)
		poping = self.stack.pop(0)
		print(poping)
		print(token)
		return self.soul[poping][token]

	def is_correct(self) :
		while not self.delete_same_token() and len(self.stack) != 0 :
			add_list = self.get_list('')
			self.stack = add_list + self.stack
			print('last stack: ' + str(self.stack))

	def delete_same_token(self) :
		check = False
		while len(self.tokens) > 0 and len(self.stack) > 0 :
			if self.stack[0] == self.tokens[0] :
				self.stack.pop(0)
				self.tokens.pop(0)
				check = True
			else :
				break
		return check
		#print(self.tokens)
		#print(self.stack)

	def new_token(self, token) :
		print('in: ' + token)
		self.tokens = [token] + self.tokens
		#self.tokens.append(token)
		while not self.delete_same_token() :
			add_list = self.get_list(token)
			self.stack = add_list + self.stack
			print('be stack: ' + str(self.stack))
		
		print('stack: ' + str(self.stack))
		print('tokens: ' + str(self.tokens))
		print()