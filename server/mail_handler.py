import pymongo
client=pymongo.MongoClient("mongodb://localhost:27017/")
db=client.Email_DB
def mail(data):
    collections=db.Mails
    collections.insert_one(data)
    