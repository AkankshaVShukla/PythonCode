#learning basics
monty=True
python=1.234
monty_python =python**2

#MEAL
""" 
You've finished eating at a restaurant, and received this bill:

Cost of meal: $44.50
Restaurant tax: 6.75%
Tip: 15%
You'll apply the tip to the overall cost of the meal (including tax).
"""

meal = 44.50
tax = 6.75 / 100
tip = 15.0 / 100

meal = meal + meal * tax
total=meal + meal * tip

print("%.2f" % total)