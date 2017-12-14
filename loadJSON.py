#!/usr/bin/env python3

import urllib.request, json
with urllib.request.urlopen("https://data.public.lu/api/1/organizations/") as url:
    data = json.loads(url.read().decode())
    print(data)
