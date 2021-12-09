from urllib.request import urlopen
import json

def get_flight_information_utils():
    url = 'https://raw.githubusercontent.com/Skyscanner/full-stack-recruitment-test/main/public/flights.json'
    serialized_data = urlopen(url).read()
    data = json.loads(serialized_data)
    return data