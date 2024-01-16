import os

import sys
import tarfile
from io import StringIO
import gzip



tar_file_path = sys.argv[1]
plddt_json_path = sys.argv[2]

def plddt_of_pdb(content):
    plddts = []
    latest_aa_num = 0
    for line in filelines:
        if line[:4] =="ATOM" :
            res_num,plddt = int(line[22:26]), float(line[60:66])
            if res_num != latest_aa_num:
                plddts.append(plddt)
            latest_aa_num = res_num
    return plddts




tfile = tarfile.open(tar_file_path, 'r|')
json_file = open(plddt_json, "w")

json_file.write("{\n")
for i,t in enumerate(tfile):
    f = gzip.open(tfile.extractfile(t), 'rt')
    seed_id = t.get_info()['name'].split("-")[1]  #####adjust it
    content = f.readlines()
    plddt_seed = plddt_of_pdb(content)
    if i!=0:
        json_file.write(",")
    json_file.write("\"" + seed_id + "\":" + str(plddt_seed) + "\n")
json_file.write("}\n")
tfile.close()
json_file.close()
