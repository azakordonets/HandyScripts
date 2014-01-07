import string
import random
import urllib2
import json
import hashlib
import uuid
import csv

def generate_device_token(size=32, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for x in range(size))

def generate_unique_token():
	mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> i) & 0xff) for i in range(0,8*6,8)][::-1])
	salt = ''.join(random.choice(string.ascii_lowercase) for x in range(20))
	return hashlib.sha256(mac_address + salt).hexdigest()

r = urllib2.urlopen('http://pr-stg.coders.pro/api/v1/testing/unactivated-invites/?format=json&limit=10000')
result = json.load(r)
objects = result['objects']

tokensWriter = csv.writer(open('tokens.csv', 'wb'))
for el in objects : 
	tokensWriter.writerow([el['promotional_code'], generate_device_token(), generate_unique_token()])


# for el in objects : 
	# print el['promotional_code']