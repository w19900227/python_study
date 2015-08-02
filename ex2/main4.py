class Demo(object):
	def __init__(self,x):
		self.x = x

	@classmethod
	def addOne(self, x):
		return x+1

	@staticmethod
	def addTwo(x):
		return x+2

	def addThree(self, x):
		return x+3

def main():
	print "one ========================"
	print Demo.addOne(2)

	print "two ========================"
	print Demo.addTwo(2)

	#print Demo.addthree(2) #Error
	print "three ========================"
	demo = Demo(2)
	print demo.addThree(2)


if __name__ == '__main__':
	main()