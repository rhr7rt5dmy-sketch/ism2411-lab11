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

# Exercise 3: Safe lookup

print(customer.get("email", "no email on file"))

try:
    print(customer["email"])
except KeyError:
    print("KeyError: email does not exist in the dictionary.")
    # Exercise 4: Iterate

for key, value in customer.items():
    print(f"{key}: {value}")

# Without .items(), the loop only gives us the keys.
# With .items(), we get both the key and its value.

for key in customer:
    print(key)

# Exercise 5: Lookup table

tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15
}

discount_rate = tier_discounts.get(customer["tier"], 0)
purchase_price = 200
discount_amount = purchase_price * discount_rate
final_price = purchase_price - discount_amount

print(f"Tier: {customer['tier']}")
print(f"Discount rate: {discount_rate:.0%}")
print(f"Final price: ${final_price:.2f}")

# Exercise 6: List of dicts

customers = [
    {"name": "Alice", "tier": "platinum"},
    {"name": "Bob", "tier": "gold"},
    {"name": "Charlie", "tier": "silver"}
]

purchase_price = 300

for customer in customers:
    discount_rate = tier_discounts.get(customer["tier"], 0)
    discount_amount = purchase_price * discount_rate

    print(
        f"{customer['name']} | "
        f"{customer['tier']} | "
        f"Discount: ${discount_amount:.2f}"
    )

# Exercise 7: Nested catalog

catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8}
}

for product, details in catalog.items():
    if details["stock"] < 20:
        print(
            f"LOW STOCK: {product} "
            f"(Stock: {details['stock']})"
        )


# Exercise 8: Sales by region

transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]

sales_summary = {}

for transaction in transactions:
    region = transaction["region"]
    amount = transaction["amount"]

    sales_summary[region] = sales_summary.get(region, 0) + amount

for region in sorted(sales_summary):
    print(f"{region}: ${sales_summary[region]}")
