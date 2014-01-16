#!/usr/bin/env python3

import urllib3;
import sys;

if len(sys.argv) < 2:
    print("Usage: %s $login $count=100" % sys.argv[0])
    sys.exit(1);

count = 100
login = sys.argv[1]
if len(sys.argv) > 2:
    count = int(sys.argv[2])
url = 'https://docs.google.com/forms/d/1jyFjBJ_0Qq8Rzjh5cMHAuDiqo3floADMNK3B-Tk0X4s/formResponse'

fields = {
        'entry.1184760385': login
        }

for i in range(0, count):

    http = urllib3.PoolManager()
    r = http.request('POST', url, fields)
    print("Count: %d" % (i + 1))
