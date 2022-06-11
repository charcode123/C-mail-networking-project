import pymongo
import json
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
    dict_inbox={'mails':inbox}
    dict_inbox_json=json.dumps(dict_inbox)
    return dict_inbox_json
def view_sent(username):
    sent=[]
    collections=db.Mails
    sent=collections.find({"from":username})
    dict_sent={'mails':sent}
    dict_sent_json=json.dumps(dict_sent)
    return dict_sent_json        