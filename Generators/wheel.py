import random
import time
print("Welcome to the Wheel of Fortune!")
time.sleep(2)
print("You can choose from the following types of wheels:")
wheel_types = {
    "1": "Prize wheel",
    "2": "Number Wheel",
    "3": "Name Wheel"
}
print(wheel_types)
wheel_choice = input("Please enter the number corresponding to your choice: ").strip()
print(f"You have chosen the {wheel_types.get(wheel_choice, 'Invalid choice')}.")
if wheel_choice == "1":
    prizes = input("Please enter the prizes, separated by commas: ").strip().split(",")
if wheel_choice == "2":
    numbers = input("Please enter the numbers, separated by commas: ").strip().split(",")
if wheel_choice == "3":
    names = input("Please enter the names of the participants, separated by commas: ").strip().split(",")
print("Spinning the wheel...")
time.sleep(2)
if wheel_choice == "1":
    result = random.choice(prizes)
    print(f"The wheel landed on: {result}")
elif wheel_choice == "2":
    result = random.choice(numbers)
    print(f"The wheel landed on: {result}")
elif wheel_choice == "3":
    result = random.choice(names)
    print(f"The wheel landed on: {result}")