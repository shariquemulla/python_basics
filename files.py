# READING A FILE
f = open('camelot.txt', 'r')
file_data = f.read()
f.close()

# WRITING TO A FILE
f = open('camelot.txt', 'w')
f.write("Hello there!")
f.close()

# WITH keyword to close the file automatically
with open('my_path/my_file.txt', 'r') as f:
    file_data = f.read()

##################################################################################################

with open("camelot.txt") as song:
    print(song.read(2))
    print(song.read(8))
    print(song.read())

##################################################################################################

camelot_lines = []
with open("camelot.txt") as f:
    for line in f:
        camelot_lines.append(line.strip())

print(camelot_lines)

##################################################################################################

def create_cast_list(filename):
    cast_list = []
    #use with to open the file filename
    #use the for loop syntax to process each line
    #and add the actor name to cast_list
    with open(filename) as f:
        for line in f:
            cast_list.append(line.strip().split(',')[0])
    
    return cast_list

cast_list = create_cast_list('flying_circus_cast.txt')
for actor in cast_list:
    print(actor)


################################################################################################

# Create a function that opens the flowers.txt, reads every line in it, and saves it as a dictionary. 
# The main (separate) function should take user input (user's first name and last name) and parse the user input to identify the first letter of the first name. 
# It should then use it to print the flower name with the same first letter (from dictionary created in the first function).

def create_flower_dict(filename):
    flowers_dict = {}
    with open(filename) as file:
        for line in file:
            tokens = [token.strip() for token in line.split(':')]
            flowers_dict[tokens[0]] = tokens[1]
    return flowers_dict

def main():
    flowers_dict = create_flower_dict('flowers.txt')
    name = input('Enter your First [space] Last name only:')
    print('Unique flower name with the first letter: {}'.format(flowers_dict.get(name[0].upper())))

main()

##############################################################################################

