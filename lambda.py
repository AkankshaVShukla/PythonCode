my_list = range(16)
print filter(lambda x: x % 3 == 0, my_list)

###############################################
languages = ["HTML", "JavaScript", "Python", "Ruby"]

# Add arguments to the filter()
print filter(lambda x: x=="Python", languages)

##############################################
"""
Create a list, squares, that consists of the squares of the numbers 1 to 10. A list comprehension could be useful here!

Use filter() and a lambda expression to print out only the squares that are between 30 and 70 
"""
squares=[x**2 for x in range(1,11)]
print filter(lambda x: x>=30 and x<=70, squares)

###############################################
threes_and_fives=[x for x in range(1,16) if x%3==0 or x%5==0]

###############################################