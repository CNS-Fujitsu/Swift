import requests
import json

# Docs:
# http://developer.openstack.org/api-ref/object-storage/index.html

projectid = '3cef1071f8ff432989f18aa14ce3cc66'
identity_url = 'https://identity.uk-1.cloud.global.fujitsu.com/v3/auth/tokens'
swift_url = 'https://objectstorage.uk-1.cloud.global.fujitsu.com/v1/AUTH_'+projectid

k5user = 'USER'
k5pwd = 'PASS'

# Get Token 
response = requests.post(identity_url, headers={'Content-Type': 'application/json','Accept':'application/json'}, json={"auth":{"identity":{"methods":["password"],"password":{"user":{"domain":{"name":"YssmW1yI"}, "name": k5user, "password": k5pwd}}}, "scope": { "project": {"id":"3cef1071f8ff432989f18aa14ce3cc66"}}}})
token = response.headers['X-Subject-Token']
print(token)

# Get container list
response = requests.get(swift_url, headers={'Content-Type': 'application/json','X-Auth-Token': token, 'Accept':'application/json'})
print(response.json())

# Create container
response = requests.put(swift_url+"/drortest", headers={'X-Auth-Token': token})
#print(response)

# Put file in container
response = requests.put(swift_url+"/drortest/index.html", headers={'X-Auth-Token': token, 'Content-Type': 'text/html'}, data="hello world!")
#print(response)

# Make world readable and set website index
response = requests.post(swift_url+"/drortest", headers={'X-Auth-Token': token, 'X-Container-Read': '.r:*', 'X-Container-Meta-Web-Index': 'index.html'})
#print(response)

# Get container contents
response = requests.get(swift_url+"/drortest", headers={'X-Auth-Token': token})
#print(response.headers)
#print(response.text)


# Delete file from container
response = requests.delete(swift_url+"/drortest/index.html", headers={'X-Auth-Token': token})
#print(response)

# Delete container
response = requests.delete(swift_url+"/drortest", headers={'X-Auth-Token': token})
#print(response)

