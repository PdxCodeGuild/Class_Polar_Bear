def game(user,computer):
    printMsg = (f'I chose {computer}, ')
    lose = ' you lose.'
    win = ' you win.'

    if user == computer:
        print(f'I chose {computer}, TIE')
    elif user == 'rock':
        if computer == 'paper':
            print(printMsg + lose)
        elif computer == 'scissors':
            print(printMsg + win)
    elif user == 'paper':
        if computer == 'scissors':
            print(printMsg + lose)
        elif computer == 'rock':
            print(printMsg + win)
    elif user == 'scissors':
        if computer == 'rock':
            print(printMsg + lose)
        elif computer == 'paper':
           print(printMsg + win)