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
    output_text = (f"The total number of coins is {coins_count}. \nThe number of active markets for cryptocurrencies are: {active_markets}")
    return output_text


def all_coins():
    """
    :goal: Provides all the coins
    :return: list of total coins of the market with their properties
    :rtype: list(str)
    """
    coin_list = []

    # Setting the parameters to the URL API Request

    ploads = {'start': 100, 'limit': 100}
    ploads2 = {'start': 200, 'limit': 100}
    # # Sending the request with the parameters
    api_all1 = f"{base_url}tickers/"
    response = {"data": [1] * 100}
    index = 0

    while len(response["data"]) == 100 and index <= 5:
        response = requests.get(api_all1, params={"limit": 100, "start": 100 * index}).json()

        time.sleep(1)
        index += 1
        coin_list += response["data"]
    variabila = ['Global markets:\n']
    for element in coin_list:
        price_usd=round(float(element['price_usd']),2)
        variabila.append([f"ID: {element['id']}\nSymbol: {element['symbol']}\nName:{element['name']}\nPrice USD: {price_usd}\n \n"])
    return variabila


def market_for_coins(id):  # parameter to be set - id
    """
    :goal: Provides all the coin markets
    :param id: the coin's id
    :type id: int
    """
    try:
        market = f"{base_url}coin/markets/"
        payload = {'id': id}
        response = requests.get(market, params=payload)
        dictionary = response.json()
        list=["Data for the selected url:\n"]
        for i in dictionary:
            if i["name"] == None or i["name"] == "Unnamed" or i["price_usd"] == None or i["quote"] == None:
                continue
            else:
                list.append(f"Name:{i['name']}\n   Base:{i['base']}\n   Price USD:{i['price_usd']}\n   Total:{i['quote']}\n \n")
        return list
    except:
        return ("No data for this specific API, please select a different one")

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
                result.append(f"{j['volume_usd_adj']} : {j['url']} : {j['country']}")


    elif type_of_return == 2:
        result = []
        for i, j in response.items():
            for key in j:
                result.append(f"{j['url']}")
    elif type_of_return == 3:
        result = {}
        for i, j in response.items():
            result[i] = f"{j['url']}"
    return (result)


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
    output = ["The details for the selected URL are:,\n"]
    dictionary = data.get('pairs')
    for element in dictionary:
        volume = "{:,}".format(round(int(element.get('volume'))))
        price_usd = round(float(element['price_usd']), 2)
        output.append(f"\n Currency Code: {element.get('base')} \n Currency Exchange: {element.get('quote')} \n Tranzactions volume: {volume} \n Price USD: {price_usd} \n \n")
    return output


