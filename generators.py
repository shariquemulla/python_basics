def my_range(x):
    i = 0
    while i < x:
        yield i
        i += 1

for x in my_range(5):
    print(x)

################################################################################################

lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]

def my_enumerate(iterable, start=0):
    # Implement your generator function here
    for i in iterable:
        yield start, i
        start += 1

for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))

# OUTPUT
# Lesson 1: Why Python Programming
# Lesson 2: Data Types and Operators
# Lesson 3: Control Flow
# Lesson 4: Functions
# Lesson 5: Scripting

##############################################################################################

def chunker2(iterable, size):
    for i in range(0, len(iterable), size):
        yield iterable[i : i+size]

for chunk in chunker2('range(25)', 4):
    print(list(chunk))