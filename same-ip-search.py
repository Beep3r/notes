#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
Author:Jumbo
Website:http://www.chinabaiker.com
Date:2015/22/3
Thanks:ziwen,L3m0n,Object
'''
import urllib
import sys
import re
try:
	url = "http://s.tool.chinaz.com/same?s= "
	zhan = sys.argv[1]
	f = open(zhan + ".txt","w")
	jieguo = urllib.urlopen(url + str(zhan))
	content = jieguo.read()
	ree = r"\" target\=\_blank\>(.*?)\<\/a\>\<\/div\>"
	ss = re.findall(ree,content)
	for x in ss:
		print>>f,x
	print 'ok,look ' + zhan + '.txt.'
	f.close()
except:
	print 'eg:python %s www.chinabaiker.com' % sys.argv[0]
 
