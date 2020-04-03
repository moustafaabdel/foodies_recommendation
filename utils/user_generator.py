

import random
import math


#start w 50 users
NUM_USERS = 50


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





#generate list of friends
def generate_rand_friends(user_id, output):

    # TODO: change to scale free distribution later.
    # As of now no user can have more than (n = 1/3 of total population) friends.
    num_friends = random.randint(0, math.ceil(NUM_USERS / 3))

    # Get random list of user ids
    list_of_friends = random.sample(range(NUM_USERS), num_friends)

    # Remove friend if friend is the user
    if user_id in list_of_friends:
        list_of_friends.remove(user_id)

    for friend_id in list_of_friends:
        output.append(str(user_id) + ',' + str(friend_id))

    return output


#execute main
def main():

    # Generate random food users
    rand_food_users = []
    for x in range(0, NUM_USERS):
        rand_food_users = generate_user(x + 1, rand_food_users)

    filename = 'random_food_users.csv'
    with open(filename, 'w') as file:
        for line in rand_food_users:
            file.write(line)
            file.write('\n')
    file.close()


    # Generate friendships
    rand_friends = []

    for x in range(0, NUM_USERS):
        rand_friends = generate_rand_friends(x + 1, rand_friends)

    filename = 'friendships.csv'
    with open(filename, 'w') as file:
        for line in rand_friends:
            file.write(line)
            file.write('\n')
    file.close()



if __name__ == "__main__":
    main()
