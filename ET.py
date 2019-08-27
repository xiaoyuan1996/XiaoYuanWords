#coding:utf-8
#Author:Zhiqiang Yuan
# 学习时每次显示5个单词及其含义，选择一个你认为最简单的，
# 若这个单词含义和你设想一致的话，这个词将从数据库中删除
# 如果都不熟悉则按N进行下一个五个单词

import EDB

print("++++++++++++++++++++++++++++++++++++++++++++++++++")
print("            欢迎使用小袁单词测试系统！               ")
print("++++++++++++++++++++++++++++++++++++++++++++++++++")

while True:
    if EDB.read_all_num() == 0:
        print("         当前词库中没有单词呢！添加后再来吧！")
        print("--------------------------------------------------")
        break
    else:
        data = EDB.word_learn()

    # print("id  单词        含义               句子")
    print("id  单词        ")
    print("--------------------------------------------------")

    for l in data:
        # print("{:<2d}   {:<8s}   {:<10s}   {:<10s}".format(l[0],l[1],l[2],l[3]))

        print("{:<2d}   {:<8s}".format(l[0], l[1]))
        print("--------------------------------------------------")

    print("请选择你学会的单词，输入id,全不会请输'.',退出输'q'")
    print("+------------------------------------------------+")
    state = input()

    if state == 'q':
        break
    elif state == '.':
        pass
    else:
        while True:
            if state.isnumeric():

                temp = False
                for l in data:
                    if int(state)==l[0]:
                        temp = True
                if temp:
                    # EDB.delete(int(state))
                    print("id  单词        含义               句子")
                    temp_data = EDB.read_one(int(state))
                    print("{:<2d}   {:<8s}   {:<10s}   {:<10s}".format(temp_data[0],temp_data[1],temp_data[2],temp_data[3]))
                    print("--------------------------------------------------")

                    key_same = input("和你想的一样吗？(y/n)\n")
                    if key_same =="y":
                        EDB.delete(int(state))
                        print("--------------------------------------------------")
                        print("该单词已学习完毕。")
                        print("--------------------------------------------------")

                    else:
                        print("没事，要更加努力哦！")
                        print("--------------------------------------------------")

                    break
                else:
                    print("--------------------------------------------------")
                    print("请输入正确ID！")
                    state = input()
            else:
                print("--------------------------------------------------")
                print("请输入正确数字！")
                state = input()
                if state == ".":
                    break

print("++++++++++++++++++++++++++++++++++++++++++++++++++")
print("           欢迎您再次使用小袁单词测试系统！")
print("++++++++++++++++++++++++++++++++++++++++++++++++++")