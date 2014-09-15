a=[]
b=[]
try:
    with open('hello.txt')as data:
        for each_line in data:
            try:
                (role,speak)=each_line.split(':')
                if role =='a':
                    a.append(speak)
                elif role =='b':
                    b.append(speak)
            except ValueError:
                pass
except IOError as er:
    print('the file not exit',str(er))
try:
    with open('aspeak.txt','w') as aspeak,open('bspeak.txt','w') as bspeak:
        print>>aspeak,a
        print>>bspeak,b
except IOError:
    print('the file a and b not exit')
