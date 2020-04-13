import pandas as pd
import json
import csv

#-----------------------------------------------------------#
# Handles converting JSON data about restaurant to CSV files
#   - Menu Item Data
#   - Restaurant Data
#   - Category Data
#-----------------------------------------------------------#



##############################################
# Restaurant ID
##############################################
def get_restaurant_ids():

    with open('data/restaurant_ids.csv','r') as csv_file:
        lines = csv_file.readlines()

    restaurant_ids = []
    for line in lines:
        data = line.split(',')
        restaurant_ids.append(data[0])

    return restaurant_ids

##############################################
# JSON Data
##############################################
def get_json_data():
    # Initialize menu_id at 1
    menu_id = 1
    list_of_menu_items = []
    list_of_restaurants = []
    list_of_categories = []

    restaurant_ids = get_restaurant_ids()

    for id in restaurant_ids:
        new_itmes = []

        json_path = "json_clean/" + str(id) + "_data.json"
        json_val = json.load(open(json_path))
        df = json_val['result']

        new_items, menu_id = get_menu_items(list_of_menu_items, df, menu_id)
        list_of_menu_items = new_items
        list_of_restaurants = get_restaurant_data(list_of_restaurants, df)
        list_of_categories = get_category_data(list_of_categories, df)

    return list_of_menu_items, list_of_restaurants, list_of_categories

##############################################
# Menu Data
##############################################
def get_menu_items(list_of_menu_items, df, menu_id):
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


    return list_of_menu_items, menu_id

##############################################
# Restaurant Data
##############################################
def get_restaurant_data(list_of_restaurants, df):
    restaurant_data = {}

    try:
        data = df['data'][0]
    except Exception as e:
        return list_of_restaurants
    restaurant_data['restaurant_id'] = data['restaurant_id']
    restaurant_data['restaurant_name'] = data['restaurant_name']
    restaurant_data['price_range'] = data['price_range']
    restaurant_data['street'] = data['address']['street']
    restaurant_data['city'] = data['address']['city']
    restaurant_data['cuisines'] = data['cuisines']
    list_of_restaurants.append(restaurant_data)

    return list_of_restaurants

##############################################
# Category Data
##############################################
def get_category_data(list_of_categories, df):
    try:
        data = df['data'][0]
    except Exception as e:
        return list_of_categories
    for category in data['cuisines']:
        categories = {}
        categories['restaurant_id'] = data['restaurant_id']
        categories['category'] = category

        list_of_categories.append(categories)

    return list_of_categories

##############################################
# Converts dataframe to CSV
##############################################
def tocsv(path, list):
    df = pd.DataFrame(list)
    df.reset_index(drop=True, inplace=True)
    df.to_csv(path, index=False)



def main():

    restaurant_ids = get_restaurant_ids()

    menu_item_path = "data/foods.csv"
    restaurant_path = "data/restaurants.csv"
    category_path = "data/categories.csv"

    list_of_menu_items, list_of_restaurants, list_of_categories = get_json_data()

    tocsv(menu_item_path, list_of_menu_items)
    tocsv(restaurant_path, list_of_restaurants)
    tocsv(category_path, list_of_categories)

if __name__ == "__main__":
    main()
