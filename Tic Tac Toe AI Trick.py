import os
def player(board): #Player Function
    q = 1
    while(q>0):
        choice = int(input("(1) Enter in xy: "))
        i = choice%10
        j = int(choice/10)
        if board[j][i] != "":
            print("Wrong input")
            continue
        else:
            board[j][i] = "X"
            q = q-1
def spec_print(list): #print the grid
    for i in range(5):
        for j in range(5):
            if j==4:
                print(list[j][i])
                break
            else:
                print(list[j][i],end="\t")

def win(board, play):
    for j in range(1,4): #Check horizontal
        i=1
        if board[j][i]==board[j][i+1] and board[j][i]==board[j][i+2] and board[j][i] == play:
            return True
    for i in range(1,4): #Check vertical
        j=1
        if board[j][i]==board[j+1][i] and board[j][i]==board[j+2][i] and board[j][i] == play:
            return True
    if board[1][1] == board[2][2] and board[3][3] == board[2][2] and board[2][2] == play: # Check diagonal
        return True
    elif board[3][1]==board[2][2] and board[2][2]==board[1][3] and board[2][2]== play: # Check diagonal
        return True
    else:
        return False
def scan(a,b,c,play):
    if (a==b and b==play and c=="") or (a==c and c==play and b=="") or (b==c and b==play and a==""):
        return True

def ai(board):
    # To fast win
    for j in range(1,4):
        if scan(board[j][1],board[j][2],board[j][3],"O") == True:
            for i in range(1,4):
                if board[j][i]=="":
                    board[j][i]="O"
                    return
    for j in range(1,4):
        if scan(board[1][j],board[2][j],board[3][j],"O") == True:
            for i in range(1,4):
                if board[i][j]=="":
                    board[i][j]="O"
                    return
    if scan(board[1][1], board[2][2], board[3][3],"O") == True:
        for i in range(1,4):
            if board[i][i]=="":
                board[i][i]="O"
                return
    elif scan(board[1][3],board[2][2],board[3][1],"O") == True:
        for i in range(1,4):
            if board[i][4-i]=="":
                board[i][4-i]="O"
                return
    #To defense
    elif scan(board[1][1], board[2][2], board[3][3],"X") == True:
        for i in range(1,4):
            if board[i][i]=="":
                board[i][i]="O"
                return
    elif scan(board[1][3],board[2][2],board[3][1],"X") == True:
        for i in range(1,4):
            if board[i][4-i]=="":
                board[i][4-i]="O"
                return
    for j in range(1,4):
        if scan(board[j][1],board[j][2],board[j][3],"X") == True:
            for i in range(1,4):
                if board[j][i]=="":
                    board[j][i]="O"
                    return
    for j in range(1,4):
        if scan(board[1][j],board[2][j],board[3][j],"X") == True:
            for i in range(1,4):
                if board[i][j]=="":
                    board[i][j]="O"
                    return
    #To offense
    else:
        if board[2][2]=="":
            board[2][2]="O"
            return
        elif board[1][1] =="" or board[1][3]=="" or board[3][1]=="" or board[3][3]=="":
            for i in range(1,4,2):
                for j in range(1,4,2):
                    if board[j][i]=="":
                        board[j][i]="O"
                        return
        elif board[2][1] =="" or board[1][2]=="" or board[3][2] =="" or board[2][3]=="":
            if board[2][1] =="":
                board[2][1]="O"
                return
            if board[1][2] =="":
                board[1][2]="O"
                return
            if board[3][2] =="":
                board[3][2]="O"
                return
            if board[2][3] =="":
                board[2][3]="O"
                return


#Start program
user = "X"
pc = "O"

board = [[""for i in range(5)]for i in range(5)] #Create board
for i in range(1,4):
    board[i][0]=i
    board[0][i]=i
board[0][0]="0"
board[4][0]='x'
board[0][4]='y'

for i in range(1,5):
    os.system("cls")
    spec_print(board)
    player(board)
    spec_print(board)
    ai(board)
    spec_print(board)
    if win(board,user)==True:
        print("You win")
        input()
        exit()
    elif win(board,pc)==True:
        print("You lose")
        input()
        exit()
os.system("cls")
spec_print(board)
player(board)
spec_print(board)
if win(board, player) == True:
    print("You win")
    input()
else:
    print("Tide")
    input()
