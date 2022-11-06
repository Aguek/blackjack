import random
from art import logo


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

has_game_ended = False
def play_game():
    print(logo)
    def deal_card():
        random_card = random.choice(cards)
        return random_card

    user_cards = []
    computer_cards = []
    #deal the user and computer two cards each using the deal_card() function.

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    print(f"Your cards are {user_cards}, current sum: {sum(user_cards)}")
    print(f"Computer's first card is {computer_cards[0]}")
    def calculate_score(cards):
        score = sum(cards)
        if score == 21 and len(cards) == 2:
            # print(f"Black jack for {cards}")
            return 0
        elif 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
        return score

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)


        
    if user_score == 0 or computer_score == 0 or user_score > 21:
        has_game_ended = True
    else:
        should_draw_card = input("Would you like to draw another card? Type 'y' for yes and 'n' for no.\n").lower()
        if should_draw_card == "y":
            user_cards.append(deal_card())
            while sum(computer_cards) < 17:
                computer_cards.append(deal_card())
                if computer_score >= 17:
                    exit
        else:
            has_game_ended = True

    def compare(u_score, c_score):
        if u_score == 0:
            print("You win, you have a black jack.")
        elif c_score == 0:
            print("You lose, opponent has a black jack.")
        elif u_score == c_score:
            print("It's a draw")
        elif c_score == 21:
            print("You lose, computer wins.")
        elif u_score == 21:
            print("You win.")
        elif u_score > 21:
            print("You lose.")
        elif c_score > 21:
            print("You win.")
        else:
            print("You lose") if sum(computer_cards) > sum(user_cards) else print("You win")
        print(f"Your final cards are {user_cards}, current sum: {sum(user_cards)}")
        print(f"Computer's cards are {computer_cards}, current sum: {sum(computer_cards)}")
    compare(sum(user_cards), sum(computer_cards))

begin_again = input("Would you like to play the game of Black Jack? Type 'y' for yes and 'n' for no.")
if begin_again == "y":
    play_game()
else:
    exit
