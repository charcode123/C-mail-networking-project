from numpy import dtype
import pymongo
client=pymongo.MongoClient("mongodb://localhost:27017/")
db=client.Email_DB
collections=db.Mails
x=collections.find({"from":"charan@cmail.com"})
y=[]
for i in x:
    y.append(i)

print(y)