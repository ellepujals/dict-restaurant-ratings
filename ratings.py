import sys

def get_user_input():

    new_restaurant_name = input("Choose a restaurant: ")
    new_restaurant_score = input("Rate that restaurant on a scale from 1 to 5: ")

    while True:

        if int(new_restaurant_score) > 5 or int(new_restaurant_score) < 1:
            print("Your rating was out of range. Please choose again.")
            new_restaurant_score = input("Rate that restaurant on a scale from 1 to 5: ")

        if 1 <= int(new_restaurant_score) <= 5:
            break

    new_info = (new_restaurant_name, new_restaurant_score)

    return new_info

def list_restaurant_ratings(the_file):

    """Restaurant rating lister."""

    restaurant_ratings = {}
    filename = open(the_file)
    print(filename)

    for line in filename:

        line = line.rstrip()

        item = line.split(":")

        restaurant_ratings[item[0]] = item[1]

    user_input = get_user_input()

    restaurant_ratings[user_input[0]] = user_input[1]

    return restaurant_ratings


def print_alpha_ratings(the_file):

    tuples_list_dictionary = list_restaurant_ratings(the_file).items()
    in_order_tuples_list = sorted(tuples_list_dictionary)

    for restaurant, rating in in_order_tuples_list:
        print("{} is rated at {}.".format(restaurant, rating))


print_alpha_ratings(sys.argv[1])



