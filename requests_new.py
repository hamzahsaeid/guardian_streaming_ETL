import requests

def get_data():
    api_response = requests.get("https://api.github.com")
    
    # data = api_response.json()

    # results = data.get('response', {}).get('results', [])

    print(api_response.headers['server'])
    # print('text response >>>>>', requests.get("https://api.github.com").text )
    # print('json response >>>>>', api_response.json())

get_data() 