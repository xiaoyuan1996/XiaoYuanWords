#coding:utf-8
#Author:Zhiqiang Yuan
import EDB

print("++++++++++++++++++++++++++++++++++++++++++++++++++")
print("            欢迎使用小袁单词操作系统！               ")
print("++++++++++++++++++++++++++++++++++++++++++++++++++")

while True:

    print("==================================================")
    print("          请输入数字选择需要执行的操作             ")
    print("             1.查询词库个数。")
    print("                2.显示词库。")
    print("             3.导出词库至E:\EL.csv。")
    print("               4.删除固定ID。")
    print("                 q.退出。")
    print("==================================================")

    op = input()
    if op == "1":
        num = EDB.read_all_num()
        print("+================================================+")
        print("当前词库中一共有{}个单词，加油学习吧！".format(num))
        print("+================================================+")

        print("还需要做点别的吗？")
        print("+================================================+")
    elif op == "2":
        num = EDB.read_all_num()
        if num == 0:
            print("--------------------------------------------------")
            print("当前词库中没有单词呢！加油记录吧！")
            print("--------------------------------------------------")
        else:
            data = EDB.read_all()
            print("--------------------------------------------------")
            print("id  单词        含义               句子")
            print("--------------------------------------------------")
            for l in data:
                print("{:<2d}   {:<8s}   {:<10s}   {:<10s}".format(l[0], l[1], l[2], l[3]))
                print("--------------------------------------------------")

        print("还需要做点别的吗？")
        print("+================================================+")
    elif op == "3":
        EDB.into_file()
        print("+================================================+")
        print("导入成功，请在E:\EL.csv查看。")
        print("+================================================+")
        print("还需要做点别的吗？")
        print("+================================================+")

    elif op == "4":
        key_ID = input("请输入需要删除的ID号：\n")

        try:
            print(EDB.read_one(int(key_ID)))
            key_identify = input("确认删除？(y/n)\n")
            if key_identify == "y":
                EDB.delete(int(key_ID))
                print("该词条已删除。")
            else:
                print("好的，我知道了。")
                continue

        except:
            print("输入错误！")
            continue

    elif op == "q":
        break
    else:
        print("请输入正确的数字！")
        print("+================================================+")

print("++++++++++++++++++++++++++++++++++++++++++++++++++")
print("         小袁单词操作系统欢迎您的再次使用！           ")
print("++++++++++++++++++++++++++++++++++++++++++++++++++")