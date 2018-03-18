#!/usr/bin/python3

import MySQLdb
from sys import argv, exit
import time

db = MySQLdb.connect("localhost", "root", "lb/n2dcxP3/x", "test")

request_info = [
    'SELECT * FROM offer;', 
    'SELECT * FROM company;', 
    'SELECT * FROM offer WHERE offer.id < 10;',
    'SELECT company.id, company.name FROM company;',
    'SELECT offer.id, offer.name, company.name FROM offer INNER JOIN company ON offer.company_fk_id = company.id;'
]

def main():
    cursor = db.cursor()
    start = time.time()
    for item in request_info:
        print("Executing command:", item)
        cursor.execute(item)
        end = time.time()
        print("Total duration:", end - start)
        r = cursor.fetchall()
        print("got:", len(r), "entries")
    cursor.close()


if __name__=="__main__":
    main()