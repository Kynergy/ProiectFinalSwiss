import csv
import requests
import apis
import time
import plotly.graph_objects as go




def save_to_csv(url,name_of_csv,id):

    url = apis.base_url + url +str(id)
    response = requests.request("GET", url, data={})
    myjson = response.json()
    ourdata = []
    csvheader = ['Name', 'Price-USD', 'Volume']

    for x in myjson['pairs']:
        listing = [x['base'], x['price_usd'], x['volume']]
        ourdata.append(listing)
    # print(ourdata)
    date=time.strftime('%Y-%m-%d')
    with open(f'{name_of_csv}{date}.csv', 'w', encoding='UTF8', newline='', errors="ignore") as f:
        writer = csv.writer(f)
        writer.writerow(csvheader)
        writer.writerows(ourdata)

# def show_histogram():
#     with open(f'{name_of_csv}{date}.csv', 'w', encoding='UTF8', newline='', errors="ignore") as f:
#         f.readlines()
#
#
#
# fig = go.Figure(
#     data=[go.Bar(y=[dfdff], x=["text"])],
#     layout_plotly= "text"
#         )
# fig.show()
# fig.write_image("plot.png")




