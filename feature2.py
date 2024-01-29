import json

# Read items from JSON file
with open('c:/Users/Owner/Desktop/cart.json', 'r') as file:
    shopping_cart = json.load(file)

# Sales tax rate (in decimal form)
sales_tax_rate = 0.0825  # Example: 8.25%

# Calculate Subtotal, Tax Total, and Grand Total
subtotal = 0
for item in shopping_cart:
    quantity = item.get("quantity", 1)
    subtotal += item["price"] * quantity

tax_total = subtotal * sales_tax_rate
grand_total = subtotal + tax_total

# Print item details
for item in shopping_cart:
    quantity = item.get("quantity", 1)
    total_price = item["price"] * quantity
    print(f"{item['itemName']} (Quantity: {quantity}): ${total_price:.2f}")

# Print Subtotal, Tax Total, and Grand Total
print(f"\nSubtotal: ${subtotal:.2f}")
print(f"Tax Total: ${tax_total:.2f}")
print(f"Grand Total: ${grand_total:.2f}")
