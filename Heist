print("Recruits!")
import time

print()
time.sleep(1)
print("We have missions to do.")
print()
time.sleep(1)
print("Things to steal, people to con, and money to make.")
print()
time.sleep(1)
print("You are assigned Bank Heist.")
print()
time.sleep(2)
print("You will need to gather a team, plan the heist, and execute it flawlessly.")

print()
time.sleep(1)
partners = input("Enter the names of your partners, separated by commas: ")
partner_names = [name.strip() for name in partners.split(",") if name.strip()]

jeff_on_team = any(name.casefold() == "jeff" for name in partner_names)
if jeff_on_team:
    print("Really? You want Jeff?", end="", flush=True)
    time.sleep(0.5)
    print(" He is obnoxious and will likely get you caught.")
    choice = input("Enter 'yes' to keep Jeff on your team or 'no' to remove him: ").strip().casefold()
    while choice not in {"yes", "no"}:
        choice = input("Please enter 'yes' or 'no': ").strip().casefold()
    if choice == "yes":
        print("You have chosen to keep Jeff on your team. Good Luck.")
    else:
        partner_names = [name for name in partner_names if name.casefold() != "jeff"]
        print("Jeff is not on your team. Good Choice")
        jeff_on_team = False
else:
    print("Jeff is not on your team. Good Choice")

time.sleep(1)
print(f"You have chosen {', '.join(partner_names) if partner_names else 'no one'} as your partners.")
time.sleep(1)
print("Now, let's plan the heist.")
time.sleep(1)


def choose_plan(prompt, options):
    print()
    print(prompt)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
        time.sleep(0.5)

    print()
    valid = {str(i) for i in range(1, len(options) + 1)}
    choice = input("Enter the number of the plan you want to use: ").strip()
    while choice not in valid:
        print("Invalid choice. Please pick one of the listed numbers.")
        choice = input("Enter the number of the plan you want to use: ").strip()

    selected = options[int(choice) - 1]
    print(f"You have chosen plan {choice}. {selected}")
    print()
    return choice, selected


def summarize_money(container_choice):
    amounts = {
        "1": ("$100,000", "duffel bags"),
        "2": ("$10,000", "a potato sack"),
        "3": ("$50,000", "a cart"),
        "4": ("$25,000", "a backpack"),
    }
    if container_choice in amounts:
        amount, carry_type = amounts[container_choice]
        print(f"You stole: {amount} in cash using {carry_type}.")


entrance = input("Enter the entrance you will use (front, back, or roof): ").strip().lower()
print(f"You have chosen the {entrance} entrance.")
print()

