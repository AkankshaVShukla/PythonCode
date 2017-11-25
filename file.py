my_list = [i ** 2 for i in range(1, 11)]

my_file = open("output.txt", "w")

# Add your code below!
for i in my_list:
  my_file.write(str(i) + "\n")
  
my_file.close()

############################
my_file=open("output.txt", "r")
print my_file.read()
my_file.close()

###############################
# Use a file handler to open a file for writing
write_file = open("text.txt", "w")

# Open the file for reading
read_file = open("text.txt", "r")

# Write to the file
write_file.write("Not closing files is VERY BAD.")
write_file.close()


# Try to read from the file
print read_file.read()
read_file.close()

##############################
with open("text.txt", "w") as textfile:
  textfile.write("Success!")

###############################
with open("text.txt","w") as my_file:
  my_file.write("Any data")
  if not my_file.closed:
    my_file.close()    
  print my_file.closed