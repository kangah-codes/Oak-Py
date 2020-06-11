# Memory setup with some native functions

class nativeFunction():
	def __init__(self):
		self.isNative = True
		self.typeof = 'fn'
		self.params = []

	def getVariable(self):
		return self.name

class printFunction(nativeFunction):
	def __init__(self):
		nativeFunction.__init__(self)
		self.name = 'printf'
		print(self.isNative)

	def print(self, params):
		arrToPrint = []
		for i in params:
			if (params[params.index(i)]):
				arrToPrint.append(params[params.index(i)])
			elif (type(params[params.index(i)]) in (int, float)):
				arrToPrint.append(params[params.index(i)])
			else:
				arrToPrint.append(filter(lambda e: (True if e != '"' else False) , params[i].split('')).join(''))
		if len(arrToPrint) == 1:
			print(arrToPrint[0])
		else:
			print(''.join(arrToPrint))

	def __repr__(self):
		return self.name

class pushFunction(nativeFunction):
	def __init__(self):
		nativeFunction.__init__(self)
		self.name = 'push'

	def push(self, params):
		thiss = params[0]
		arrVariable = params[1]
		thingToPush = params[2]

		if (int(thingToPush)):
			thingToPush = int(thingToPush)
		# if (type(thingToPush) == dict):