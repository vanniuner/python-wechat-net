#coding=utf-8
import itchat
import commands
from itchat.content import *
import os
import sys
import re
import time

reload(sys)
sys.setdefaultencoding('utf-8')
pattern = re.compile(r'(vim|top|vi|ps -ef|su|sh|tail -f).*')

@itchat.msg_register([itchat.content.TEXT])
def simple_reply(msg):
    if msg['Type'] == TEXT:
    	output=''
    	try:
	    	if pattern.match(msg['Content']):
	    		output = msg['Content'] + ' is useless'
	    	elif msg['Content'].startswith('cd '):
	    		pwd=os.getcwd()+"/"  		
	    		if(msg['Content'][3:].startswith('../')==True):
	    			dirtemp = pwd + msg['Content'][3:]
	    		else:
	    			dirtemp = msg['Content'][3:]
	    		os.chdir(dirtemp)
	    		status=0
	    		output=os.getcwd()
	    	elif msg['Content']=='hand':
	    		status=0
			commands.getstatusoutput('cd /root')
	    		output='welcome '+msg['FromUserName']
	    	else:
	    		print str(commands.getstatusoutput('date')[1])
	    		(status, output) = commands.getstatusoutput(msg['Content'])
	    		print 'done'
	    		if msg['Content'] == 'ls':
	    			output = output.replace('\n', '\t')
        except Exception,e:
			itchat.send(u'.error ,%s , %s' % (repr(e),output), msg['FromUserName'])
			return ""
        itchat.send(u'.%s' % (output), msg['FromUserName'])
time.sleep(10)
commands.getstatusoutput('cd /root')
itchat.auto_login(enableCmdQR=1, hotReload=True)
itchat.run()
