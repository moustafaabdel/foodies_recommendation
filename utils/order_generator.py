

import random
import math


#started with 50 users
NUM_USERS = 50

#started with 493 menu items
NUM_ORDERS = 493

order_num = 0
def get_order_num():
    global order_num
    order_num += 1
    return order_num


def generate_rand_orders(user_id, output):
    global order_num

    # TODO: change to scale free distribution later.
    # As of now no user can have more than 1/20 total menu items.
    orders = random.randint(0, math.ceil(NUM_ORDERS / 30))

    # Get random list of user ids
    list_of_orders = random.sample(range(1, NUM_ORDERS), orders)

    for menu_id in list_of_orders:
        num_times_ordered = random.randint(1, 10)
        output.append(str(get_order_num()) + ',' + str(user_id) + ',' + str(menu_id) + ',' + str(num_times_ordered))



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
