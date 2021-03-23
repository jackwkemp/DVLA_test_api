import requests
import json

url = "https://uat.driver-vehicle-licensing.api.gov.uk/vehicle-enquiry/v1/vehicles"

headers = {'Content-Type': 'application/json',
           'Accept': 'application/json',
           'x-api-key': 'INSERT API KEY HERE',
           'X-Correlation-Id': 'INSERT COMPANY NAME HERE', "Accept-Charset": "UTF-8"
           }

response = requests.post(url, data='{"registrationNumber": "INSERT REG NUMBER HERE"}', headers=headers)

data = response.json()

with open('data.json', 'w') as f:
    json.dump(data, f)

print("Vehicle Registration Number:")
print(data["registrationNumber"])
print("Vehicle Make:")
print(data["make"])
print("Vehicle Colour:")
print(data["colour"])
print("MOT Expiry Date:")
print(data["motExpiryDate"])
