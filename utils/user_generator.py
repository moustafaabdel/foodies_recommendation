import random
from numpy.random import choice
from weight_generator import get_list_of_weights

#-----------------------------------------------------------#
# Generates users and atrificial friendships for each user :)
#-----------------------------------------------------------#


# Represent rough estimate of Northeastern student body actively on campus
NUM_USERS = 5000

#######################################################
# Generates user with random gender, height, and weight
#######################################################
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

#######################################################
# User Info Generators
#######################################################
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



############################################################
# Generates list of random friends using desired weights
############################################################
def generate_rand_friends(user_id, rand_friends):
    # Weighted distribution using 5 ceilings & weights (see weight_generator.py)
    # 80%   chance of having    0-5     friendships
    # 10%   chance of having    5-15    friendships
    # 8%    chance of having    15-50   friendships
    # 2%    chance of having    50-100  friendships
    # 0%    chance of having    100 <   friendships
    weights = get_list_of_weights(5, 0.8, 15, 0.1, 50, 0.08, 100, 0.02, 5000, 0)
    list_of_candidates = list(range(1, NUM_USERS + 1))

    # Chooses number of friends based on weighted distribution
    num_friends = choice(list_of_candidates, 1, p=weights)

    # Generates random sample of friends
    list_of_friends = random.sample(range(NUM_USERS), num_friends[0])

    # Remove friend if friend is the user
    if user_id in list_of_friends:
        list_of_friends.remove(user_id)

    for friend_id in list_of_friends:
        rand_friends.append(str(user_id) + ',' + str(friend_id))

    return rand_friends

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

    # Generate random food users
    rand_food_users = []
    for x in range(0, NUM_USERS):
        rand_food_users = generate_user(x + 1, rand_food_users)

    users_path = 'us_menu_api/data/random_food_users.csv'
    tocsv(users_path, rand_food_users)


    # Generate Friendships
    rand_friends = []
    for x in range(0, NUM_USERS):
        rand_friends = generate_rand_friends(x + 1, rand_friends)

    friendships_path = 'us_menu_api/data/friendships.csv'
    tocsv(friendships_path, rand_friends)


if __name__ == "__main__":
    main()
