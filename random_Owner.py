from audioop import maxpp
from pickle import NONE
import random
from telnetlib import Telnet
from faker import Faker
import pymysql

def IDmake():
    ownerid='ID'
    for i in range(1,13):
        ownerid+=str(random.randint(1,9))
    return ownerid

def RandomName():
    random_name=Faker("zh-CN")
    return random_name.name()

def RandomGender():
    i=random.randint(0,1)
    if i==0:
        return '男'
    else:
        return '女'

def RandomOccupation():
    random_occupation=Faker("zh-CN")
    return '职业：'+random_occupation.name()
    # 小孩子不懂事，乱写的

def RandomAddr():
    Addr='Addr'
    for i in range(1,25):
        Addr+=str(random.randint(1,9))
    return Addr

def RandomTel():
    Tel='Tel'
    for i in range(1,8):
        Tel+=str(random.randint(1,9))
    return Tel

def Register():
    nAme=RandomName()
    ownerID=IDmake()
    while usedID.get(ownerID,0)!=0:
        ownerID=IDmake()
    usedID[ownerID]=nAme
    print(nAme)
    print(ownerID)
    print(RandomGender())
    print(RandomOccupation())
    print(RandomAddr())
    print(RandomTel())
    # 输出到数据库,table Owner
    vAlue=(str(ownerID),str(nAme),str(RandomGender()),str(RandomOccupation()),str(RandomAddr()),str(RandomTel()))
    cur=db.cursor()
    cur.execute(sqlInsert,vAlue)
    
usedID={}
sqlInsert='INSERT INTO Owner(PersonID,Name,Gender,Occupation,Addr,Tel) VALUE(%s,%s,%s,%s,%s,%s)'
try:
    db=pymysql.connect(host='',user='',password='',database='EstateDB',charset='utf8mb4')
    print("连接成功")
except:
    print("快跑，是丁真在测代码")
    exit()
mAx=int(input('Enter the popularity:'))
for i in range(0,mAx):
    Register()
db.commit()
db.close()

# 随机生成名字