if entrance == "front":
    print("You will need to disable the security cameras and guards.")
    time.sleep(1)
    print("How will you do that?")
    camera_plan1 = "Use a jammer to disable the cameras."
    camera_plan2 = "Use bricks to break the cameras."
    camera_plan3 = "Use a gun to break the cameras."
    camera_choice, camera_plan = choose_plan("Choose your plan for the cameras:", [camera_plan1, camera_plan2, camera_plan3])

    print("Now, let's plan the guards.")
    Bguard_plan1 = "Use a smoke bomb to distract the guards."
    Bguard_plan2 = "Use a gun to take out the guards."
    Bguard_plan3 = "Use a taser to disable the guards."
    Bguard_plan4 = "Fake emergency to lure the guards away."
    guard_choice, guard_plan = choose_plan("Choose your plan for the guards:", [Bguard_plan1, Bguard_plan2, Bguard_plan3, Bguard_plan4])

    print("Make sure to have a plan for the vault and the money.")
    print("How will you get the money out of the vault?")
    vault_plan1 = "Use a drill to break into the vault."
    vault_plan2 = "Use a key to open the vault."
    vault_plan3 = "Use a bomb to blow up the vault."
    vault_choice, vault_plan = choose_plan("Choose your plan for the vault:", [vault_plan1, vault_plan2, vault_plan3])

    print("How will you get the money out of the bank?")
    container_plan1 = "Use duffel bags to carry the money."
    container_plan2 = "Use a potato sack to carry the money."
    container_plan3 = "Use a cart to carry the money."
    container_plan4 = "Use a backpack to carry the money."
    container_choice, container_plan = choose_plan("Choose your plan for the money:", [container_plan1, container_plan2, container_plan3, container_plan4])

    print("Last, you will need to have a getaway car ready.")
    Car1 = "Honda Sedan"
    Car2 = "Bank Van"
    Car3 = "Ford Mustang"
    Car4 = "Chevrolet Camaro"
    getaway_choice, getaway_car = choose_plan("Choose your getaway car:", [Car1, Car2, Car3, Car4])

    time.sleep(2)
    print("Now, let's execute the heist.")
    time.sleep(2)
    print()
    print(f"You enter the bank through the {entrance} entrance. You disabled the cameras using {camera_plan}")
    time.sleep(0.5)
    print(f"You distracted the guards using {guard_plan}. You broke into the vault using {vault_plan}.")
    time.sleep(0.5)
    print()
    if jeff_on_team == True:
        print("Jeff was supposed to help you carry the money out of the bank, but he tripped and dropped the duffel bags.")
        time.sleep(1)
        print("The guards were alerted and caught you and your team. While the driver was able to escape.")
        time.sleep(1)
        print("Jeff was a liability during the heist, and got you caught.")
        time.sleep(1)
        print("You and your team have failed the heist.")
        time.sleep(1)
        print("You have lost all the money and your freedom.")
        time.sleep(1)
        import random
        years = random.randint(5, 20)
        print(f"You were sent to prison for {years} years.")
        time.sleep(1)
        print("Game Over.")
    else:
        print(f"You carry the money out of the bank using {container_plan}. You got into your getaway car and drove away.")
        time.sleep(1)
        print("You and your team have successfully completed the heist!")
        summarize_money(container_choice)
  

elif entrance == "back":
    print("You will need to disable the security cameras.")
    time.sleep(1)
    print("How will you do that?")
    camera_plan1 = "Use a jammer to disable the cameras."
    camera_plan2 = "Use bricks to break the cameras."
    camera_plan3 = "Use a gun to break the cameras."
    camera_choice, camera_plan = choose_plan("Choose your plan for the cameras:", [camera_plan1, camera_plan2, camera_plan3])

    print("Now we need a plan to open the back door.")
    time.sleep(1)
    backdoor_plan1 = "Use a crowbar to pry open the door."
    backdoor_plan2 = "Look for the keycard to open the door."
    backdoor_plan3 = "Use a keypad combination cracker to open the door."
    backdoor_plan4 = "Dewire the door lock to open the door."
    backdoor_choice, backdoor_plan = choose_plan("Choose your plan for the back door:", [backdoor_plan1, backdoor_plan2, backdoor_plan3, backdoor_plan4])

    print("Make sure to have a plan for the vault and the money.")
    time.sleep(1)
    print("How will you get into the vault?")
    vault_plan1 = "Use a drill to break into the vault."
    vault_plan2 = "Use a keycard to open the vault."
    vault_plan3 = "Use a bomb to blow up the vault."
    vault_choice, vault_plan = choose_plan("Choose your plan for the vault:", [vault_plan1, vault_plan2, vault_plan3])

    print("How will you get the money out of the vault?")
    container_plan1 = "Use duffel bags to carry the money."
    container_plan2 = "Use a potato sack to carry the money."
    container_plan3 = "Use a cart to carry the money."
    container_plan4 = "Use a backpack to carry the money."
    container_choice, container_plan = choose_plan("Choose your plan for the money:", [container_plan1, container_plan2, container_plan3, container_plan4])

    print("Choose your getaway car:")
    Car1 = "Honda Sedan"
    Car2 = "Bank Van"
    Car3 = "Ford Mustang"
    Car4 = "Chevrolet Camaro"
    getaway_choice, getaway_car = choose_plan("Choose your getaway car:", [Car1, Car2, Car3, Car4])

    time.sleep(2)
    print("Now, let's execute the heist.")
    time.sleep(2)
    print()
    print("You sneak in through the back entrance and disable the cameras using the chosen method.")
    print(f"You open the back door with {backdoor_plan} and crack the vault using {vault_plan}.")
    if jeff_on_team:
        print("Jeff was supposed to help you carry the money out of the bank, but he tripped and dropped the bags.")
        time.sleep(1)
        print("The guards were alerted and caught you and your team. The driver was able to escape.")
        time.sleep(1)
        print("Jeff was a liability during the heist, and got you caught.")
        time.sleep(1)
        print("You and your team have failed the heist.")
        time.sleep(1)
        print("You have lost all the money and your freedom.")
        time.sleep(1)
        import random
        years = random.randint(5, 20)
        print(f"You were sent to prison for {years} years.")
        time.sleep(1)
        print("Game Over.")
    else:
        print(f"You carry the money out using {container_plan} and escape in your getaway car.")
        time.sleep(1)
        print()
        print("You and your team have successfully completed the heist!")
        summarize_money(container_choice)

