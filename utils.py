import csv
import requests
import apis


def clear_screen():
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def save_to_csv(id):
    url = apis.base_url + "/?id="
    response = requests.request("GET", url, data={})
    myjson = response.json()
    ourdata = []
    csvheader = ['Name', 'Price-USD', 'Volume']

    for x in myjson['pairs']:
        listing = [x['base'], x['price_usd'], x['volume']]
        ourdata.append(listing)
    print(ourdata)

    with open("name.csv", 'w', encoding='UTF8', newline='', errors="ignore") as f:
        writer = csv.writer(f)
        writer.writerow(csvheader)
        writer.writerows(ourdata)
    print("done")
