#coding:utf-8
#Author:Zhiqiang Yuan
import os

print("############################################")
print("##           欢迎使用小袁单词！           ##")

while True:
    print("##         请输入您需要执行的操作：       ##")
    print("##          O：对单词进行管理             ##")
    print("##          R：对单词进行记录             ##")
    print("##          L：对单词进行学习             ##")
    print("##          T：对单词进行测试             ##")
    print("##              Q：退出                   ##")
    print("############################################")

    op = input("你需要做点什么呢:")
    op = op[0].lower()

    if op == "o":
        os.system("python EO.py")
    elif op == "r":
        os.system("python ER.py")
    elif op == "l":
        os.system("python EL.py")
    elif op == "t":
        os.system("python ET.py")
    elif op == "q":
        break
    else:
        print("输入错误！")

print("############################################")
print("##          欢迎再次使用小袁单词！        ##")
