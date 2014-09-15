# -*- coding: utf-8 -*-
import test2
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')
myspider =test2.webSpider()

lists=['0321002','0321007','0321022','0821001','0821100','0821101','0821001','0821005','0821102']
for sno in range(1650,1800):
	for num in lists:
		resphtml= myspider.send_get('http://210.27.12.1:90/queryDegreeScoreAction.do?studentid=xdleess20130621zq%d&degreecourseno=%s'%(sno,num))
		p=re.compile("\s+")
		rresphtml=re.sub(p,'',resphtml).decode('gbk')#解释为gbk格式
		#print rresphtml + '\n'
		finddate=re.search('<td\s?width="20%">(.*?)</td><td\s?width="15%">(.*?)</td>',rresphtml)
		finddate2=re.search('<tdwidth="16%"align="left">(.*?)</td><tdwidth="4%"align="left">.*?</td><tdwidth="14%"align="left">.*?</td><tdwidth="7%"align="left">(.*?)</td>',rresphtml)
		f=open("test.txt","a")
		if(finddate and finddate2):
			for e in finddate.groups():
				print e
				print >>f,e
		
			for e in finddate2.groups():
				print e		
				print >>f,e
		else:
			print 'cant find'
		f.close()
	
