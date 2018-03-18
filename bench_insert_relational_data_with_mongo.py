#!/usr/bin/python3.6

from pymongo import MongoClient
import time
import json
from sys import argv
from sys import exit

def main():
    client = MongoClient('localhost', 27017)
    db = client['bench_test_relational']
    offersCollection = db['collection']['huge_offers']
    companyCollection = db['collection']['huge_companies']

    dataOffer = json.load(open(argv[1]))
    dataCompany = json.load(open(argv[2]))

    start = time.time()

    offersCollection.insert_many(dataOffer)
    companyCollection.insert_many(dataCompany)

    end = time.time()

    print("Duration for relational:", end - start)

if __name__=="__main__":
    if not len(argv) == 3:
        print("Usage:", argv[0], "<json_offers>", "<json_companies>")
        exit(0) 
    main()
    exit(1)