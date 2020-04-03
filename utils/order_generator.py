

import random
import math


#started with 50 users
NUM_USERS = 50

#started with 493 menu items
NUM_ORDERS = 493


def generate_rand_orders(user_id, output):
    # TODO: change to scale free distribution later.
    # As of now no user can have more than 1/10 total menu items.
    orders = random.randint(0, math.ceil(NUM_ORDERS / 10))

    # Get random list of user ids
    list_of_orders = random.sample(range(NUM_ORDERS), orders)


    for menu_id in list_of_orders:
        output.append(str(user_id) + ',' + str(menu_id))

    return output


def main():

    # Generate random food orders
    rand_food_orders = []
    for x in range(0, NUM_USERS):
        rand_food_orders = generate_rand_orders(x + 1, rand_food_orders)

    filename = 'random_food_orders.csv'
    with open(filename, 'w') as file:
        for line in rand_food_orders:
            file.write(line)
            file.write('\n')
    file.close()



if __name__ == "__main__":
    main()
