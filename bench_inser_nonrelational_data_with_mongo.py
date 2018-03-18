#!/usr/bin/python3.6

from pymongo import MongoClient
from sys import argv
import time
import json

client = MongoClient('localhost', 27017)
db = client['bench_test_nonrelational']
offersCollection = db['collection']['offers']

data = json.load(open(argv[1]))

start = time.time()

offersCollection.insert_many(data)

end = time.time()

print("Total duration: ", end - start)