import requests
import json
import pprint
from flask import Flask, request
import time


def global_api():
    api_global = "https://api.coinlore.net/api/global/"
    response = requests.get(api_global)
    dictionary = response.json()

    # Changing the response JSON to a dictionary

    coins_count = dictionary[0]['coins_count']
    active_markets = dictionary[0]['active_markets']
    print(f"The total number of coins is {coins_count}")
    print(f"The number of active markets for cryptocurrencies are: {active_markets}")


# global_api()

def All_Coins():
    coin_list = []

    # How to set parameters to the URL API Request

    ploads = {'start': 100, 'limit': 100}
    ploads2 = {'start': 200, 'limit': 100}
    # Sending the request with the parameters
    api_all1 = "https://api.coinlore.net/api/tickers/"

    r = requests.get(api_all1, params=ploads)
    dictionary = r.json()
    time.sleep(1)
    r2 = requests.get(api_all1)
    dictionary2 = r2.json()
    time.sleep(1)
    r3 = requests.get(api_all1, params=ploads2)
    dictionary3 = r3.json()

    coin_list.append(dictionary["data"])
    coin_list.append(dictionary2["data"])
    coin_list.append(dictionary3["data"])
    variabila = coin_list[0] + coin_list[1] + coin_list[2]
    j = 0
    for i in variabila:
        j += 1
        print(j, i["id"], i["symbol"], i["name"], i["rank"], i["price_usd"], i["percent_change_24h"])
        # print(f"The Id of the currency is: {i[0],'id'}")


# All_Coins()


def Market_for_coins(id):
    market = "https://api.coinlore.net/api/coin/markets/"
    payload = {'id': id}
    response = requests.get(market, params=payload)
    dictionary = response.json()
    # pprint.pprint(dictionary)
    for i in dictionary:
        print(i["name"], i["base"], i["price_usd"], i["quote"])


# Market_for_coins(90)

def All_exchanges():
    exchanges = "https://api.coinlore.net/api/exchanges/"
    response = requests.get(exchanges)
    json_data = response.json()
    print(type(json_data))
    # pprint.pprint(json_data)
    # dictionary = json.loads(str(json_data))
    exchange_list = []
    for i, j in json_data.items():
        for key in j:
            # print(j["volume_usd_adj"], j["url"])
            exchange_list.append(f"{j['volume_usd_adj']} : {j['url']} : {j['country']}")
            # exchange_list.append(j["url"])
    print(exchange_list)


All_exchanges()
