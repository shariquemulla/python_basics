# Arithmetic operators : 
#   + Addition
#   - Subtraction
#   * Multiplication
#   / Division
#   % Mod (the remainder after dividing)
#   ** Exponentiation (note that ^ does not do this operation, as you might have seen in other languages)
#   // Divides and rounds down to the nearest integer


#################################################################################################


# The current volume of a water reservoir (in cubic metres)
reservoir_volume = 4.445e8
# The amount of rainfall from a storm (in cubic metres)
rainfall = 5e6

# decrease the rainfall variable by 10% to account for runoff
rainfall -= rainfall*10/100

# add the rainfall variable to the reservoir_volume variable
reservoir_volume += rainfall

# increase reservoir_volume by 5% to account for stormwater that flows
# into the reservoir in the days following the storm
reservoir_volume += reservoir_volume*5/100

# decrease reservoir_volume by 5% to account for evaporation
reservoir_volume -= reservoir_volume*5/100

# subtract 2.5e5 cubic metres from reservoir_volume to account for water
# that's piped to arid regions.
reservoir_volume -= 2.5e5

# print the new value of the reservoir_volume variable
print(reservoir_volume)


#################################################################################################


sf_population, sf_area = 864816, 231.89
rio_population, rio_area = 6453682, 486.5

san_francisco_pop_density = sf_population/sf_area
rio_de_janeiro_pop_density = rio_population/rio_area

# Write code that prints True if San Francisco is denser than Rio, and False otherwise
print(san_francisco_pop_density > rio_de_janeiro_pop_density)


################################################################################################


# TODO: Fix this string!
ford_quote = 'Whether you think you can, or you think you can\'t--you\'re right.'

username = "Kinari"
timestamp = "04:50"
url = "http://petshop.com/pets/mammals/cats"

# TODO: print a log message using the variables above.
# The message should have the same format as this one:
# "Yogesh accessed the site http://petshop.com/pets/reptiles/pythons at 16:20."

print(username + " accessed the site " + url + " at " + timestamp + ".")


#################################################################################################


given_name = "William"
middle_names = "Bradley"
family_name = "Pitt"

#todo: calculate how long this name is
name_length = len(given_name + " " + middle_names + " " + family_name)

# Now we check to make sure that the name fits within the driving license character limit
# Nothing you need to do here
driving_license_character_limit = 28
print(name_length <= driving_license_character_limit)


###################################################################################################


print(type("12"))
print(type(12.3))
print(type(len("my_string")))
print(type("hippo" *12))


###################################################################################################


mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"

# TODO: Print a string with this format: This week's total sales: xxx
# You will probably need to write some lines of code before the print statement.

total_sales = int(mon_sales) + int(tues_sales) + int(wed_sales) + int(thurs_sales) + int(fri_sales)
print("This week's total sales: " + str(total_sales))


###############################################################################################


# Browse the complete list of string methods at:
# https://docs.python.org/3/library/stdtypes.html#string-methods
# and try them out here

test_string = "browse the complete list of {} string methods"
print(test_string.capitalize())
print(test_string.casefold())
print(test_string.center(5, 'a'))
print(test_string.count("m"))
print(test_string.endswith('methods'))
print(test_string.find('the'))
print(test_string.format("Python"))
print(test_string.strip('bso'))


##############################################################################################


verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(verse)

# Use the appropriate functions and methods to answer the questions above
# Bonus: practice using .format() to output your answers in descriptive messages!

print('the length of the string variable verse - {}', len(verse))
print('the index of the first occurrence of the word \'and\' in verse - {}'.format(verse.find('and')))
print('the index of the last occurrence of the word \'you\' in verse - {}'.format(verse.rfind('you')))
print('the count of occurrences of the word \'you\' in the verse - {}'.format(verse.count('you')))


################################################################################################


