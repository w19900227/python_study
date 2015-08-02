class myDecorator(object):

    def __init__(self, f):
        print "inside myDecorator.__init__()"
        f(1) # Prove that function definition has completed
        self.__function = f

    def __call__(self, *args):
        # the *args magic is here to mirror the original parameter list of
        # the decorated function. But it is better to place here parameter list
        # of the function you want to decorate, in order to minimize error possibilities
        print "inside myDecorator.__call__()"
        return self.__function(*args)

@myDecorator
def aFunction(*a):
    print a
    print "inside aFunction()"

print "==========================="
print "Finished decorating aFunction()"

print "==========================="
aFunction(2)

print "==========================="
aFunction('a', 23, 42)

