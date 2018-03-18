#!/usr/bin/python3.6

from pymongo import MongoClient
from sys import argv
import time
import re
import json

client = MongoClient('localhost', 27017)
db = client['bench_test_nonrelational']
offersCollection = db['collection']['offers']

print("Starting command:", "find()")

start = time.time()
cursor = offersCollection.find()
end = time.time()

print("Total duration: ", end - start)

pattern = re.compile('^a.*')

print("Starting command:", "find({'name' : pattern})")

start = time.time()
cursor = offersCollection.find({'name' : pattern})
end = time.time()

print("Total duration: ", end - start)

print("Starting command:", "find({'company.name' : pattern})")

start = time.time()
cursor = offersCollection.find({'company.name' : pattern})
end = time.time()

print("Total duration: ", end - start)

print("Starting command:", "find({\'$or\' : [ {\'company.name\' : pattern}, {\'name\' : pattern} ]})")

start = time.time()
cursor = offersCollection.find({'$or' : [ {'company.name' : pattern}, {'name' : pattern} ]})
end = time.time()

print("Total duration: ", end - start)

print("Starting command:", "find({\'$and\' : [ {\'company.name\' : pattern}, {\'name\' : pattern} ]})")

start = time.time()
cursor = offersCollection.find({'$and' : [ {'company.name' : pattern}, {'name' : pattern} ]})
end = time.time()

print("Total duration: ", end - start)