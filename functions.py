def cylinder_volume(height, radius=5):  # radius is optional, defaults to 5
    pi = 3.14159
    return height * pi * radius ** 2

cylinder_volume(10) # not passing the optional argument
cylinder_volume(10, 7)  # pass in arguments by position
cylinder_volume(height=10, radius=7)  # pass in arguments by name

####################################################################################################

# write your function here
def population_density(population, land_area):
    return population/land_area

# test cases for your function
test1 = population_density(10, 1)
expected_result1 = 10
print("expected result: {}, actual result: {}".format(expected_result1, test1))

test2 = population_density(864816, 121.4)
expected_result2 = 7123.6902801
print("expected result: {}, actual result: {}".format(expected_result2, test2))

#####################################################################################################

# write your function here
def readable_timedelta(days):
    return '{} week(s) and {} day(s).'.format(days//7, days%7)

# test your function
print(readable_timedelta(10))

####################################################################################################

egg_count = 0

def buy_eggs(count):
    return count + 12  # purchase a dozen eggs

egg_count = buy_eggs(egg_count)

####################################################################################################

def population_density2(population, land_area):
    """Calculate the population density of an area.

    INPUT:
    population: int. The population of that area
    land_area: int or float. This function is unit-agnostic, if you pass in values in terms
    of square km or square miles the function will return a density in those units.

    OUTPUT: 
    population_density: population / land_area. The population density of a particular area.
    """
    return population / land_area


##################################################################################################


def multiply(x, y):
    return x * y
# can be reduced to:

multiply = lambda x, y: x * y
# Both of these functions are used in the same way. In either case, we can call multiply like this:

multiply(4, 7)

#################################################################################################

numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]

# def mean(num_list):
#     return sum(num_list) / len(num_list)
# averages = list(map(mean, numbers))

averages = list(map(lambda num_list : sum(num_list) / len(num_list), numbers))
print(averages)

################################################################################################

cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

# def is_short(name):
#     return len(name) < 10
# short_cities = list(filter(is_short, cities))

short_cities = list(filter(lambda name : len(name) < 10, cities))
print(short_cities)