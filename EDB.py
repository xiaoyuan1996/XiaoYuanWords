#coding:utf-8
#Author:Zhiqiang Yuan
#这个文件为数据库管理模块，负责python与mysql的交互

#############################################################################################################
############################### 数据库操作   #################################################################
import MySQLdb
import os
import random

db = MySQLdb.connect(host="localhost",user="root",passwd="123",db="english",charset="utf8")

cursor = db.cursor()    #创建一个游标对象
cursor.execute("use english;")    #执行SQL语句，注意这里不返回结果，只是执行而已

def read_last():
    cursor.execute("select * from NeedLearn order by id desc limit 1;")
    data = cursor.fetchall()[0]
    return data

def read_all():
    cursor.execute("select * from NeedLearn;")
    data = cursor.fetchall()
    return data

def read_one(id):
    cmd = "select * from NeedLearn where id="+str(id)+";"
    cursor.execute(cmd)
    data = cursor.fetchall()[0]
    return data

def read_all_num():
    cursor.execute("select count(*) from NeedLearn;")
    num= cursor.fetchall()[0][0]
    return num

def insert(word, mean, sentence):
    # new = (2, "I", "我", "I love you!")
    id_last = read_all_num()
    id = id_last+1
    param = (id,word,mean,sentence)
    sql = "insert into NeedLearn values(%s,%s,%s,%s)"
    n = cursor.execute(sql, param)
    # 提交
    db.commit()

def sort_id():
    cursor.execute("alter table NeedLearn drop id;")
    db.commit()
    cursor.execute("alter table NeedLearn add id int(11) primary key auto_increment first;")
    db.commit()

def delete(id):
    cmd = "delete from NeedLearn where id = '"+str(id)+"';"
    cursor.execute(cmd)
    db.commit()
    sort_id()

def delete_last():
    cursor.execute("delete from NeedLearn where 1 order by id desc limit 1;")
    db.commit()

def into_file(route="E:\EL.txt"):
    if os.path.exists(route):
        os.remove(route)
    cursor.execute("SELECT * FROM NeedLearn INTO OUTFILE 'E:\EL.txt'FIELDS TERMINATED BY ',' LINES TERMINATED BY '\r\n' ;")

    import pandas as pd
    # read from EL.txt
    file = open("E:\EL.txt",'r',encoding="UTF-8")
    content=file.readlines()
    file.close()
    data = []
    for c in content:
        temp = c.replace("\,","，")
        temp = temp.split(',')
        data.append(temp)

    data = pd.DataFrame(data,columns=["Index","Word","Means","Sentense"])
    data.to_csv("E:\EL.csv",index=None)
    os.remove(route)

def word_learn():
    # 返回单词
    data = read_last()
    if data[0] <= 5:
        return read_all()
    else:
        i = 1
        id_table = []
        while(i<=5):
            id = int(random.random()*data[0])+1
            if id not in id_table:
                id_table.append(id)
                i = i + 1

        data_read = []
        for id in id_table:
            data_read.append(read_one(id))
        return data_read



# print(word_learn())
# delete_last()
# sort_id()

#create table if not exists `NeedLearn`(`id` INT UNSIGNED AUTO_INCREMENT, `word` varchar(128),`mean` varchar(128),`sentence` varchar(1024) , PRIMARY KEY ( `id` ));