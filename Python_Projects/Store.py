import time
import random

print("Welcome to the Store!")
time.sleep(1)
print("We have a variety of items for sale.")
time.sleep(1)
items = {
    "produce": {
        "apples": 0.5,
        "bananas": 0.3,
        "oranges": 0.7,
        "grapes": 1.0,
        "watermelons": 3.0,
    },
    "deli": {
        "turkey": 4.0,
        "ham": 3.5,
        "pepperoni": 5.0,
        "salami": 4.5,
        "pastrami": 6.0,
        "american_cheese": 2.0,
        "pepperjack": 2.5,
        "colbyjack": 2.0,
        "swiss": 2.0
    },
    "bakery": {
        "bread": 2.0,
        "bagels": 1.5,
        "croissants": 2.5,
        "muffins": 2.0,
        "donuts": 1.0,
        "cookies": 1.5,
        "rolls": 1.0
    },
    "cereal": {
        "cheerios": 3.0,
        "frosted_flakes": 3.5,
        "cocoa_puffs": 4.0,
        "raisin_bran": 3.0,
        "cinnamon_toast_crunch": 3.5
    },
    "snacks": {
        "20oz-chips": 2.0,
        "16oz-chips": 1.5,
        "12oz-chips": 1.0,
        "box-12oz-chips": 6.0,
        "pretzels": 1.5,
        "pork_rinds": 2.0,
        "spicy_pork_rinds": 2.5,
        "popcorn": 2.5,
        "trail_mix": 3.0,
        "granola_bars": 1.5
    },
    "freezer": {
        "food": {
            "frozen_pizza": 5.0,
            "frozen_vegetables": 3.0,
            "frozen_dinners": 6.0,
            "frozen_fish": 7.0,
            "frozen_waffles": 4.0,
            "frozen_burritos": 5.0
        },

        "ice_cream": 4.0,
        "frozen_fruit": 4.0,
        "frozen_cakes": 5.0,
        "ice": 2.0,
        "popsicles": 3.0
    },
    "beverages": {
        "soda": 1.5,
        "juice": 2.0,
        "water": 1.0,
        "tea": 1.5,
        "iced_coffee": 2.0,
        "energy_drinks": 3.0,
        "sports_drinks": 2.5,
        "sparkling_water": 1.5,
        "gatorade": 2.0,
        "vitamin_water": 2.5
    },
    "dairy": {
        "milk": 2.0,
        "almond_milk": 3.0,
        "soy_milk": 3.0,
        "coconut_milk": 3.0,
        "cheese": 3.0,
        "yogurt": 1.5,
        "coconut_yogurt": 2.0,
        "yoplait": 1.5,
        "greek_yogurt": 2.0,
        "butter": 2.5,
        "cream_cheese": 2.0,
        "sour_cream": 1.5
    },
    "meat": {
        "chicken": 5.0,
        "beef": 7.0,
        "pork": 6.0,
        "lamb": 8.0,
        "bacon": 4.0,
        "sausage": 5.0,
        "ground_beef": 6.0,
        "ground_turkey": 5.0,
        "ground_chicken": 5.0,
        "ground_pork": 6.0,
        "steak": 10.0,
        "ribeye": 12.0,
        "ribs": 9.0,
        "chops": 8.0,
        "roasts": 12.0
    }
}
def get_category_items(category):
    category_items = {}
    for item, price in items[category].items():
        if isinstance(price, dict):
            category_items.update(price)
        else:
            category_items[item] = price
    return category_items


def display_item_name(item):
    return item.replace("_", " ").title()


categories = list(items)
cart = []
checkout = False

while not checkout:
    print("Choose a category to browse:")
    for index, category in enumerate(categories, start=1):
        print(f"{index}. {category.title()}")

    choice = input("Enter the number of your choice: ")
    if not choice.isdigit() or not 1 <= int(choice) <= len(categories):
        print("That is not a valid category.")
        continue

    category = categories[int(choice) - 1]
    category_items = get_category_items(category)
    print(f"Here are the items in {category.title()}:")
    item_options = list(category_items.items())
    for index, (item, price) in enumerate(item_options, start=1):
        print(f"{index}. {display_item_name(item)} - {price}")

    while True:
        choice = input("Enter the number of the item to add: ").strip()
        if not choice.isdigit() or not 1 <= int(choice) <= len(item_options):
            print("That is not a valid item number.")
            continue

        cart_choice = item_options[int(choice) - 1][0]
        cart.append(cart_choice)
        print(display_item_name(cart_choice), "added to cart.")
        print("Your cart contains:", [display_item_name(item) for item in cart])
        next_choice = input(
            "Enter 1 to add another item, 2 to browse another category, "
            "or 3 to checkout: "
        ).strip()

        if next_choice == "1":
            continue
        if next_choice == "2":
            break
        if next_choice == "3":
            checkout = True
            break
        print("Please choose 1 (add), 2 (browse), or 3 (checkout).")

print("Proceeding to checkout...")
all_items = {
    item: price
    for category in categories
    for item, price in get_category_items(category).items()
}
total = sum(all_items[item] for item in cart)
print("Your total is: $", round(total, 2))
time.sleep(1)
print("Cash or card?")
payment_method = input("Enter '1' for cash or '2' for card: ")
if payment_method == "1":
    print("Please hand over the cash to the cashier.")
elif payment_method == "2":
    print("Please swipe your card at the terminal.")
else:
    print("Invalid payment method.")
print("Processing payment...")
time.sleep(2)
print("Payment successful!")
time.sleep(1)
print("Here is your receipt:")
for item in cart:
    print(display_item_name(item), "-", all_items[item])
print("Total: $", round(total, 2))
time.sleep(2)
print("Thank you for shopping with us!")