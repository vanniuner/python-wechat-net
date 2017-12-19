# python-wechat-net
a nat-ddns base on python &amp; wechart 
基于 python & 微信的内网穿透 

## 概述
市面上有很多内网穿透的工具，比如花生壳，frp等。像花生壳这一类是收费服务，而搭建frp则需要具有公网ip的机器。本程序 通过itchart将指令发送到server机器上进行执行，并返回结果。双方通信就是基于微信来的。主要是方便省钱，而且可以做到高度自定义。美中不足的是，所有交互式命令，以及main programe shell程序都将在服务器端挂起，导致客户端无法收到消息而处于wait状态。因此，需要在客户端的命令中，禁止输入该类命令。

## 准备
 ### 两个可以扫码登录的微信号 （微信有一些限制，刚注册的微信号还无法用web微信。）
 ### 安装python的linux机器


## 使用
### 启动服务器服务
### python server/pye-server.py
### 使用微信A扫码

### 客户端链接
### python pye-client.py
### 使用微信B扫码
