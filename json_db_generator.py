#!/usr/bin/python3.6

from sys import exit
from sys import argv
import random
import time
import json

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

nb_entries = 0

def generate_entrie():
    return random.choice(arr_prefix) + random.choice(arr_suffix) + random.choice(arr_end)

def generate_random_object_id():
    millis = int(round(time.time() * 1000))
    timestamp = str(format((int(millis) | 0), 'x'))
    return timestamp + ''.join((lambda v: str(format(int(random.randint(0, 16) | 0), 'x')).lower())(x) for x in range(13))

def generate_dic_entry_without_company():
    return {
        "_id"       :   generate_random_object_id()[0:23],
        "name"      :   generate_entrie(),
        "address"   :   generate_entrie(),
        "about"     :   generate_entrie(),
        "email"     :   generate_entrie(),
        "company"   :   generate_random_object_id()[0:23]
    }

def generate_dic_entry_with_company():
    return {
        "_id"       :   generate_random_object_id()[0:23],
        "name"      :   generate_entrie(),
        "address"   :   generate_entrie(),
        "about"     :   generate_entrie(),
        "email"     :   generate_entrie(),
        "company"   :   {
            "name"      :   generate_entrie(),
            "address"   :   generate_entrie(),
            "about"     :   generate_entrie(),
            "financial" :   generate_entrie(),
            "ceo"       :   generate_entrie()
        }
    }

def generate_dic_company(id_company):
    return {
        "_id"           :   id_company,
        "name"          :   generate_entrie(),
        "address"       :   generate_entrie(),
        "about"         :   generate_entrie(),
        "financial"     :   generate_entrie(),
        "ceo"           :   generate_entrie()
    }

def main():
    output = []
    output_company = []

    for i in range(0, nb_entries):
        entry = generate_dic_entry_with_company() if argv[3] == "with_company" else generate_dic_entry_without_company()
        if argv[3] == "without_company":
            entry_company = generate_dic_company(entry['company'])
            output_company.append(entry_company)
        output.append(entry)

    print("Generating offer file:", argv[1], "...")
    with open(argv[1], 'w') as f:
        json.dump(output, f)
    print("done.")

    if argv[3] == "without_company":
        company_file = argv[1][:-5] + '_company.json'
        print("Generating on company file:", company_file, "...")
        with open(company_file, 'w') as ofs:
            json.dump(output_company, ofs)
        print("done.")

if __name__ == "__main__":
    if not len(argv) == 4:
        print("Usage:", argv[0], "<output_file_name> <object_nbr> <with_company | without_company>")
        exit(0)
    nb_entries = int(argv[2])
    main()
