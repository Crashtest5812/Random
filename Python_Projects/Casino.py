import random
import time

# ============================================================
# Casino game file overview
# - Slot Machine
# - Blackjack
# - Roulette
# - Bingo
# - Craps
# - Main menu loop
# ============================================================

# ---------------------------
# SLOT MACHINE
# ---------------------------
class SlotMachine:
    def __init__(self):
        self.reels = ['Cherry', 'Lemon', 'Orange', 'Plum', 'Bell', 'Bar', 'Seven']
        self.balance = 100
        self.payouts = {'Cherry': 10, 'Bar': 50, 'Seven': 100}

    def spin(self):
        return [random.choice(self.reels) for _ in range(3)]

    def payout_for(self, result):
        if result[0] == result[1] == result[2]:
            return self.payouts.get(result[0], 0)
        return 0


# Play the slot machine game and handle betting results.
def play_slot_machine():
    print("Welcome to the Slot Machine!")
    time.sleep(1)
    slot_machine = SlotMachine()
    print(f"Your starting balance is: ${slot_machine.balance}")

    machines = [
        ("Classic Slot Machine", SlotMachine()),
        ("Fruit Slot Machine", SlotMachine()),
        ("Lucky Seven Slot Machine", SlotMachine()),
    ]

    for number, (name, _) in enumerate(machines, start=1):
        print(f"{number}. {name}")

    choice = int(input("Select a slot machine (1-3): "))
    selected_machine = machines[choice - 1][1]
    bet_amount = int(input("Enter your bet amount: "))

    if bet_amount > slot_machine.balance:
        print("Insufficient balance for that bet.")
        return

    print(f"Spinning the reels for {machines[choice - 1][0]}...")
    time.sleep(2)
    result = selected_machine.spin()
    print(" | ".join(result))

    winnings = selected_machine.payout_for(result)
    slot_machine.balance += winnings - bet_amount
    if winnings:
        print(f"You won ${winnings}!")
    else:
        print("No win this time.")
    print(f"Your balance is now: ${slot_machine.balance}")


# ---------------------------
# BLACKJACK
# ---------------------------

def deal_card():
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    return random.choice(cards)


def hand_total(hand):
    card_values = {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11,
    }
    total = sum(card_values[card] for card in hand)
    aces = hand.count('A')
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total


# Run a full blackjack round.
def play_blackjack():
    print("Welcome to the Blackjack Table!")
    print("Dealing cards.", end=" ")
    time.sleep(0.5)
    print(".", end=" ")
    time.sleep(0.5)
    print(".")
    time.sleep(1)

    player_hand = [deal_card(), deal_card()]
    print(f"Your hand: {player_hand}")

    while True:
        hit_or_stand = input("Do you want to hit or stand? (h/s): ").strip().lower()
        if hit_or_stand == 's':
            break
        if hit_or_stand != 'h':
            print("Please enter 'h' or 's'.")
            continue

        player_hand.append(deal_card())
        print(f"Your hand: {player_hand}")
        if hand_total(player_hand) > 21:
            print("Bust! You lose.")
            return

    print("You chose to stand. Dealer's turn...")
    dealer_hand = [deal_card(), deal_card()]
    print(f"Dealer's hand: {dealer_hand}")

    while hand_total(dealer_hand) < 17:
        dealer_hand.append(deal_card())
        print(f"Dealer's hand: {dealer_hand}")

    player_total = hand_total(player_hand)
    dealer_total = hand_total(dealer_hand)
    if dealer_total > 21 or player_total > dealer_total:
        print("You win!")
    elif player_total < dealer_total:
        print("Dealer wins!")
    else:
        print("It's a tie!")


# ---------------------------
# ROULETTE
# ---------------------------

def spin_wheel():
    red_numbers = {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36}
    number = random.randint(0, 36)
    color = 'Red' if number in red_numbers else 'Black' if number != 0 else 'Green'
    return number, color


