import requests
import json

#-----------------------------------------------------------#
# Queries restaruant data from US Restaurant Menu API
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


def query_restaurant_data(restaurant_ids):
    #
    # url = "https://us-restaurant-menus.p.rapidapi.com/menuitems/search/fields"
    #
    # for id in restaurant_ids:
    #     querystring = {"page":"1","fields":"%7B%22restaurant_id%22%3A " + str(id) + "%7D"}
    #
    #     headers = {
    #         'x-rapidapi-host': "us-restaurant-menus.p.rapidapi.com",
    #         'x-rapidapi-key': "b018f7f58bmsh0edfeda0d3e3764p1d6012jsnb76af518a482"
    #         }
    #
    #     response = requests.request("GET", url, headers=headers, params=querystring)
    #
    #
    #     file_name = "../boston_menu_items/json_clean/" + str(id) + "_data.json"
    #     json_object = json.dumps(response.json())
    #
    #     with open(file_name, 'w') as outfile:
    #         outfile.write(json_object)


def main():

    restaurant_ids = get_restaurant_ids()
    query_restaurant_data(restaurant_ids)

if __name__ == "__main__":
    main()
