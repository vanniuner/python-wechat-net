#coding=utf-8
import itchat
from itchat.content import *
import sys
import os

reload(sys)
sys.setdefaultencoding('utf-8')

@itchat.msg_register([TEXT])
def simple_reply(msg):
    if msg['User']['NickName'] != 'sdserver':
        return
    if msg['Type'] != TEXT:
        return
    author = itchat.search_friends(nickName=r'sdserver')[0]
    if msg['Content'][1:]!='':
        print msg['Content'][1:]
    commandstr = raw_input("[root@raspberry]$ ")
    if commandstr=='exit':
        os._exit(0)
    else:
        author.send(commandstr)

if __name__ == '__main__':
    itchat.auto_login(enableCmdQR=0, hotReload=True)
    author = itchat.search_friends(nickName=r'sdserver')[0]
    author.send("hand")
    itchat.run()
    os._exit(0)
    