# Handle a roulette wager and reveal the winning result.
def play_roulette():
    print("Welcome to the Roulette Table!")
    bet_type = input("Place your bet (number/color): ").strip().lower()

    if bet_type == 'number':
        bet_number = int(input("Enter a number between 0 and 36: "))
        if bet_number < 0 or bet_number > 36:
            print("Invalid number. Please choose between 0 and 36.")
            return
        print(f"You placed a bet on number {bet_number}. Spinning the wheel...")
        time.sleep(2)
        result_number, result_color = spin_wheel()
        print(f"The ball landed on {result_number} ({result_color}).")
        if result_number == bet_number:
            print("Congratulations! You win!")
        else:
            print("Sorry, you lose.")
    elif bet_type == 'color':
        bet_color = input("Enter a color (red/black): ").strip().lower()
        if bet_color not in ['red', 'black']:
            print("Invalid color. Please choose 'red' or 'black'.")
            return
        print(f"You placed a bet on {bet_color}. Spinning the wheel...")
        time.sleep(2)
        result_number, result_color = spin_wheel()
        print(f"The ball landed on {result_number} ({result_color}).")
        if result_color.lower() == bet_color:
            print("Congratulations! You win!")
        else:
            print("Sorry, you lose.")
    else:
        print("Please choose 'number' or 'color'.")


# ---------------------------
# BINGO
# ---------------------------
class BingoGame:
    def __init__(self):
        self.numbers = list(range(1, 76))
        random.shuffle(self.numbers)
        self.called_numbers = []

        columns = [
            random.sample(range(1, 16), 5),
            random.sample(range(16, 31), 5),
            random.sample(range(31, 46), 5),
            random.sample(range(46, 61), 5),
            random.sample(range(61, 76), 5),
        ]
        self.card = [list(row) for row in zip(*columns)]
        self.card[2][2] = "FREE"

    def display_card(self):
        print("  B    I    N    G    O")
        for row in self.card:
            print(" ".join(f"{number:>4}" for number in row))

    def call_number(self):
        if self.numbers:
            number = self.numbers.pop()
            self.called_numbers.append(number)
            return number
        return None

    def has_won(self):
        marked = set(self.called_numbers) | {"FREE"}
        lines = []
        for row in self.card:
            lines.append(row[:])
        for column_index in range(5):
            lines.append([self.card[row_index][column_index] for row_index in range(5)])
        lines.append([self.card[index][index] for index in range(5)])
        lines.append([self.card[index][4 - index] for index in range(5)])
        return any(all(value in marked for value in line) for line in lines)


# Simulate a bingo round by calling numbers and checking for a win.
def play_bingo():
    print("Welcome to the Bingo Game!")
    bingo_game = BingoGame()
    print("Starting the Bingo game. Numbers will be called...")
    time.sleep(2)
    bingo_game.display_card()
    time.sleep(1)

    for _ in range(10):
        called_number = bingo_game.call_number()
        if called_number is not None:
            print(f"Number called: {called_number}")
            time.sleep(1)
            if bingo_game.has_won():
                print("Bingo! You won!")
                return
        else:
            print("All numbers have been called.")
            break
    print("No Bingo this time.")


# ---------------------------
# CRAPS
# ---------------------------

def roll_dice():
    input("\n Press ENTER to roll the dice...")
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    print(f"Rolled: {die1} + {die2} = {total}")
    return total


# Run one craps round: come-out roll, point, and win/loss checks.
def play_craps():
    print("--- Welcome to the Craps Table! ---")
    print("\n[Phase 1] Come-Out Roll...")
    time.sleep(0.5)
    first_roll = roll_dice()

    if first_roll in (7, 11):
        print(" Natural! You WIN!")
        return True
    if first_roll in (2, 3, 12):
        print(" Craps! You LOSE.")
        return False

    point = first_roll
    print(f"\n The Point is set to: {point}")
    print("To win, you must roll your Point again before rolling a 7.")

    while True:
        time.sleep(0.5)
        subsequent_roll = roll_dice()
        if subsequent_roll == point:
            print(f" Hit the Point ({point})! You WIN!")
            return True
        if subsequent_roll == 7:
            print(" Seven Out! You LOSE.")
            return False
        print(f"No decision. Point is still {point}. Rolling again...")


