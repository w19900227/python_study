def ex1(a, b, c):
	print "a=" , a , ",b=" , b , ",c=" , c

def ex2(a, b, *c):
	print "a=" , a , ",b=" , b , ",c=" , c , ";len:%d" % len(c)

def ex3(a, b, **c):
	print "a=" , a , ",b=" , b
	for x in c:
		print x + ": " + str(c[x])

def ex4(a, *b, **c):
	print "a=" , a , ",b=" , b
	for x in c:
		print x + ": " + str(c[x])

print "ex1 ========================="
ex1(1, 2, 3)
ex1(1, c=2, b=3)

print "ex2 ========================="
ex2(1, 2, 3, 4, 5, 6)

print "ex3 ========================="
ex3(1, c=2, b=3)

print "ex4 ========================="
ex4(1, 2, 3, 4, c=5)