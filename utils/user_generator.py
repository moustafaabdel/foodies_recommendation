

import random
import math
import numpy as np
from numpy.random import choice
from scipy.stats import expon


# 10000 users to represent Northeastern student body
NUM_USERS = 5000


def generate_user(user_id, output):

    gender = random_gender()
    feet_height = random_feet_height()
    inches_height = random_inches_height()
    weight = random_weight()

    output.append(str(user_id) + ',' +
    gender + ',' +
    str(feet_height) + ',' +
    str(inches_height) + ',' +
    str(weight))

    return output

def random_gender():
    gender_val = random.randrange(3)
    if (gender_val == 0):
        return "male"
    elif (gender_val == 1):
        return "female"
    elif (gender_val == 2):
        return "other"

def random_feet_height():
    return random.randint(5,6)

def random_inches_height():
    return random.randrange(0,12)

def random_weight():
    return random.randint(130,200)


def get_list_of_weights():
    # Considering there is inefficient data to create and actual
    # scale-free distribution, we created a rough scale free distribution
    # EXTREMELY ROUGH SCALE-FREE DISTRIBUTION:
    #       0     -   5    followers = 80%       [weights_first]
    #       5   -   15    followers = 10%       [weights_second]
    #       15   -   50    followers = 8%       [weights_third]
    #       50   -   100   followers = 2%      [weights_fourth]
    #       100  -   10000   followers = 0%      [weights_fifth]
    first_ceiling = 5
    second_ceiling = 15
    third_ceiling = 50
    fourth_ceiling = 100
    fifth_ceiling = 5000

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

#generate list of friends
def generate_rand_friends(user_id, output):

    weights = get_list_of_weights()
    list_of_candidates = list(range(1, NUM_USERS + 1))

    num_friends = choice(list_of_candidates, 1, p=weights)

    # Get random list of user ids
    list_of_friends = random.sample(range(NUM_USERS), num_friends[0])

    # Remove friend if friend is the user
    if user_id in list_of_friends:
        list_of_friends.remove(user_id)

    for friend_id in list_of_friends:
        output.append(str(user_id) + ',' + str(friend_id))

    return output


def main():

    # # Generate random food users
    rand_food_users = []
    for x in range(0, NUM_USERS):
        rand_food_users = generate_user(x + 1, rand_food_users)

    filename = 'us_menu_api/data/random_food_users.csv'
    with open(filename, 'w') as file:
        for line in rand_food_users:
            file.write(line)
            file.write('\n')
    file.close()


    # Generate friendships
    rand_friends = []

    for x in range(0, NUM_USERS):
        rand_friends = generate_rand_friends(x + 1, rand_friends)

    filename = 'us_menu_api/data/friendships.csv'
    with open(filename, 'w') as file:
        for line in rand_friends:
            file.write(line)
            file.write('\n')
    file.close()


if __name__ == "__main__":
    main()
