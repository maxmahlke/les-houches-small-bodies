#!/usr/bin/env python

import requests
import json
import pandas as pd
from astropy.coordinates import Angle


ep = "2022-06-21T00:00:00"
ra = "07h08m00"
dec = "+26d34m00"
observer = "500"

# Service URL
url = "http://vo.imcce.fr/webservices/skybot/skybotconesearch_query.php?"

# Query parameters
params = {
    "-ep": ep,
    "-ra": Angle(ra).degree,
    "-dec": Angle(dec).degree,
    "-sr": 15 / 60,
    "-mime": "text",
    "-output": "all",
    "-loc": observer,
    "-tscale": "UTC",
}


# -------------------------------------------------------------------------------
# Version 1: Do not write a file
# Execute query
try:
    r = requests.post(url, params=params, timeout=2000)
except requests.exceptions.ReadTimeout:
    print("Time out")


# Find columns header
inlist = r.text.split("\n")[2]
header = inlist.split("|")

# Convert result in pandas DataGrame
inlist = r.text.split("\n")[3:]
data = [line.split("|") for line in inlist]

data = pd.DataFrame(data)
data.columns = header
data.columns = data.columns.str.strip()

# -------------------------------------------------------------------------------
# Version 2: Write a file
# Execute query
try:
    r = requests.post(url, params=params, timeout=2000)
except requests.exceptions.ReadTimeout:
    print("Time out")

# Write results
with open("response.txt", "w") as f:
    f.write(r.text)

# Read in pandas DataFrame
data = pd.read_csv("response.txt", sep="|", skiprows=2)
data.columns = data.columns.str.strip()
print(data.head())
