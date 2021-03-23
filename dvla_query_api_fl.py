from flask import Flask, render_template, request
import requests
import json



app = Flask(__name__)

url = "https://uat.driver-vehicle-licensing.api.gov.uk/vehicle-enquiry/v1/vehicles"

headers = {'Content-Type': 'application/json',
           'Accept': 'application/json',
           'x-api-key': 'INSERT API KEY HERE',
           'X-Correlation-Id': 'INSERT COMPANY NAME HERE', "Accept-Charset": "UTF-8"
           }

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/send', methods=['POST'])
def send():

    a = "{"
    b = '"'
    c = str("registrationNumber")
    d = '"'
    e = ":"
    f = " "
    g = '"'
    query = request.form['number']
    h = '"'
    i = "}"

    result = (a + b + c + d + e + f + g + query + h + i)

    response = requests.post(url, data=str(result), headers=headers)

    data = response.json()

    return data


if __name__ == '__main__':
    app.run(debug=True)
