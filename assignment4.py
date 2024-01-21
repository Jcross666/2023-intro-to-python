#jacob Cross
#1/12/24
#by taking the items in the given dictionary, the program asks what item you want and how many, and stores it in an empty dictionary then prints out that dictionary,
#printing the item, the quantity and the total price, then gives a grand total price of everything added up.

import json

supplier_data = '{"parts": ["sprocket", "gizmo", "widget", "dodad"], "sprocket": {"price": 3.99, "quantity": 32}, "gizmo": {"price": 7.98, "quantity": 2}, "widget": {"price": 14.32, "quantity": 4}, "dodad": {"price": 0.5, "quantity": 0}}'
supplier_list = json.loads(supplier_data)

order_list = {}

def your_order(order_list, supplier_list):
    print("Your order")
    total_price = 0
    for order, quantity in order_list.items():
        price = supplier_list[order]["price"]
        total = price * quantity
        total_price += total
        print(f"{order} - {quantity} @ {price} = {total}")
    print(f"Total: ${total_price}")
    print("Thank you for using the parts ordering system")


print("Welcome to the parts ordering system, please enter in a part name, followed by a quantity\n")
print("parts for order are:\n")
print('\n\n'.join(supplier_list["parts"]))


while True:
    order = input("\nPlease enter in a part name, or quit to exit: ")
    if order == "quit":
        your_order(order_list, supplier_list)
        break
    if order not in supplier_list["parts"]:
        print("Error, part does not exist, try again")
        continue
    amount = int(input("Please enter in a quantity to order: "))
    if amount > supplier_list[order]["quantity"]:
        print(f"Error, only {supplier_list[order]['quantity']} left of {order}")
    else:
        if order in order_list:
            if order_list[order] + amount > supplier_list[order]["quantity"]:
                print(f"Error, There is only {amount} left of {order}")
            else:
                order_list[order] += amount
        else:
            order_list[order] = amount