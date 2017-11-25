my_dict= {
  "Name": "Akanksha",
  "Age": 26,
  "BDFL": True
}
print my_dict.items()
print my_dict.keys()
print my_dict.values()


for key in my_dict:
  print key, my_dict[key]
  
######################
doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0]

# Complete the following line. Use the line above for help.
even_squares = [x**2 for x in range(1, 11) if x%2==0]

print even_squares

#########################
cubes_by_four = [x ** 3 for x in range(1, 11) if ((x ** 3) % 4) == 0]
print cubes_by_four

#########################
l = [i ** 2 for i in range(1, 11)]
# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print l[2:9:2]
#[9, 25, 49, 81]

my_list = range(1, 11) # List of numbers 1 - 10

# Add your code below!
print my_list[::2] # [1, 3, 5, 7, 9]

############################

#Create a variable called backwards and set it equal to the reversed version of my_list.
my_list = range(1, 11)

# Add your code below!

# Add your code below!
backwards=my_list[::-1]