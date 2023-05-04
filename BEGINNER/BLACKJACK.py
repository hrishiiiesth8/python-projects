import random


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


game_on = True
user_cards = []
com_cards = []
for _ in range(2):
    user_cards.append(deal_card())
    com_cards.append(deal_card())


def calculate_score(cards):
    # user_score = sum(user_cards)
    # com_score = sum(com_cards)
    # return com_score, user_score
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


while game_on:
    user_score = calculate_score(user_cards)
    com_score = calculate_score(com_cards)
    print(f"Your cards : {user_cards}, your score : {user_score}")
    print(f"Computer's first card is : {com_cards[0]}")
    if user_score == 0 or com_score == 0 or user_score > 21:
        game_on = False
        # print(f"Computer score is :{com_score}")
        # print(f"Your score is : {user_score}")
        # print("You lost.")
    else:
        ask_deal = input("Type 'y' for another card or 'n' to pass:\n")
        if ask_deal == "y":
            user_cards.append(deal_card())
        else:
            game_on = False
            # print(f"Computer score is :{com_score}")
            # if user_score > com_score:
            #     print(f"You win with a score of {user_score}.")
            # elif com_score > user_score:
            #     print(f"Computer is just {com_score-user_score} away with score of {com_score}.")
            # else:
            #     print("It's a draw")

while
