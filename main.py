import random

def snake_water_gun(computer, player):
    if computer == player:
        return None
    if computer == 's' and player == 'g':
        return True
    elif computer == 'w' and player == 's':
        return True
    elif computer == 'g' and player == 'w':
        return True
    else:
        return False

choice = ('s', 'w', 'g')
computer = random.randint(0,2)
computer = choice[computer]
player = input("Choose either snake(s), water(w) or gun(g): ").lower()

win = snake_water_gun(computer, player)

if win==True:
    print("The computer chose " + computer + " and you chose " + player + ". You win!")
if win is None:
    print("Draw!")
else:
    print("The computer chose " + computer + " and you chose " + player + ". You lose!")
