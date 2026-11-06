print("Announcer: Welcome to the 31st Annual Orange County Horse Races!")
import random
import time

# Generate random horse names
adjectives = ["Lightning", "Thunder", "Midnight", "Golden", "Silver", "Wild", "Lucky", "Rapid", "Fierce", "Majestic"]
nouns = ["Bolt", "Storm", "Rider", "Hooves", "Streak", "Comet", "Star", "Shadow", "Blaze", "Spirit","Bullet","Flash","Gale","Phantom","Tornado","Whirlwind","Zephyr","Tempest","Cyclone","Hurricane"]
name_combinations = [f"{adjective} {noun}" for adjective in adjectives for noun in nouns]
horse_names = random.sample(name_combinations, 5)

# Prizes and losses for the race
first_place_prize = random.randint(1000, 5000)
second_place_prize = random.randint(500, 2000)
third_place_prize = random.randint(100, 1000)
fourth_place_loss = random.randint(50, 500)
fifth_place_loss = random.randint(100, 1000)

# Race introduction
time.sleep(1)
print("Announcer: Get ready for some exciting racing!")
print()
time.sleep(1)
print("Announcer: The horses are lined up at the starting gate, and the crowd is buzzing with anticipation.")
time.sleep(1)
print()

# Ticket sales and betting
bet = input("Ticket Sales: Do you want to place a bet on a horse? (yes/no): ").strip().lower()
horse_name = None
amount = 0.0
if bet == "yes":
    print("Here are the horses you can bet on:")
    for number, name in enumerate(horse_names, start=1):
        print(f"{number}. {name}")
    horse_number = input("Ticket Sales: Which horse do you want to bet on? (1-5): ").strip()
    if horse_number in ["1", "2", "3", "4", "5"]:
        try:
            amount = float(input("Ticket Sales: How much do you want to bet? $").strip())
            if amount <= 0:
                print("Invalid bet amount. No bet placed.")
            else:
                horse_name = horse_names[int(horse_number) - 1]
                print(f"Ticket Sales: You placed a bet on {horse_name} for ${amount:.2f}. Good luck!")
        except ValueError:
            print("Invalid bet amount. No bet placed.")
    else:
        print("Invalid horse number. No bet placed.")
else:
    print("Ticket Sales: No bet placed. Enjoy the race!")

print()

# Race simulation
print("Announcer: Today's race will be a thrilling competition between the following horses:")
for name in horse_names:
    print(f" - {name}")

print()
print("Announcer: And they're off!")
random.shuffle(horse_names)
for i in range(5):
    time.sleep(1)
    print(f"Announcer: {horse_names[i]} is in the lead!")
    time.sleep(1)
print()
print("Announcer: It's a close race! The horses are neck and neck as they approach the finish line!")
time.sleep(1)
winner = random.choice(horse_names)
second_place = random.choice([name for name in horse_names if name != winner])
third_place = random.choice([name for name in horse_names if name != winner and name != second_place])
fourth_place = random.choice([name for name in horse_names if name != winner and name != second_place and name != third_place])
fifth_place = [name for name in horse_names if name != winner and name != second_place and name != third_place and name != fourth_place][0]
print(f"Announcer: And the winner is... {winner}!")
time.sleep(0.75)
print(f"Announcer: And the second place is... {second_place}!")
time.sleep(0.75)
print(f"Announcer: And the third place is... {third_place}!")
time.sleep(1)
print(f"Announcer: And the fourth place is... {fourth_place}!")
time.sleep(1)
print(f"Announcer: And the fifth place is... {fifth_place}!")
time.sleep(1)
if horse_name is not None:
    finish_order = [winner, second_place, third_place, fourth_place, fifth_place]
    place = finish_order.index(horse_name) + 1
    prizes = {
        1: first_place_prize,
        2: second_place_prize,
        3: third_place_prize,
    }
    losses = {
        4: fourth_place_loss,
        5: fifth_place_loss,
    }
    if place in prizes:
        prize = prizes[place]
        print(f"Ticket Sales: Your horse finished in {place}{'st' if place == 1 else 'nd' if place == 2 else 'rd'} place. You won ${prize:.2f}!")
    else:
        loss = losses[place]
        print(f"Ticket Sales: Your horse finished in {place}th place. You lost ${loss:.2f}.")
        time.sleep(0.5)
        print()
        print("Ticket Sales: Better luck next time! Thank you for participating in the 31st Annual Orange County Horse Races!")
time.sleep(1)
print()
print("Announcer: Thank you for joining us today! We hope you enjoyed the races and we look forward to seeing you next year!")