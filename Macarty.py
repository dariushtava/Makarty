import random

game_cards = [i for i in range(5, 26)]
robot_cards = [i for i in range(5, 26)]
player_cards = [i for i in range(5, 26)]
robot_scores = []
player_scores = []
# There are 3 lists for robot,player and game's cards
# There are 2 lists for robot and player's scores


def score_sum(a_list):
    """
    Gets the list of scores and calculate the diamond scores
    Finally returns the diamond scores
    """

    diamond_score = 0
    a_list.sort()
    for i in a_list:
        try:
            if a_list[a_list.index(i)] + 1 == a_list[a_list.index(i) + 1]:
                diamond_score += 10
        except:
            pass
    return diamond_score


while len(game_cards) != 0:
    # It spins as long as there are game cards.
    game_card = game_cards.pop(game_cards.index(random.choice(game_cards)))
    # pops randomly a card from game cards and prints it in red color
    print(f"\033[91m{game_card}")
    robot_card = robot_cards.pop(robot_cards.index(random.choice(robot_cards)))
    # pops randomly a cart from robot carts
    carts = [print(f"\033[92m{i}", end="  ") for i in player_cards]
    # prints player cards in green color for choice

    while True:
        try:
            # asks for player card in normal until input is usable number
            player_card = player_cards.pop(player_cards.index(int(input("\n\033[0mWhat is the number? "))))
            break
        except:
            pass

    if robot_card > player_card:
        # if robot score is bigger than player card gives game card to robot
        robot_scores.append(game_card)
        print(f"you didn't got the score because my cart was {robot_card}")

    elif player_card > robot_card:
        # if robot score is smaller than player card gives game card to player
        player_scores.append(game_card)
        print(f"You got the score because my cart was {robot_card}")
    # else doesn't give the game card

robot_scores.append(score_sum(robot_scores))
player_scores.append(score_sum(player_scores))
# calculates the diamonds scores and add them to robot and player's score list

if sum(robot_scores) > sum(player_scores):
    # if robot scores is bigger than player scores prints the text bellow in red
    print(f"\033[91mGame over! Robot score: {sum(robot_scores)} Your score: {sum(player_scores)}")
elif sum(robot_scores) < sum(player_scores):
    # else if player score is bigger than robot score prints it in text bellow in green
    print(f"\033[92mYou won ! Robot score: {sum(robot_scores)} Your score: {sum(player_scores)}")
else:
    # else prints text bellow
    print(f"I wonder we are equal together Robot score: {sum(robot_scores)} Your score: {sum(player_scores)}")