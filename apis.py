import requests
import time

base_url = "https://api.coinlore.net/api/"


def global_api():
    """
    :goal: Returns the number of coins and markets
    :return: Total number of coins and active markets
    :rtype: str
    """

    api_global = requests.get(url=f"{base_url}global").json()
    coins_count = api_global[0]['coins_count']
    active_markets = api_global[0]['active_markets']
    print(f"The total number of coins is {coins_count}")
    print(f"The number of active markets for cryptocurrencies are: {active_markets}")
    output_text = (f"The total number of coins is {coins_count}. \nThe number of active markets for cryptocurrencies are: {active_markets}")

    # return (f"The total number of coins is {coins_count}",f"\nThe number of active markets for cryptocurrencies are: {active_markets}")
    return output_text


def all_coins():
    """
    :goal: Provides all the coins
    :return: list of total coins of the market with their properties
    :rtype: list(str)
    """
    coin_list = []

    # How to set parameters to the URL API Request

    ploads = {'start': 100, 'limit': 100}
    ploads2 = {'start': 200, 'limit': 100}
    # # Sending the request with the parameters
    # api_all1 = requests.get(url=f"{base_url}tickers/")
    api_all1 = f"{base_url}tickers/"
    response = {"data": [1] * 100}
    index = 0

    while len(response["data"]) == 100 and index <= 5:
        response = requests.get(api_all1, params={"limit": 100, "start": 100 * index}).json()

        time.sleep(1)
        index += 1
        coin_list += response["data"]

    variabila = []
    for element in coin_list:
        variabila.append(f"ID: {element['id']}, Symbol: {element['symbol']}, Name: {element['name']}, Price in USD: +{element['price_usd']}")
        variabila.append(f"Symbol: {element['symbol']}")
        variabila.append(f"Name: {element['name']}")
        variabila.append(f"Price in USD: {element['price_usd']}")

#     # variabila = variabila + coin_list[element]
#     #         j = 0
#     #         for i in variabila:
#     #              j += 1
#     #              print(j, i["id"], i["symbol"], i["name"], i["rank"], i["price_usd"], i["percent_change_24h"])
#     #              print(f"The Id of the currency is: {i[0],'id'}")
    return variabila


def market_for_coins(id):  # parameter to be set - id
    """
    :goal: Provides all the coin markets
    :param id: the coin's id
    :type id: int
    """

    market = f"{base_url}coin/markets/"
    payload = {'id': id}
    response = requests.get(market, params=payload)
    dictionary = response.json()
    # pprint.pprint(dictionary)
    for i in dictionary:
        print(i["name"], i["base"], i["price_usd"], i["quote"])
        print(type(dictionary))


def all_exchanges(type_of_return):
    """
    :goal: Returns different endpoints for exchange markets
    :param type_of_return: the endpoint
    :type type_of_return: str
    :return: dict(str: str)
    """


    exchanges = f'{base_url}exchanges/'
    response = requests.get(exchanges).json()

    if type_of_return == 1:
        result = []
        for i, j in response.items():
            for key in j:
                # print(j["volume_usd_adj"], j["url"])
                result.append(f"{j['volume_usd_adj']} : {j['url']} : {j['country']}")
                # exchange_list.append(j["url"])

    elif type_of_return == 2:
        result = []
        for i, j in response.items():
            for key in j:
                # print(j["volume_usd_adj"], j["url"])
                result.append(f"{j['url']}")
                # result[key] = f"{j['url']}"
    elif type_of_return == 3:
        result = {}
        for i, j in response.items():
            result[i] = f"{j['url']}"
            # result[f"{i['url']}"]=f"{j['url']}"
            # result[f"{i['id']}"]=f"{j['id']}"
    return (result)


# all_exchanges()
# #
def fetch_exchange(id):
    """Return list of tranzaction volume, currency exchange , code and price
    :param id: integer
    :return: list
    """
    fetch = f"{base_url}exchange/"
    payload = {'id': id}
    response = requests.get(fetch, params=payload)
    data = response.json()
    # Iterate over all key-value pairs of dict argument

    dictionary = data.get('pairs')
    for element in dictionary:
        volume = "{:,}".format(round(int(element.get('volume'))))
        print("Currency Code:", element.get('base'), "|", "Currency exchange:", element.get('quote'), "USDT", "|",
              "Tranzactions volume:", volume, '|'     "Price/UOM:",
              "{:,}".format(float("{:.2f}".format(float(element.get('price_usd'))))), 'USD')


    return dictionary
#
# fetch_exchange(90)
#
# #
