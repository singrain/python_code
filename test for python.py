#coding: utf-8
import urllib.request
import re
req = urllib.request.Request('http://www.so.com')
response = urllib.request.urlopen(req)
the_page = response.read().decode('utf-8')
#print (response)

reg=re.compile('<strong>(网页)</strong>')
result=reg.findall(the_page)
print (result)
