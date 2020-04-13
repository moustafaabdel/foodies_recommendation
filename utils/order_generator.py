import random
from numpy.random import choice
import pandas as pd
from weight_generator import get_list_of_weights

#-----------------------------------------------------------#
# Generates orders for users with a weighted distribution for
#   number of orders and restaurants ordered from
#-----------------------------------------------------------#


# Represent rough estimate of Northeastern student body actively on campus
NUM_USERS = 5000
# 2073 menu items pulled from us_menu_api
NUM_ITEMS = 2073

#######################################################
# Used to get order number
#######################################################
order_num = 0
def get_order_num():
    global order_num
    order_num += 1
    return order_num


def get_items_from_restaurants(data, restaurants_to_order_from):
    restaurants = data.loc[data['restaurant_id'].isin(restaurants_to_order_from)]
    return restaurants['menu_id'].tolist()


###############################################################################
# Generate random orders for specified user from n number of chosen restaurants
# where n is a random value between 1 & 5.
# Probability of total number of orders shown below.
###############################################################################
def generate_rand_orders(user_id, rand_food_orders, data, restaurant_ids):
    global order_num
    # Weighted distribution using 5 ceilings & weights (see weight_generator.py)
    # 20%   chance of having    0-5     orders
    # 70%   chance of having    5-12    orders
    # 8%    chance of having    12-20   orders
    # 2%    chance of having    20-30   orders
    # 0%    chance of having    30 <    orders
    weights = get_list_of_weights(5, 0.2, 12, 0.7, 20, 0.08, 30, 0.02, 2073, 0)
    weighted_num_orders = choice(list(range(1, NUM_ITEMS + 1)), 1, p=weights)
    num_orders = weighted_num_orders[0]

    # Choose up to 4 random restaurants specified user will order from to simulate customer loyalty
    # Pigeonhole - 70% of users will order from at least one restaurant more than once
    num_restaurants = random.randint(1,4)

    restaurants_to_order_from = random.sample(restaurant_ids, num_restaurants)
    list_of_options_from_restaurant = get_items_from_restaurants(data, restaurants_to_order_from)

    adjustment_size = 1
    # Will ensure that there are enough options for the user to choose from
    while num_orders > len(list_of_options_from_restaurant):
        restaurants_to_order_from = random.sample(restaurant_ids, num_restaurants + adjustment_size)
        list_of_options_from_restaurant = get_items_from_restaurants(data, restaurants_to_order_from)
        adjustment_size *= 2

    list_of_orders = random.sample(list_of_options_from_restaurant, num_orders)


    for menu_id in list_of_orders:
        #number of times user ordered a meal
        num_times_ordered = random.randint(1, 3)
        rand_food_orders.append(str(get_order_num()) + ',' + str(user_id) + ',' + str(menu_id) + ',' + str(num_times_ordered))

    return rand_food_orders


##############################################
# Restaurant ID
##############################################
def get_restaurant_ids():

    with open('us_menu_api/data/restaurant_ids.csv','r') as csv_file:
        lines = csv_file.readlines()

    restaurant_ids = []
    for line in lines:
        data = line.split(',')
        restaurant_ids.append(data[0])

    return restaurant_ids

##############################################
# Generates CSV using path and provided list
##############################################
def tocsv(path, list):
    with open(path, 'w') as file:
        for line in list:
            file.write(line)
            file.write('\n')
    file.close()

def main():
    # Generate random food orders
    rand_food_orders = []

    data = pd.read_csv("us_menu_api/data/foods.csv")
    restaurant_ids = get_restaurant_ids()
    for x in range(0, NUM_USERS):
        rand_food_orders = generate_rand_orders(x + 1, rand_food_orders, data, restaurant_ids)

    filename = 'us_menu_api/data/random_food_orders.csv'
    tocsv(filename, rand_food_orders)



if __name__ == "__main__":
    main()
