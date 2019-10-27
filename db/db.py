from pymongo import MongoClient
import config.config as core_config

client = MongoClient(core_config.DBHOST, core_config.BDPORT)
db = client.bot1
collection = db.users


def add_topic(topic: str, text: str) -> None:
    collection.insert_one(
        {
            str(topic): str(text)
        }
    )


def show_topic(topic: str):
    print(topic)
    for i in list(collection.find({})):
        if i.get(topic) is not None:
            return i.get(topic)


def show_all_topic():
    topics = list(collection.find({}))
    a = []
    for topic in topics:
        topic = dict(topic)
        for key in topic.keys():
            if key == '_id':
                continue
            a.append(key)

    return '\n'.join(a)
