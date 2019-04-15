"""Restaurant rating lister."""

# read the ratings from the file
# store as dictionary
# sorts the ratings
# print as full sentences

def restaurant_rating(filename):
    ratings = {}

    with open(filename) as open_file:

        ratings ={open_file}

    for restaurant, rating in ratings.items():
        print(f"{restaurant} is rated at {rating}.")
    




# put your code here
restaurant_rating("scores.txt")