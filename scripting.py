name = input("Enter your name: ")
print("Hello there, {}!".format(name.title()))

num = int(input("Enter an integer"))
print("hello" * num)

result = eval(input("Enter an expression: "))
print(result)


##################################################################################################


names = input("Enter names separated by commas: ").split(",") # get and process input for a list of names
assignments = input("Enter assignment count separated by commas: ").split(",") # get and process input for a list of the number of assignments
grades = input("Enter grades separated by commas: ").split(",") # get and process input for a list of grades

# message string to be used for each student
# HINT: use .format() with this string in your for loop
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

# write a for loop that iterates through each set of names, assignments, and grades to print each student's message

for name, a, g in zip(names, assignments, grades):
    potential_grade = int(g) + 2*int(a)
    print(message.format(name, a, g, potential_grade))


##################################################################################################


# Use an import statement at the top
import random

word_file = "words.txt"
word_list = []

#fill up the word_list
with open(word_file,'r') as words:
	for line in words:
		# remove white space and make everything lowercase
		word = line.strip().lower()
		# don't include words that are too long or too short
		if 3 < len(word) < 8:
			word_list.append(word)

# Add your function generate_password here
# It should return a string consisting of three random words 
# concatenated together without spaces
def generate_password():
    return random.choice(word_list)+random.choice(word_list)+random.choice(word_list)
    
# test your function
print(generate_password())