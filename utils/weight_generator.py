import math


#################################################################################
# Weighted Distribution using 5 ceiling values and distributions for each ceiling
#################################################################################
def get_list_of_weights(first_ceiling, dist_first, second_ceiling, dist_second,
third_ceiling,dist_third, fourth_ceiling, dist_fourth, fifth_ceiling, dist_fifth):
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
