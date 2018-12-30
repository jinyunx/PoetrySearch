# -*- coding: utf-8 -*-
import sys
import os
import json

def load(src_name):
    with open(src_name) as json_file:
        data = json.load(json_file)
        return data

if len(sys.argv) != 3:
    print("Usage: " + sys.argv[0] + " src_dir dst_dir")
    exit(0)

src_dir = sys.argv[1]
if src_dir[len(src_dir) - 1] != '/':
    src_dir += '/'

src_list = os.listdir(src_dir)

if len(src_list) == 0:
    print("There is no file in " + sys.argv[1])
    exit(0)

dst_dir = sys.argv[2]
if dst_dir[len(dst_dir) - 1] != '/':
    dst_dir += '/'
dst_file = open(dst_dir + "bulk.poetry.json", 'w')

for src_name in src_list:
    data_list = load(src_dir + src_name)
    for data in data_list:
        if "paragraphs" not in data.keys():
            continue
        data.pop("strains")
        dst_file.write('{ "index":{}}\n')
        dst_file.write(json.dumps(data, ensure_ascii=False, encoding='utf-8').encode('utf8'))
        dst_file.write("\n")
