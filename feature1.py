import json

# Read items from JSON file
with open('c:/Users/Owner/Desktop/cart.json', 'r') as file:
    shopping_cart = json.load(file)

# Calculate Grand Total and print item details
grand_total = 0
for item in shopping_cart:
    quantity = item.get("quantity", 1)  # Assume quantity is 1 if not specified
    grand_total += item["price"] * quantity

# Print item details
for item in shopping_cart:
    quantity = item.get("quantity", 1)  # Assume quantity is 1 if not specified
    total_price = item["price"] * quantity
    print(f"{item['itemName']} (Quantity: {quantity}): ${total_price:.2f}")

# Print Grand Total
print(f"\nGrand Total for all items: ${grand_total:.2f}")