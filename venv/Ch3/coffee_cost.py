# coffee_cost
# A program to compute the cost of the coffee powder.
# Cost / pound = $10.50
# Shipping costs -- Fixed = $1.50 / order
# Shipping costs -- Variable = $0.86 / Order.

def coffee_cost():
    cost = 0
    quantity = float(input("Enter the quantity of the Coffee : "))
    cost = quantity * (10.50 + 0.86) + 1.50
    return cost


print("Cost of the coffee is : $", coffee_cost())
