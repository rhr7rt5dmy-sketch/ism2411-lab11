# ISM 2411 - Module 11: Dictionaries Lab
#
# Reflection 1:
# I would use .get() when a value might be missing and I want my program
# to keep running with a default value. I would use bracket notation when
# I expect a key to exist and want Python to raise an error if it does not.
#
# Reflection 2:
# Building a summary dictionary with a loop reminds me of using a PivotTable
# in Excel to group data and calculate totals. Python can automate this process
# across large datasets and repeat the same calculations without manually
# organizing the data each time.


# Exercise 1: One customer

customer = {
    "name": "Alice",
    "email": "alice@email.com",
    "tier": "gold",
    "ytd_spend": 1250
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])

print(customer)

# Exercise 2: Update and add

customer["phone"] = "555-123-4567"
print(customer)

customer["tier"] = "platinum"
print(customer)

del customer["email"]
print(customer)