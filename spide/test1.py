# -*- coding: UTF-8 -*-
import urllib2;
import re;
def main():
	url="http://210.27.12.1:90/queryDegreeScoreAction.do?studentid=xdleess20130621zq1731&degreecourseno=0321007";
	#userMainUrl="http://www.hao123.com";
	req=urllib2.Request(url);
	try:
		resp=urllib2.urlopen(req);
	except Exception,e:
		print "exception",e 
	respHtml=resp.read();
	print "respHtml=",respHtml;
	foundH1user = re.search('<td width="20%">学号:(?p<sno>.+?)</td><td width="15%">姓名：(?p<name>.+?)</td><td>课程编号：(?p<cno>.+?)</td>', respHtml);
	print "foundH1user=",foundH1user;
	if(foundH1user):
		h1user=foundH1user.group("sno","name","cno");
		print "sno,name,cno",h1user;
if __name__=="__main__":
	main();