elif entrance == "roof":
    print("The roof is your route. You will need a stealthy entry and a fast exit.")
    time.sleep(1)
    roof_plan1 = "Use a drone to scout the roof access point."
    roof_plan2 = "Cut through the maintenance tunnel."
    roof_plan3 = "Use an elevator access keycard."
    roof_choice, roof_plan = choose_plan("Choose your roof entry plan:", [roof_plan1, roof_plan2, roof_plan3])

    print("How will you get into the vault?")
    vault_plan1 = "Use a drill to break into the vault."
    vault_plan2 = "Use a key to open the vault."
    vault_plan3 = "Use a bomb to blow up the vault."
    vault_choice, vault_plan = choose_plan("Choose your plan for the vault:", [vault_plan1, vault_plan2, vault_plan3])

    print("How will you get the money out of the bank?")
    container_plan1 = "Use duffel bags to carry the money."
    container_plan2 = "Use a potato sack to carry the money."
    container_plan3 = "Use a cart to carry the money."
    container_plan4 = "Use a backpack to carry the money."
    container_choice, container_plan = choose_plan("Choose your plan for the money:", [container_plan1, container_plan2, container_plan3, container_plan4])

    print("Choose your getaway vehicle:")
    vehicle_plan1 = "Honda Sedan"
    vehicle_plan2 = "Bank Van"
    vehicle_plan3 = "Helecopter"
    vehicle_plan4 = "Motorcycle"    
    getaway_choice, getaway_car = choose_plan("Choose your getaway vehicle:", [vehicle_plan1, vehicle_plan2, vehicle_plan3, vehicle_plan4])

    time.sleep(2)
    print("Now, let's execute the heist.")
    time.sleep(2)
    print()
    print("You approach the roof quietly and execute your entry plan before descending to the vault.")
    if jeff_on_team:
        print("Jeff was supposed to help you carry the money off the roof, but he lost his footing and dropped the duffel bags.")
        time.sleep(1)
        print("The guards were alerted and caught you and your team before you could escape.")
        time.sleep(1)
        print("Jeff was a liability during the heist, and got you caught.")
        time.sleep(1)
        print("You and your team have failed the heist.")
        time.sleep(1)
        print("You have lost all the money and your freedom.")
        time.sleep(1)
        import random
        years = random.randint(5, 20)
        print(f"You were sent to prison for {years} years.")
        time.sleep(1)
        print("Game Over.")
    else:
        print("You bypass the security and carry the money to the getaway vehicle with no delay.")
        print("The crew escapes cleanly and lands the heist.")
        time.sleep(1)
        print()
        print("You and your team have successfully completed the heist!")
        summarize_money(container_choice)

    print("Invalid entrance choice. The heist has been called off.")
