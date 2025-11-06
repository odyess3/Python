import random

def pick_a_card():
    card = random.choice(deck)
    if card == "a":
        return int(input("You got an Ace! Choose 1 or 11: "))
    elif card in ["j", "q", "k"]:
        return 10
    else:
        return int(card)

def check_winner(player_deck, cpu_deck):
    player_total = sum(player_deck)
    cpu_total = sum(cpu_deck)

    print(f"\nFinal Hands:\nYou: {player_deck} (Total: {player_total})\nCPU: {cpu_deck} (Total: {cpu_total})")

    if player_total == 21:
        print("win.")
    elif player_total > 21:
        print("CPU wins!")
    elif cpu_total > 21:
        print("CPU busted! You win.")
    elif cpu_total == 21:
        print("CPU WIN")
    else:
        more(player_deck, cpu_deck)

def more(player_deck, cpu_deck):
    choice = input("Do you want another card? (y/n): ").lower()
    if choice == "y":
        player_deck.append(pick_a_card())
        print(f"Your cards: {player_deck}")
    cpu_deck.append(pick_a_card())
    check_winner(player_deck, cpu_deck)


while input("Do you want to play? (y/n): ").lower() == "y":
    deck = ["a", "2", "3", "4", "5", "6", "7", "8", "9", "10", "j", "q", "k"]
    player_deck = [pick_a_card(), pick_a_card()]
    cpu_deck = [pick_a_card()]

    print(f"Your cards: {player_deck}")
    print(f"CPU shows: {cpu_deck}")

    check_winner(player_deck, cpu_deck)