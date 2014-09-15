def turn(s):
    """过滤字符"""
    if '-'in e:
        spliter='-'
    elif ':'in e:
        spliter=':'
    else:
        return s
    (mins,secs)=s.split(spliter)
    return mins+'.'+secs
def openfile(filename):
    """打开一个文件返回一个列表"""
    try:
        with open(filename) as dat:
            data=dat.readline()
        return data.strip().split(',')
    except IOError as ioerr:
        print 'file erro' + str(ioerr)
        return(None)
sarah=openfile('sarah2.txt')
sarah_data={}
sarah_data['name']=sarah.pop(0)
sarah_data['dob']=sarah.pop(0)
sarah_data['time']=sarah
print sarah_data['time']
print [turn(e)for e in sarah_data['time']]
print set([turn(e)for e in sarah_data['time']])
print sorted(set([turn(e) for e in sarah_data['time']]))
print sarah_data['name']+' ,'+sarah_data['dob']+' ,'+str(sorted(set([turn(e)for e in sarah_data['time']]))[0:3])
