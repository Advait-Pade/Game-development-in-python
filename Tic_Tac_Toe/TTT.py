board = {'1':' ','2':' ','3':' ',
        '4': ' ','5':' ','6':' ',
        '7':' ','8':' ','9':' '}
bkeys = []
for key in board:
    bkeys.append(key)

#print(bkeys)

def printboard(board):
    print(board['1']+"/"+board['2']+"/"+board['3'])
    print('-+-+-')

    print(board['4']+"/"+board['5']+"/"+board['6'])
    print('-+-+-')

    print(board['7']+"/"+board['8']+"/"+board['9'])
    print('-+-+-')

def main():
    turn = 'X'
    count = 0

    for i in range(10):
        printboard(board)
        move = input("It is the chance of "+turn+" please enter your position ")

        if board[move] == ' ':
            board[move] = turn
            count += 1
            
        else:
            print("The position you entered is already filled ")
            i-=1
            continue
        if count>=5:

            if board['1']==board['2']==board['3'] != ' ':
                print("Player "+turn+" won the game ")
                printboard(board)
                break
            
            if board['4']==board['5']==board['6'] != ' ':
                print("Player "+turn+" won the game ")
                printboard(board)
                break
            
            if board['7']==board['8']==board['9'] != ' ':
                print("Player "+turn+" won the game ")
                printboard(board)
                break
            
            if board['1']==board['4']==board['7'] != ' ':
                print("Player "+turn+" won the game ")
                printboard(board)
                break
            
            if board['2']==board['5']==board['8'] != ' ':
                print("Player "+turn+" won the game ")
                printboard(board)
                break
            
            if board['3']==board['6']==board['9'] != ' ':
                print("Player "+turn+" won the game ")
                printboard(board)
                break
            
            if board['1']==board['5']==board['9'] != ' ':
                print("Player "+turn+" won the game ")
                printboard(board)
                break
            
            if board['3']==board['5']==board['7'] != ' ':
                print("Player "+turn+" won the game ")
                printboard(board)
                break
            
            if count==9:
                printboard(board)
                print("It is a tie")
            
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
    
    restart = input("Do you want to play again (y/n) ")

    if restart == 'Y' or restart == 'y':
        for key in bkeys:
            board[key] = ' '
        main()
            
if __name__ == "__main__":
    main()