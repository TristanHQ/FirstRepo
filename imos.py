#!/usr/bin/env python
##-*- coding: utf-8 -*-
 
import os
 
print("n欢迎大家跟我一起学Python")
 
system=os.name;                                                                #获取系统的类型
if(system=="nt"):
        print("您使用的操作系统是windows")
        print("使用windows表示的特定路径分割符是 ")+os.sep          #获取系统的分隔符
        print("您的电脑系统的终止符效果" + os.linesep)        #获取系统换行符
else:
        print("您使用的操作系统是Linux")
        print("使用windows表示的特定路径分割符是 " + os.sep)
        print("您的电脑系统的终止符是" + os.linesep)

        path=os.getcwd();                                                        #获得当前目录
        print("您运行本程序所在目录是 " + path)

        print("你电脑的Path环境变量为 " + os.getenv("Path"))
        #获取环境变量的值os.putenv(key,value)可以设置环境变量的值

        print("你当前文件夹中的文件有：")
        print(os.listdir(path))        #获取文件夹中的所有文件
