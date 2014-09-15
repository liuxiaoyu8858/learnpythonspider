from turn import turn
class Athlete(list):
    def __init__(self,a_name,a_dob=None,a_times=[]):
        list.__init__([])
        self.name=a_name
        self.dob=a_dob
        self.extend(a_times)
 #   def add_time(self,time):
 #       self.append(self,time)
 #   def add_times(self,times):
 #       self.extend(self,times)
    def top3(self):
        return sorted(set([turn(e) for e in self]))[0:3]
a=Athlete('xiaoming')
a.append('2.10')
a.extend(['2-15','2.18','3:10','2.01','2.06'])
print a
print a.top3()
        
        
