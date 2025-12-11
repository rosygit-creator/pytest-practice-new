import requests
import json
import pprint

# api-endpoint
BASE_URL = "https://reqres.in/api/users/1"

headers={'x-api-key':'reqres_1758465aee6743278e83aeb428580577'}


# location given here
# location = "delhi technological university"
#
# # defining a params dict for the parameters to be sent to the API
# PARAMS = {'address':location}

# sending get request and saving the response as response object
response = requests.get(BASE_URL, headers=headers)

# pprint.pprint(dict(response.headers),indent=5) # indent adds space on leftside

assert 'Content-Type' in response.headers

for k, v in response.headers.items():
    if k=='Content-Type':
        print(v) # application/json; charset=utf-8

# data is in a list of dictionaries
temp_data=response.json()

# pprint.pprint(temp_data) # this works

# pretty print data
# pretty_data=json.dumps(temp_data, indent=4)

# print(pretty_data)

assert temp_data['data']['email']=="george.bluth@reqres.in"
assert temp_data['support']['url']=="https://contentcaddy.io?utm_source=reqres&utm_medium=json&utm_campaign=referral"
assert temp_data['_meta']['docs_url']=='https://reqres.in'

# verify the key :template_gallery contains templates in value

actual_value=temp_data['_meta']['template_gallery']
# print(temp_data['_meta']['template_gallery'])
assert "templates" in actual_value

len_features=temp_data['_meta']['features']
# print(len(len_features))
assert len(len_features)==4

# verify value is not null
assert temp_data['support']['url'] is not None, f"did not expect"

# verify string is not empty
assert temp_data['support']['url']!=""

# find all keys of support
# print(temp_data['support'])


for k,v in temp_data['support'].items():
    # print(k)
    if k=="url":
        print(v)

for k, v in temp_data['_meta'].items():
            # print(k)
    if k == "features":
        print(v)

# extracting latitude, longitude and formatted address
# of the first matching location
# latitude = data['results'][0]['geometry']['location']['lat']
# longitude = data['results'][0]['geometry']['location']['lng']
# formatted_address = data['results'][0]['formatted_address']
#
# # printing the output
# print("Latitude:%s\nLongitude:%s\nFormatted Address:%s"
#     %(latitude, longitude,formatted_address))