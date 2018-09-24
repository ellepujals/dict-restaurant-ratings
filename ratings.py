import sys

def list_restaurant_ratings(the_file):

    """Restaurant rating lister."""

    restaurant_ratings = {}
    filename = open(the_file)
    print(filename)

    for line in filename:

        line = line.rstrip()

        item = line.split(":")

        restaurant_ratings[item[0]] = item[1]

    new_restaurant_name = input("Choose a restaurant! ")
    new_restaurant_score = input("Rate that restaurant on a scale from 1 to 5. ")

    restaurant_ratings[new_restaurant_name] = new_restaurant_score

    return restaurant_ratings


def print_alpha_ratings(the_file):

    tuples_list_dictionary = list_restaurant_ratings(the_file).items()
    in_order_tuples_list = sorted(tuples_list_dictionary)

    for restaurant, rating in in_order_tuples_list:
        print("{} is rated at {}.".format(restaurant, rating))


print_alpha_ratings(sys.argv[1])



