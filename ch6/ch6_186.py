def turn (e):
    if '-' in e:
        spliter = '-'
    elif ':' in e:
        spliter = ':'
    else:
        return e
    (mins,secs)=e.split(spliter)
    return mins+'.'+secs
def openfile (s):
    try:
        with open (s) as dat :
            date=dat.readline()
            tem=date.strip().split(',')
            return {'name':tem.pop(0),'dop':tem.pop(0),'times':sorted(set([turn(e) for e in tem]))}
    except IOError as ir:
        print 'can not open the file'+str(ir)
james=openfile('james2.txt')
print str(james['name'])+str(james['times'])
        
