with open ('james.txt')as james:
    data=james.readline()
    james=data.strip().split(',')
with open ('julie.txt')as julie:
    data=julie.readline()
    julie=data.strip().split(',')
with open ('mikey.txt')as mikey:
    data=mikey.readline()
    mikey=data.strip().split(',')
with open ('sarah.txt')as sarah:
    data=sarah.readline()
    sarah=data.strip().split(',')
print james
print julie
print mikey
print sarah
raw_input('any key continue')
print sorted(james)
print sorted(julie)
print sorted(mikey)
print sorted(sarah)
raw_input('any key continue')
def turn(s):
    if '-' in s:
        spliter='-'
    elif ':' in s:
        spliter =':'
    else:
        return s
    (mins,secs)=s.split(spliter)
    return mins+'.'+secs
a=[]
b=[]
c=[]
for each_item in james:
    a.append(turn(each_item))
for each_item in julie:
    b.append(turn(each_item))
for each_item in mikey:
    c.append(turn(each_item))
"""aԭ�ظ�ֵ"""
a.sort()
print a
print sorted(b)
print sorted(c)
print "ȥ�أ���ӡǰ��"
ua=[]
ub=[]
uc=[]
for each in a:
    if each not in ua:     """not in ȥ��""""
        ua.append(each)
print ua[0:3]
for each in b:
    if each not in ub:
        ub.append(each)
print ub[0:3]
for each in c:
    if each not in uc:
        uc.append(each)
print uc[0:3]
"""sarahʹ�����б��Ƶ�������ɾ���ظ��sorted()���������б������з�ƬֻҪǰ3"""
print sorted(set([turn(each) for each in sarah]))[0:3]

          


