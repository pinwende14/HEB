import json

# Read items from JSON file
with open('c:/Users/Owner/Desktop/cart.json', 'r') as file:
    shopping_cart = json.load(file)

# Sales tax rate (in decimal form)
sales_tax_rate = 0.0825 # Example: 8%

# Calculate Subtotal, Tax Total, and Grand Total
subtotal = 0
taxable_subtotal = 0
tax_total = 0
total_items = 0

for item in shopping_cart:
    quantity = item.get("quantity", 1)
    total_items += quantity
    item_price = item["price"] * quantity
    subtotal += item_price

    if item.get("isTaxable", True):  # Assume taxable if not specified
        taxable_subtotal += item_price

# Calculate tax total only for taxable items
tax_total = taxable_subtotal * sales_tax_rate
grand_total = subtotal + tax_total

# Print item details
for item in shopping_cart:
    quantity = item.get("quantity", 1)
    total_price = item["price"] * quantity
    print(f"{item['itemName']} (Quantity: {quantity}): ${total_price:.2f}")

# Print Subtotal, Tax Total, Grand Total, and Total Items
print(f"\nSubtotal: ${subtotal:.2f}")
print(f"Tax Total: ${tax_total:.2f}")
print(f"Grand Total: ${grand_total:.2f}")
print(f"Total Items: {total_items}")
