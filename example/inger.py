#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Felix Lehmann
Examples:
    python3 inger.py
    python3 inger.py v1 google adwords v201705 deprecated
"""
import json, requests, sys

def load_data():
    url = 'http://inger.io'
    inger_version="v1"
    vendor="facebook"
    service="graph"
    version="v2.10"
    method="deprecated"
    separator="/"

    if(len(sys.argv)==6):
        inger_version=sys.argv[1]
        vendor=sys.argv[2]
        service=sys.argv[3]
        version=sys.argv[4]
        method=sys.argv[5]

    full_url=url+separator+inger_version+separator+vendor+separator+service+separator+version+separator+method

    response = requests.get(full_url)
    if(response.ok):
        print(json.dumps(json.loads(response.content), indent=4, sort_keys=True))
    else:
        response.raise_for_status()

load_data()