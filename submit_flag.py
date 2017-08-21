#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

def submit(flag, token):
    failed = '"status":"error"'
    data = {
        "flag":flag,
        "token":token
    }
    print "[+] Submiting flag : [%s]" % (data)
    response = requests.post("http://172.16.200.3:9000/submit_flag/", data=data)
    content = response.content
    print "[+] Content : %s" % (content)
    if failed in content:
        print "[-] failed!"
        return False
    else:
        print "[+] Success!"
        return True
