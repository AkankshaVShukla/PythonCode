
"""Removing elements from lists
This exercise will expand on ways to remove items from a list. You actually have a few options. For a list called n:

n.pop(index) will remove the item at index from the list and return it to you:

n = [1, 3, 5]
n.pop(1)
# Returns 3 (the item at index 1)
print n
# prints [1, 5]
n.remove(item) will remove the actual item if it finds it:

n.remove(1)
# Removes 1 from the list,
# NOT the item at index 1
print n
# prints [3, 5]
del(n[1]) is like .pop in that it will remove the item at the given index, but it won't return it:

del(n[1])
# Doesn't return anything
print n
"""
############################################################
"""
Passing a range into a function
Okay! Range time. The Python range() function is just a shortcut for generating a list, so you can use ranges in all the same places you can use lists.

range(6) # => [0, 1, 2, 3, 4, 5]
range(1, 6) # => [1, 2, 3, 4, 5]
range(1, 6, 3) # => [1, 4]
"""

n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here

def flatten(lists):
  results=[]
  for numbers in lists:
    for num in numbers:
      results.append(num)
  return results


print flatten(n)