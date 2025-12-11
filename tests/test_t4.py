import requests
import json

# api-endpoint
URL = "https://jsonplaceholder.typicode.com/todos/"

# location given here
location = "delhi technological university"

# defining a params dict for the parameters to be sent to the API
PARAMS = {'address':location}

# sending get request and saving the response as response object
response = requests.get(url = URL)

# data is in a list of dictionaries
data=response.json()

# data is a list since response is a list
for i in range(len(data)):
    print(data[i]['userId']) # prints all userId



# extracting latitude, longitude and formatted address
# of the first matching location
# latitude = data['results'][0]['geometry']['location']['lat']
# longitude = data['results'][0]['geometry']['location']['lng']
# formatted_address = data['results'][0]['formatted_address']
#
# # printing the output
# print("Latitude:%s\nLongitude:%s\nFormatted Address:%s"
#     %(latitude, longitude,formatted_address))