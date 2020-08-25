import requests

parameters = {"lat":40.71, "lon":-74}

# Make a get request to get the latest position of the international space station from the opennotify api.
# needs 2 params for this particular json request
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
response2 = requests.get("http://api.open-notify.org/astros.json")

data = response.json()
# data2 = response2.json()

# Print the status code of the response.
print(type(data))
print(data)

# print(data2["number"])
# print(response.headers["content-type"])
