from audioop import maxpp
import random
from telnetlib import Telnet
from faker import Faker
import pymysql

def Estatemake():
    ownerid='EID'
    for i in range(1,12):
        ownerid+=str(random.randint(1,9))
    return ownerid

def RandomName():
    random_name1=Faker("zh-CN")
    random_name2=Faker("zh-CN")
    return random_name1.name()+random_name1.name()

def RandomGender():
    i=random.randint(0,1)
    if i==0:
        return '男'
    else:
        return '女'

def RandomType():
    i=random.randint(0,3)
    return EstateT[i]

def RandomAddr():
    Addr='Addr'
    Addr+=str(random.randint(1,4))
    return Addr

def RandomDate():
    return str(random.randint(2017,2019))+'-'+str(random.randint(1,12))+'-'+str(random.randint(1,28))

def Register():
    EstateId=Estatemake()
    while usedID.get(EstateId,0)!=0:
        EstateId=Estatemake()
    EstateName=RandomName()
    usedID[EstateName]=EstateId
    sqlInsert='INSERT INTO Estate(EstateID,EstateName,EstateBuildName,EstateAddr,EstateCity,EstateType,PropertyArea,UsableArea,CompletedDate) VALUE(%s,%s,%s,%s,%s,%s,{},{},{})'.format(round(random.randint(100,200)+random.random(),2),round(random.randint(100,200)+random.random(),2),'\''+RandomDate()+'\'')
    vAlue=(str(EstateId),str(RandomName()),str(RandomName()),RandomAddr(),RandomAddr(),str(RandomType()))
    # python整出一个3byte值，我怎么搞
    # 输出到数据库,table Owner
    cur=db.cursor()
    cur.execute(sqlInsert,vAlue)

EstateT=('住宅','商铺','车位','别墅')
usedID={}
try:
    db=pymysql.connect(host='',user='',password='',database='EstateDB',charset='utf8mb4')
    print("连接成功:Estate")
except:
    print("快跑，是丁真在测代码")
    exit()
mAx=int(input('Enter the number of states:'))
for i in range(0,mAx):
    Register()
db.commit()
db.close()

# 随机生成名字

