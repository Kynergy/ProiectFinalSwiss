import tkinter as tk
import requests
import json
import pprint
from flask import Flask, request
import time


# Creating the app
root = tk.Tk()
# Creating the app title
root.title('API Exchange Platform')









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


def Market_for_coins(id): #parameter to be set - id

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




# All_exchanges()

def fetch_exchange(id):

    fetch = " https://api.coinlore.net/api/exchange/"
    payload = {'id': id}
    response = requests.get(fetch, params=payload)
    data = response.json()
    # print(type(data))
    # pprint.pprint(data)
    # Iterate over all key-value pairs of dict argument

    dictionary = data.get('pairs')
    print (dictionary)
    for element in dictionary:
        volume="{:,}".format(round(int(element.get('volume'))))
        print ("Currency Code:",element.get('base'),"|", "Currency exchange:", element.get('quote'),"|", "Tranzactions volume:",volume, "Price/UOM:", "{:,}".format(float("{:.2f}".format(float(element.get('price_usd'))))))

# Loop through all key-value pairs of a nested dictionary
# for pair in fetch_exchange("pairs"):
#     print(pair)

    # print(key[0:])
    # print(value)
    # print(value)
    # for i in value:
    # print(i)

    return

### ---------------- Defining the additional windows functions ---------------- ###



def open_window_1():
    window_1 = tk.Toplevel()
    window_1.title('Fetch Exchange')
    window_1_label = tk.Label(window_1, text="Fetch Exchange")
    window_1_label.grid(row=0, column=0, columnspan=2, padx=15, pady=15)


def new_window_2():
    return
# fetch_exchange(3)

# Creating the main window title:

main_window_label=tk.Label(text="--Cryptocurrencies--")
main_window_label.grid(row=0, columnspan=3)


### ---------------- Defining the buttons in the main window ---------------- ###

#--- Market Info button creation --- #
market_info_button_text = tk.StringVar()
market_info_button = tk.Button(root,textvariable=market_info_button_text, command=global_api)
market_info_button_text.set("Market Info")

#--- Coin Info button creation ---#
coin_info_button_text = tk.StringVar()
coin_info_button = tk.Button(root,textvariable=coin_info_button_text,command = All_Coins)
coin_info_button_text.set("Coin Info")

#--- Coin Market button creation ---#
coin_market_button_text = tk.StringVar()
coin_market_button = tk.Button(root,textvariable=coin_market_button_text, command = lambda: Market_for_coins(5))
coin_market_button_text.set("Coin Markets")

#--- Fetch Exchange Rates button creation ---#
fetch_exchange_button_text = tk.StringVar()
# fetch_exchange_button = tk.Button(root,textvariable=fetch_exchange_button_text, command = open_window_1)    ## Command to be changed into a new function that opens a new window
fetch_exchange_button = tk.Button(root,textvariable=fetch_exchange_button_text, command = lambda: fetch_exchange(5))
fetch_exchange_button_text.set("Exchange Rates")

#--- Help Button ---#
help_button_text= tk.StringVar()
help_button=tk.Button(root,textvariable=help_button_text)
help_button_text.set("Help")

#--- Quit Button ---#
quit_button_text= tk.StringVar()
quit_button=tk.Button(root,textvariable=quit_button_text,command=root.quit)
quit_button_text.set("Quit")

### ---------------- Adding the button to the main window ---------------- ###

#--- Market Info button adding --- #
market_info_button.grid(row=1, column=0, padx=10, pady=10)

#--- Coin Info button adding --- #
coin_info_button.grid(row=2, column=0, padx=10, pady=10)

#--- Coin Market button adding --- #
coin_market_button.grid(row=3, column=0, padx=10, pady=10)

#--- Fetch Exchange Rates button adding --- #
fetch_exchange_button.grid(row=4, column=0, padx=10, pady=10)

#--- Fetch Exchange Rates button adding --- #
help_button.grid(row=5, column=0, padx=10, pady=10)

#--- Fetch Exchange Rates button adding --- #
quit_button.grid(row=5, column=1, padx=10, pady=10)

### ---------------- Defining the main window Text Box ----------------###

text_box = tk.Text(root, height=20, width=60)

### ---------------- Adding the main window Text Box ----------------###

text_box.grid(row=1, column=1, rowspan=4, padx=10, pady=10)


root.mainloop()