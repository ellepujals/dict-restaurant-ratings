"""Restaurant rating lister."""


# put your code here

import sys

def list_restaurant_ratings(the_file):
    restaurant_ratings = {}
    filename = open(the_file)
    print(filename)
    for line in filename:

        line = line.rstrip()

        item = line.split(":")

        restaurant_ratings[item[0]] = item[1]

    return restaurant_ratings


def print_alpha_ratings(the_file):

    tuples_list_dictionary = list_restaurant_ratings(the_file).items()
    in_order_tuples_list = sorted(tuples_list_dictionary)

    for item in in_order_tuples_list:
        print("{} is rated at {}.".format(item[0], item[1]))


print_alpha_ratings(sys.argv[1])



