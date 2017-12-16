class Parser :

	def set_parser(self) :
		self.stack = ['S', '$']

	def __init__(self) :
		self.set_parser()
		self.tokens = ['ID', 'INT', 'REAL', '+', '-', '/', '*', '(', ')', '=', ';', '$']
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
				'$' : []
			},
			'S1' : 
			{
				'ID' : ['ID', '=', 'E', ';'],
				'INT' : ['ERROR'],
				'REAL' : ['ERROR'],
				'+' : ['ERROR'],
				'-' : ['ERROR'],
				'/' : ['ERROR'],
				'*' : ['ERROR'],
				'(' : ['ERROR'],
				')' : ['ERROR'],
				'=' : ['ERROR'],
				';' : ['ERROR'],
				'$' : []
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
				'$' : ['T','E1']
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
				'$' : []
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
				'$' : ['F','T1']
			},
			'T1' : 
			{
				'ID' : [],
				'INT' : [],
				'REAL' : [],
				'+' : [],
				'-' : [],
				'/' : ['/','F','T1'],
				'*' : ['*','F','T1'],
				'(' : [],
				')' : [],
				'=' : [],
				';' : [],
				'$' : []
			},
			'F' : 
			{
				'ID' : ['ID','A'],
				'INT' : ['INT'],
				'REAL' : ['REAL'],
				'+' : ['ERROR'],
				'-' : ['ERROR'],
				'/' : ['ERROR'],
				'*' : ['ERROR'],
				'(' : ['(','E',')'],
				')' : ['ERROR'],
				'=' : ['ERROR'],
				';' : ['ERROR'],
				'$' : ['ERROR']
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
				'$' : []
			},
		}

	def parsing(self, token) :
		# print(self.stack, token)
		if len(self.stack) == 0 :
			return False
		front = self.stack[0]
		if front in self.tokens :
			if front == token :
				self.stack.pop(0)
				return True
			if front != '$' :
				return False
		if front not in self.soul.keys() :
			return False
		self.stack.pop(0)
		self.stack = self.soul[front][token] + self.stack
		return self.parsing(token)

	def is_accept(self) :
		return self.parsing('$')