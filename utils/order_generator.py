

import random
import math
from numpy.random import choice



# 10000 users to emulate Northeastern student body (num students on campus)
NUM_USERS = 10000

# 2073 menu items
NUM_ORDERS = 2073

order_num = 0
def get_order_num():
    global order_num
    order_num += 1
    return order_num

def get_list_of_weights():
    # Considering there is inefficient data to create and actual
    # scale-free distribution, we created a rough scale free distribution
    # EXTREMELY ROUGH SCALE-FREE DISTRIBUTION:
    #       0     -   8      orders = 80%       [weights_first]
    #       8    -   12      orders = 10%       [weights_second]
    #       12    -   20      orders = 8%       [weights_third]
    #       20    -   30      orders = 2%      [weights_fourth]
    #       30    -   2073     orders = 0%      [weights_fifth]

    first_ceiling = 8
    second_ceiling = 12
    third_ceiling = 20
    fourth_ceiling = 30
    fifth_ceiling = 2073

    dist_first = 0.80
    dist_second = 0.10
    dist_third = 0.08
    dist_fourth = 0.02
    dist_fifth = 0.0

    num_elements_first = first_ceiling
    num_elements_second = second_ceiling - first_ceiling
    num_elements_third = third_ceiling - second_ceiling
    num_elements_fourth = fourth_ceiling - third_ceiling
    num_elements_fifth = fifth_ceiling - fourth_ceiling

    weights_first = [dist_first/num_elements_first] * num_elements_first
    weights_second = [dist_second/num_elements_second] * num_elements_second
    weights_third = [dist_third/num_elements_third] * num_elements_third
    weights_fourth = [dist_fourth/num_elements_fourth] * num_elements_fourth
    weights_fifth = [dist_fifth/num_elements_fifth] * num_elements_fifth

    total_weights = weights_first + weights_second + weights_third + weights_fourth + weights_fifth

    return total_weights


def generate_rand_orders(user_id, output):
    global order_num

    weights = get_list_of_weights()
    list_of_orders = list(range(1, NUM_ORDERS + 1))

    num_orders = choice(list_of_orders, 1, p=weights)

    list_of_orders = random.sample(range(NUM_USERS), num_orders[0])


    for menu_id in list_of_orders:
        #number of times user ordered a meal
        num_times_ordered = random.randint(1, 3)
        output.append(str(get_order_num()) + ',' + str(user_id) + ',' + str(menu_id) + ',' + str(num_times_ordered))



    return output


def main():


    # Generate random food orders
    rand_food_orders = []

    for x in range(0, NUM_USERS):
        rand_food_orders = generate_rand_orders(x + 1, rand_food_orders)

    filename = 'us_menu_api/data/random_food_orders.csv'
    with open(filename, 'w') as file:
        for line in rand_food_orders:
            file.write(line)
            file.write('\n')
    file.close()



if __name__ == "__main__":
    main()
