"""
prize.json contains all nobel prize winners, as well as the year in which they won the prize and what they won the prize for.
http://api.nobelprize.org/v1/prize.json
To import the data, we first opened the json and read in the lines to a list. Then we used the json library to convert the json strings to dictionaries and inserted them one by one into the database.
"""
import json
from pymongo import MongoClient


client = MongoClient()
db = client.teamName
collection = db.events
collection.remove()
#if(collection.count() == 0):
client = MongoClient()
db = client.teamName
collection = db.events
collection.delete_many({})


with open("./nobel/prize.json", "r") as file:
    content = json.load(file)
    for line in content['prizes']:
        # print('\n')
        # print(line["category"])
        newline = {"year": line["year"], "category": line["category"]}
        laureates = {}
        if "laureates" in line:
            for laureate in line['laureates']:
                if 'surname' in laureates:
                    laureates[laureate['id']] = {'firstname': laureate['firstname'], 'surname': laureate['surname'], 'motivation': laureate['motivation']}
                else:
                    laureates[laureate['id']] = {'firstname': laureate['firstname'], 'motivation': laureate['motivation']}
            newline['laureates'] = laureates
        #print(newline)
        # print('\n')
        collection.insert_one(newline)
# for document in collection.find({"category": "chemistry"}):
#     print(document)
#     print("\n\n")
def printHi():
    print("Hello, nobel")


def findTopic(topic):
    topic = topic.lower()
    data = collection.find({"category": topic})
    #print(data)
    hello = []
    for thing in data:
        for item in thing:
            if (item != "laureates" and item!="_id"):
                hello.append("{} : {}".format(item, thing[item]))
            elif(item!="_id"):
                count = 0
                for piece in thing[item]:
                    infoDict = thing[item][piece]
                    if(count == 0):
                        hello.append("reason: " + infoDict[u'motivation'])
                    hello.append("name: " + infoDict['firstname'])
                    count+=1
        hello.append("\n")
    return hello

def findYear(year):
    data = collection.find({"year": year})
    # print(data[0])
    hello = []
    for thing in data:
        for item in thing:
            if (item != "laureates" and item!="_id"):
                hello.append("{} : {}".format(item, thing[item]))
            elif(item!="_id"):
                count = 0
                for piece in thing[item]:
                    infoDict = thing[item][piece]
                    if(count == 0):
                        hello.append("reason: " + infoDict[u'motivation'])
                    hello.append("name: " + infoDict['firstname'])
                    count+=1
        hello.append("\n")
    return hello

#findTopic("chemistry")
# findYear("1945")
