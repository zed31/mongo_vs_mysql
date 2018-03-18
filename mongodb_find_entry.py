#!/usr/bin/python3.6

from pymongo import MongoClient
from sys import argv
import time
import json

client = MongoClient('localhost', 27017)
db = client['bench_test_nonrelational']
offersCollection = db['collection']['offers']

start = time.time()

cursor = offersCollection.find()

end = time.time()

print("Total duration: ", end - start)