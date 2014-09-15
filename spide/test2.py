import urllib
import urllib2
import cookielib
import re
import string

class webSpider:
	
	def __init__(self):
		self.cookie_jar = cookielib.CookieJar()
		self.opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookie_jar))
		self.headers={'User-Agent':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36'}
	def send_get(self,get_url):
		result = ""
		try:
			my_request =urllib2.Request(url=get_url,headers=self.headers)
			result=self.opener.open(my_request).read()
		except Exception,e:
			print "exception",e
		return result