# Jacob Cross
# december 31, 2023
# this program takes two lists of items and prices which in a for loop prints each item with its respected price from item 0 to item 4, then to get the total price it adds
#all the prices, calculates the tax, and adds the tax and prints all of the totals

items = ["big beef","Spaghetti","salad","lemonade","water"]
prices = [15.86,11.99,5.99,2.99,3.99]
total = prices[0] + prices[1] + prices[2] + prices[3] + prices[4]
total = round(total,2)
tax = 5
total_tax = (total / 100) * tax
total_tax = round(total_tax, 2)
grand_total = total_tax + total

print("Jacob's All Food Receipt\n\n")

for i in range(0, 4):
    print(f"{items[i]} - ${prices[i]}\n")
print("\n")
print(f"Total:${total}\n")
print(f"Tax {tax}%:${total_tax}\n")
print(f"Grand Total:${grand_total}\n\n")

print("Thank you for dining with us! We hope to see you again!")