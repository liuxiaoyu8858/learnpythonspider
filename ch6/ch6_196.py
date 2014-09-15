def turn(e):
    if '-' in e:
        spliter='-'
    elif ':' in e:
        spliter=':'
    else:
        return e
    (mins,secs)=e.split(spliter)
    return mins+'.'+secs
class Athlete:
    def __init__(self,a_name,a_dob=None,a_time=[]):
        self.name=a_name
        self.dob=a_dob
        self.time=a_time
    def top3(self):
        return sorted(set([turn(e) for e in self.time]))[0:3]
    def add_time(self,time):
        self.time.append(time)
    def add_times(self,times):
        self.time.extend(times)
def openfile(s):
    try:
        with open(s) as f:
            data=f.readline()
        temp=data.strip().split(',')
        return (Athlete(temp.pop(0),temp.pop(0),temp))
    except IOError as ir:
        print 'can not open'+str(ir)
        return None
a=openfile('sarah2.txt')
print a.time
time=raw_input("please input a time:")
a.add_time(time)
print a.time
times=raw_input("input times:")
a.add_times(['2.22','2.15','2.16'])
print a.time
print a.name+str(a.top3())
        
