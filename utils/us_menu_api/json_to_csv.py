import pandas as pd
import json
import csv

with open('data/restaurant_ids.csv','r') as csv_file:
    lines = csv_file.readlines()

restaurant_ids = []
for line in lines:
    data = line.split(',')
    restaurant_ids.append(data[0])


list_of_restaurants = []
list_of_menu_items = []

menu_id = 1
#clean json
for id in restaurant_ids:
    json_path = "json_clean/" + str(id) + "_data.json"

    json_val = json.load(open(json_path))

    df = json_val['result']

    for key in df['data']:
        menu_data ={}
        menu_data['menu_id'] = menu_id
        menu_data['restaurant_id'] = key['restaurant_id']
        menu_data['menu_item_name'] = key['menu_item_name']
        menu_data['subsection'] = key['subsection']

        try:
            price = key['menu_item_pricing'][0]['price']
        except Exception as e:
            price = None

        menu_data['price'] = price
        menu_id += 1
        list_of_menu_items.append(menu_data)

    # # Restaurant Data
    # restaurant_data = {}
    #
    # try:
    #     data = df['data'][0]
    # except Exception as e:
    #     continue
    # restaurant_data['restaurant_id'] = data['restaurant_id']
    # restaurant_data['restaurant_name'] = data['restaurant_name']
    # restaurant_data['price_range'] = data['price_range']
    # restaurant_data['street'] = data['address']['street']
    # restaurant_data['city'] = data['address']['city']
    # restaurant_data['cuisines'] = data['cuisines']
    # list_of_restaurants.append(restaurant_data)



csv_path = "data/menu_items.csv"
restaurant_path = "data/restaurants.csv"

def tocsv(path, list):
    df = pd.DataFrame(list)
    df.reset_index(drop=True, inplace=True)
    df.to_csv(path, index=False)


tocsv(csv_path, list_of_menu_items)
# tocsv(restaurant_path, list_of_restaurants)
