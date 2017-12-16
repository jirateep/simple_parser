class Parser :

	def set_parser(self) :
		self.stack = ['S', '$']
		self.tokens = []

	def __init__(self) :
		self.set_parser()
		self.soul = {
			'S' : 
			{
				'ID' : ['S1','S'],
				'INT' : [],
				'REAL' : [],
				'+' : [],
				'-' : [],
				'/' : [],
				'*' : [],
				'(' : [],
				')' : [],
				'=' : [],
				';' : [],
				'' : []
			},
			'S1' : 
			{
				'ID' : ['ID', '=', 'E', ';'],
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
				'' : ['F','T1']
			},
			'T1' : 
			{
				'ID' : [],
				'INT' : [],
				'REAL' : [],
				'+' : [],
				'-' : [],
				'/' : ['/','F','T'],
				'*' : ['*','F','T'],
				'(' : [],
				')' : [],
				'=' : [],
				';' : [],
				'' : []
			},
			'F' : 
			{
				'ID' : ['ID','A'],
				'INT' : ['INT'],
				'REAL' : ['REAL'],
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

	def parsing(self, token) :
		#print(self.stack, token)
		if self.stack[0] == token :
			self.stack.pop(0)
			return True
		else :
			front = self.stack.pop(0)
			if front not in self.soul :
				return False
			self.stack = self.soul[front][token] + self.stack
			if self.stack[0] == 'error' :
				return False
			return self.parsing(token)

	def is_accept(self) :
		self.parsing('$')
		return self.stack == []