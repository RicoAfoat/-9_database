from audioop import maxpp
import random
from sqlite3 import Cursor
from telnetlib import Telnet
from faker import Faker
import pymysql

def Registmake():
    return random.randint(100000000,900000000)

def RandomDate():
    return str(random.randint(2017,2019))+'-'+str(random.randint(1,12))+'-'+str(random.randint(1,28))

def getPID():
    cur1=db.cursor()
    cur1.execute("SELECT PersonID FROM `Owner` LIMIT 1 OFFSET {}".format(cont1))
    return cur1.fetchall()


def getEID():
    cur2=db.cursor()
    cur2.execute("SELECT EstateID FROM `Estate` LIMIT 1 OFFSET {}".format(cont2))
    return cur2.fetchall()


def Register():
    PersonID=getPID()
    global cont1
    global cont2
    cont1+=1
    rnm=random.randint(1,2)
    for i in range(1,rnm+1):
        cur=db.cursor()
        RegistId=Registmake()
        while usedID.get(RegistId,0)!=0:
            RegistId=Registmake()
        usedID[RegistId]=RegistId
        EstateID=getEID()
        sqlInsert='INSERT INTO Registration(RegisterID,PersonID,EstateID,Price,PurchaseDate,DeliverDate) VALUE({},\'{}\',\'{}\',{},{},{})'.format(RegistId,PersonID[0][0],EstateID[0][0],round(random.randint(2000000,10000000)+random.random(),2),'\''+RandomDate()+'\'','\''+RandomDate()+'\'')
        cur.execute(sqlInsert)
        cont2+=1

global cont1
global cont2
cont1=1
cont2=1
usedID={}
try:
    db=pymysql.connect(host='',user='',password='',database='EstateDB',charset='utf8mb4')
    print("连接成功:Registration")
except:
    print("快跑，是丁真在测代码")
    exit()
mAx=int(input('Enter the number of Registrations:'))
for i in range(0,mAx):
    Register()
db.commit()
db.close()

# 随机生成名字

