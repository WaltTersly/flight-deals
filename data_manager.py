import requests
from pprint import pprint

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/ebf0e5596df83f5c88b9131925791403/flightDeals/prices"
SHEETY_USERS_ENDPOINT  = "https://api.sheety.co/ebf0e5596df83f5c88b9131925791403/flightDeals/users"

class DataManager:
    

    def __init__(self):
        self.data_destination = {}
    
    def get_destination_data(self):
        response = requests.get(url = SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.data_destination = data["prices"]
        # pprint(data)

        return self.data_destination
    
    def update_destination_codes(self):
        for city in self.data_destination:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url = f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json = new_data
            )
            print(response.text)
    
    def get_customer_emails(self):
        customers_endpoint = SHEETY_USERS_ENDPOINT
        response = requests.get(url=customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data