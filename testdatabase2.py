###获取分别按SourceCode查询后的字段集合

from pymongo import MongoClient
import pandas as pd

##连接MongoDB
client = MongoClient('mongodb://newuserhello:IoTproject@192.168.146.192:27017/')
##指定要操作的数据库，test
db = client.test
##获取数据库中的所有表
collection_list = db.list_collection_names()
print(collection_list)

##限定数据库表，InternationalData.ILO_Value_20201207
mycol = db["message"]

# # 获取SourceCode
# ##方式一：SourceCode从excel中读取
# '''
# scode_data=pd.read_csv('data/SourceCode.csv',encoding='gb18030')
# print(scode_data.head())
# Scode=scode_data['SourceCode'].values
# '''
#
# ##方式二：SourceCode直接从MongoDB查询获得
# Scode = mycol.distinct("SourceCode")
# # print (Scode)
#
# # 方式三：直接写列表
# # Scode=["ABW_A"]
Scode=['test']
totalkey = []  ##totalkey记录所有SourceCode的涉及到的字段列表
key = []
record = []
t = 1  ## 记录第几个SourceCode
##遍历SourceCode
for code in Scode:
    # code=code
    print(t, code)
    t += 1
    ##设置查询的条件
    # myquery = {"SourceCode": code}
    myquery = {}
    mydoc = mycol.find(myquery)

    i = 0  ## i记录每个SourceCode对应的记录数
    keyvalue = []  # keyvalue记每个SourceCode的字段列表
    ##遍历每个SourceCode下的记录
    for x in mydoc:
        # print (x)
        i += 1
        for j in x.keys():  ##遍历每条记录的字段
            if j not in keyvalue:
                keyvalue.append(j)
            if j not in totalkey:
                totalkey.append(j)
    # print (keyvalue)
    # print (i)
    # data["SourceCode"].append(code)
    key.append(keyvalue)
    record.append(i)

data = pd.DataFrame()
print(data)

# data["SourceCode"] = Scode
# data["Keyvalue"] = key
# data['record'] = record
print(data['code'])
print(totalkey)
# print(data.head())

# data.to_csv('data/result.csv', encoding='gb18030', index=1)
