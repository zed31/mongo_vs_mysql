#!/usr/bin/python3

import MySQLdb
from sys import argv, exit
import time

db = MySQLdb.connect("localhost", "root", "lb/n2dcxP3/x", "test")


def main(sql_file_name):
    cursor = db.cursor()
    with open(sql_file_name, 'r') as ifs:
        file_content = ifs.read()
        start = time.time()
        cursor.execute(file_content)
        end = time.time()
        print("Total duration:", end - start)
        cursor.close()


if __name__=="__main__":
    if len(argv) != 2:
        print("usage:", argv[0], "<SQL_FILE>")
        exit(0)
    main(argv[1])