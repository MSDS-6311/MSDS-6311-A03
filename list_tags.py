#!/usr/bin/python3
import re 

with open('/home/shared/Tweets.csv', 'rt') as f:
    text = f.read()

for tag in re.findall(r'#[a-z]+', text, re.IGNORECASE):
    print(tag)