# ---------------------------
# CARD TABLE GAMES
# ---------------------------


def build_deck():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    return [f"{rank} of {suit}" for suit in suits for rank in ranks]


def score_poker_hand(hand):
    values = [card.split()[0] for card in hand]
    ranks = {value: values.count(value) for value in set(values)}
    counts = sorted(ranks.values(), reverse=True)

    is_flush = len({card.split()[-1] for card in hand}) == 1
    sorted_values = sorted([
        {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
         'J': 11, 'Q': 12, 'K': 13, 'A': 14}[value.split()[0]]
        for value in hand
    ])
    straight = False
    if len(sorted_values) == 5:
        unique = sorted(set(sorted_values))
        if unique == [2, 3, 4, 5, 14]:
            straight = True
            sorted_values = [1, 2, 3, 4, 5]
        elif unique == list(range(min(unique), max(unique) + 1)):
            straight = True

    if is_flush and straight:
        return "Straight Flush"
    if counts == [4, 1]:
        return "Four of a Kind"
    if counts == [3, 2]:
        return "Full House"
    if is_flush:
        return "Flush"
    if straight:
        return "Straight"
    if counts == [3, 1, 1]:
        return "Three of a Kind"
    if counts == [2, 2, 1]:
        return "Two Pair"
    if counts == [2, 1, 1, 1]:
        return "Pair"
    return "High Card"


def play_card_table():
    print("Welcome to the Cards Table!")
    print("Choose a table type: Poker (1) or Texas Hold'em (2)")
    table_type = input("Enter 1 for Poker or 2 for Texas Hold'em: ").strip().lower()

    if table_type == "1":
        print("You have chosen Poker. Let's play!")
        print("Choose a table to play at:")
        print("1. Low Stakes Table")
        print("2. Medium Stakes Table")
        print("3. High Stakes Table")
        table_choice = input("Enter 1, 2, or 3: ").strip().lower()

        deck = build_deck()
        random.shuffle(deck)
        hand = deck[:5]
        print("Dealing your hand...")
        time.sleep(1)
        print(f"Your hand: {', '.join(hand)}")
        print(f"Hand Rank: {score_poker_hand(hand)}")

        keep = input("Do you want to keep your hand or fold? (keep/fold): ").strip().lower()
        if keep == "keep":
            print("You chose to keep your hand.")
        else:
            print("You folded. Better luck next time!")

    elif table_type == "2":
        print("You have chosen Texas Hold'em. Let's play!")
        deck = build_deck()
        random.shuffle(deck)
        hole_cards = deck[:2]
        community_cards = deck[2:7]
        print("Your hole cards:", ", ".join(hole_cards))
        print("Community cards:", ", ".join(community_cards))
        full_hand = hole_cards + community_cards
        print(f"Best hand: {score_poker_hand(full_hand)}")
    else:
        print("Please choose 1 for Poker or 2 for Texas Hold'em.")


# ---------------------------
# MAIN MENU
# ---------------------------

def main():
    print("Welcome to Ceasar's Palace!")
    time.sleep(1)
    print("Get ready to try your luck at the slot machines, Blackjack, Roulette, Bingo, Craps, and Card Table Games!")
    time.sleep(1)

    while True:
        print("1. Slot machine")
        print("2. Blackjack")
        print("3. Roulette")
        print("4. Bingo")
        print("5. Craps")
        print("6. Card Table Games")
        selection = input("Choose a game (1-6, or quit): ").strip().lower()

        if selection in ("quit", "quit game", "q"):
            print("Thanks for playing!")
            break

        if selection == '1':
            play_slot_machine()
        elif selection == '2':
            play_blackjack()
        elif selection == '3':
            play_roulette()
        elif selection == '4':
            play_bingo()
        elif selection == '5':
            print("Welcome to the Craps Table!")
            play_craps()
        elif selection == '6':
            play_card_table()
        else:
            print("Please choose a game from 1 to 6, or quit.")

        print()


if __name__ == "__main__":
    main()
