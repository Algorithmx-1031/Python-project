import random as rd

rd_num = rd.randint(0,2)
dice = ['scissors', 'rock', 'paper']
game1 = str(input('Enrer yor guess (scissors rock paper) : '))
w = "You win!"
l = "You lose!"
first_game = True
if first_game == True:
    if game1 == 'scissors':
        if rd_num == 0:
            print(w)
        else:
            print(l)
            first_game = False
    elif game1 == 'rock':
        if rd_num == 1:
            print(w)
        else:
            print(l)
            first_game = False
    elif game1 == 'paper':
        if rd_num == 2:
            print(w)
        else:
            print(l)
            first_game = False
if first_game == False:
    print('Next game! is Cube random.')
    game2 = rd.randint(1,6)
    player = int(input('Enter your Guess (1 - 6): '))
    if player == game2:
        print('Yes, finaly you are the winner!')
    else:
        print('You lose again!')
if game1 != 'scissors' and game1 != 'rock' and game1 != 'paper':
    print('Your return ans is not match','\n')

print('THE PROGRAM IS END HERE')
print('-----------------------')
print('The num out is ', rd_num)
