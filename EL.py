#coding:utf-8
#Author:Zhiqiang Yuan
# 学习时每次显示5个单词及其含义

import EDB

print("++++++++++++++++++++++++++++++++++++++++++++++++++")
print("            欢迎使用小袁单词学习系统！               ")
print("++++++++++++++++++++++++++++++++++++++++++++++++++")

while True:
    if EDB.read_all_num() == 0:
        print("         当前词库中没有单词呢！添加后再来吧！")
        print("--------------------------------------------------")
        break
    else:
        data = EDB.word_learn()

    print("id  单词        含义               句子")
    # print("id  单词        ")
    print("--------------------------------------------------")

    for l in data:
        print("{:<2d}   {:<8s}   {:<10s}   {:<10s}".format(l[0],l[1],l[2],l[3]))

        # print("{:<2d}   {:<8s}".format(l[0], l[1]))
        print("--------------------------------------------------")

    print("学会了吗？任意键学习下一波,退出输'q'")
    print("+------------------------------------------------+")

    state = input()

    if state == 'q':
        break
    else:
        pass

print("++++++++++++++++++++++++++++++++++++++++++++++++++")
print("           欢迎您再次使用小袁单词学习系统！")
print("++++++++++++++++++++++++++++++++++++++++++++++++++")