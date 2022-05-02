from dotenv import load_dotenv
import pymongo
import os

load_dotenv()
print(os.getenv('MONGO_PASSWORD'))
#dbclient = pymongo.MongoClient("mongodb+srv://admin:<password>@cluster0.qchop.mongodb.net/courseDB?retryWrites=true&w=majority")