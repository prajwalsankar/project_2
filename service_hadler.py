import subprocess
import sys
import time
from pprint import pprint

# step1
def run_command(cmd):
    try:
        resp = subprocess.check_output(cmd)
        resp = resp.decode('utf-8')
        #print(resp)
        return resp
    except Exception as e:
        print(f"Unable to run the command: {cmd} and Error: {str(e)}")

def get_proc_dict(resp):
    lines = resp.split("\n")
    d = {}
    for line in lines[3:]:
        if len(line) == 0:
            continue
        words = line.split("  ")
        words_ = []
        for word in words:
            if len(word) !=0:
                words_.append(word)
        pname = words_[0]
        pid = words_[1].split()[0]
        mem = words[-1]
        d[pid] = [pname, mem]
    return d
