from random import randint
print('what is your name?')
name = input()
print('Hello, ' + name + ' I am Priyanshu here lets play odd even cricket')
print('I hope you are well aware of the rules of the game let me make it clear that you can only score runs between 1 and 6')
print('Time for the toss')
call = input("'even','odd'?")
print('enter toss number')
toss = int(input())
compu = randint(1,7)
player = 0
comp =-1
if ((toss + compu) % 2 == 0 and call == 'even'):
    print('You won what would you like to do')
    choice = input("batting,bowling?")
elif ((toss + compu) % 2 != 0 and call == 'odd'):
    print('You won what would you like to do')
    choice = input("batting,bowling?")
else:
    t = ['batting','bowling']
    choice = t[randint(0,1)]
    print('you lose the toss You will be ' + choice)
if(choice == 'batting'):
    print('You chose to bat start now:')
    score = 0
    while comp != player:
        player = int(input())
        if(player > 6 or player < 0):
            print('that is an invalid choice')
            continue
        comp = randint(1,7)
        if(player!=comp):
            score = score + player
            print('your score = ' + str(score))
        elif(player == comp):
            print('You are out your score is: ' + str(score))
    print('your turn to bowl')
    scorec = 0
    player = 0
    comp = -1
    while comp != player and scorec <= score:
        player = int(input())
        if(player > 6 or player < 0):
            print('that is an invalid choice')
            continue
        comp = randint(1,6)
        if(player!=comp):
            scorec = scorec + comp
            print('Priyanshu score = ' + str(scorec))
        elif(player == comp):
            print('Priyanshu is out his score is: ' + str(scorec))
if(choice == 'bowling'):
    print('You chose to bowl start now:')
    scorec = 0
    while comp != player:
        player = int(input())
        if(player > 6 or player < 0):
            print('that is an invalid choice')
            continue
        comp = randint(1,6)
        if(player!=comp):
            scorec = scorec + comp
            print('Priyanshu score = ' + str(scorec))
        elif(player == comp):
            print('Priyanshu is out his score is: ' + str(scorec))
    print('your turn to bat')
    score = 0
    player = 0
    comp = -1
    while comp != player and score <= scorec:
        player = int(input())
        if(player > 6 or player < 0):
            print('that is an invalid choice')
            continue
        comp = randint(1,6)
        if(player!=comp):
            score = score + player
            print('Your score = ' + str(score))
        elif(player == comp):
            print('You are out your score is: ' + str(score))
if(score > scorec):
    print('Well Played!!! You won')
elif(score < scorec):
    print('You lose loser')
else:
    print('Tie Game')
