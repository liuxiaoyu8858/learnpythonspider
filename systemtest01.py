import sys
args=sys.argv
if len(args)==1:
        print 'Hello, world!'
elif len(args)==2:
        print 'Hello, %s!' % args[1]
else:
        print 'Too many arguments!'
