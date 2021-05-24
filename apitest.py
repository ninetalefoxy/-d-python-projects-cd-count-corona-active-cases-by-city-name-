import requests

url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api_india"

headers = {
    'x-rapidapi-key': "59686e2e15msh971e24501f143b7p1c370ejsn95b8187138f7",
    'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()

def search_by_city(city_name):
    for each in response['state_wise']:
        for city in response['state_wise'][each]['district']:
            if city == city_name:
                return city,response['state_wise'][each]['district'][city]['active']

flag = 1

while flag!=0:
    citi = input("Enter city ")
    if citi == '0':
        break
    else:
        cases = search_by_city(citi)
        print(f'{citi} cases are {cases[1]}')

        