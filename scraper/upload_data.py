from dotenv import load_dotenv
import pymongo
import certifi
import os

load_dotenv()
url = os.getenv('MONGO_URL')
dbclient = pymongo.MongoClient(url, tlsCAFile=certifi.where())
coursedb = dbclient["courses"]

def serialize_one_course(crude_course):
    toBeInserted = crude_course.__dict__
    coursedb["coursesStr"].insert_one(toBeInserted)

def serialize_multiple_courses(locrude_courses):
    for cc in locrude_courses:
        serialize_one_course(cc)
