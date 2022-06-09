import pymongo
client=pymongo.MongoClient("mongodb://localhost:27017/")
db=client.Email_DB
def send_mail(data):
    collections=db.Mails
    collections.insert_one(data)
    return 
def view_inbox(username):
    inbox=[]
    collections=db.Mails
    inbox=collections.find({"to":username})
    return inbox
def view_sent(username):
    sent=[]
    collections=db.Mails
    sent=collections.find({"from":username})
    return sent        