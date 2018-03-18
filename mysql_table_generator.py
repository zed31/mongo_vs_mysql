#!/usr/bin/python3

import MySQLdb
from sys import argv, exit
from random import choice

arr_prefix = [
  "sit",
  "eiusmod",
  "nulla",
  "tempor",
  "exercitation",
  "Lorem",
  "consectetur",
  "qui",
  "aute",
  "laborum",
  "culpa",
  "sunt",
  "sunt",
  "enim",
  "cupidatat",
  "ipsum",
  "nulla",
  "consectetur",
  "minim",
  "ipsum",
  "sunt",
  "ut",
  "qui",
  "fugiat",
  "culpa",
  "et",
  "aliqua",
  "veniam",
  "ipsum",
  "in",
  "occaecat",
  "excepteur",
  "eu",
  "est",
  "excepteur",
  "magna",
  "nisi",
  "duis",
  "cillum",
  "culpa",
  "et"
]

arr_suffix = [
  "sunt",
  "labore",
  "id",
  "sint",
  "aliqua",
  "commodo",
  "veniam",
  "nostrud",
  "voluptate",
  "dolore",
  "laborum",
  "est",
  "est",
  "in",
  "elit",
  "eu",
  "pariatur",
  "nulla",
  "laboris",
  "sunt",
  "nostrud",
  "reprehenderit",
  "commodo",
  "occaecat",
  "et",
  "ex",
  "in",
  "irure",
  "adipisicing",
  "reprehenderit",
  "excepteur",
  "duis",
  "in",
  "pariatur",
  "labore",
  "qui",
  "cillum",
  "eu",
  "laborum",
  "anim",
  "et",
  "officia",
  "velit",
  "irure",
  "ipsum",
  "ad",
  "labore"
]

arr_end = [
  "sint",
  "officia",
  "veniam",
  "veniam",
  "labore",
  "est",
  "pariatur",
  "non",
  "nulla",
  "consectetur",
  "officia",
  "exercitation",
  "mollit",
  "reprehenderit",
  "Lorem",
  "nulla",
  "aliqua",
  "aute",
  "incididunt",
  "Lorem",
  "veniam",
  "in",
  "consequat",
  "cupidatat",
  "culpa",
  "eiusmod",
  "sit",
  "amet",
  "ad",
  "fugiat",
  "ipsum",
  "labore",
  "anim",
  "magna",
  "enim",
  "non",
  "ea",
  "labore",
  "in",
  "duis",
  "qui",
  "ullamco",
  "Lorem",
  "cillum",
  "laborum",
  "consectetur",
  "esse",
  "excepteur",
  "eu"
]

company_table = "DROP TABLE IF EXISTS offer;\n\
DROP TABLE IF EXISTS company;\n\
CREATE TABLE company (\n\
    id int not null primary key,\n\
    name varchar(255),\n\
    address varchar(255),\n\
    about varchar(255),\n\
    financial varchar(255),\n\
    ceo varchar(255)\n\
);\n\
INSERT INTO company(id, name, address, about, financial, ceo) VALUES"

offer_table = "\
CREATE TABLE offer (\n\
    id int not null primary key,\n\
    name varchar(255),\n\
    address varchar(255),\n\
    about varchar(255),\n\
    email varchar(255),\n\
    company_fk_id int not null,\n\
    foreign key (company_fk_id) references company(id)\n\
);\n\
INSERT INTO offer(id, name, address, about, email, company_fk_id) VALUES"

def generate_offer(id, name, address, about, email, company_id):
    return "( " + str(id) + ", \"" + str(name) + "\", \"" + str(address) + "\", \"" + str(about) + "\", \"" + str(email) + "\", \"" + str(company_id) + "\" )"

def generate_company(id, name, address, about, financial, ceo):
    return "( " + str(id) + ", \"" + str(name) + "\", \"" + str(address) + "\", \"" + str(about) + "\", \"" + str(financial) + "\", \"" + str(ceo) + "\" )"

def compose():
    return choice(arr_prefix) + choice(arr_prefix) + choice(arr_end)

def main(nbr_entries, output):
    final_table = company_table + ''.join([generate_company(x, compose(), compose(), compose(), compose(), compose()) + ',' for x in range(0, nbr_entries + 1)])
    final_table = final_table[:-1] + ';\n'
    final_table += offer_table
    final_table = final_table + ''.join([generate_offer(x, compose(), compose(), compose(), compose(), x) + ',' for x in range(0, nbr_entries + 1)])
    final_table  = final_table[:-1] + ';\n'
    print(final_table)
    with open(output, 'w') as ofs:
        ofs.write(final_table)

if __name__=='__main__':
    if len(argv) != 3:
        print("Usage:", argv[0], "<NB_ENTRIES> <OUTPUT_FILE>")
        exit(0)
    
    main(int(argv[1]), argv[2])
