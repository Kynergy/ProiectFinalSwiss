import csv
import requests

import apis


# from apis import *


def visualize():
    pass


# grafic


def clear_screen():
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


# list = []
# list = apis.all_exchanges(2)
# unique_list = []
# for i in list:
#     if i not in unique_list:
#         unique_list.append(i)
# for i in unique_list:
# print (apis.base_url)
def save_to_csv(id):
    url = apis.base_url + "/?id=" + id
    response = requests.request("GET", url, data={})
    myjson = response.json()
    # pprint.pprint(myjson)
    ourdata = []
    csvheader = ['Name', 'Price-USD', 'Volume']

    for x in myjson['pairs']:
        listing = [x['base'], x['price_usd'], x['volume']]
        ourdata.append(listing)
    print(ourdata)

    with open("name.csv", 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(csvheader)
        writer.writerows(ourdata)
    print("done")

# print()
