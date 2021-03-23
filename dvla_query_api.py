import json
import requests


def main():

    a = "{"
    b = '"'
    c = str("registrationNumber")
    d = '"'
    e = ":"
    f = " "
    g = '"'
    query = input("Enter a vehicle registration: ")
    h = '"'
    i = "}"

    result = (a + b + c + d + e + f + g + query + h + i)

    url = "https://uat.driver-vehicle-licensing.api.gov.uk/vehicle-enquiry/v1/vehicles"

    headers = {'Content-Type': 'application/json',
               'Accept': 'application/json',
               'x-api-key': 'INSERT API KEY HERE',
               'X-Correlation-Id': 'INSERT COMPANY NAME HERE', "Accept-Charset": "UTF-8"
               }

    response = requests.post(url, data=str(result), headers=headers)

    data = response.json()
    # print(data)

    # with open('data.json', 'w') as f:
    #     json.dump(data, f)

    print("Vehicle Registration Number:")
    print(data["registrationNumber"])
    print("Vehicle Make:")
    print(data["make"])
    # print("Vehicle Model:")
    # print(data["model"]) no model in this data set
    print("Vehicle Colour:")
    print(data["colour"])
    print("MOT Expiry Date:")
    print(data["motExpiryDate"])


main()
