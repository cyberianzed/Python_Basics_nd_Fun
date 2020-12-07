

import time

gamecontrol=1

gameboard=[[0,0,0],[0,0,0],[0,0,0]]

def display(a):
    a=a+"\n"
    for i in a:
        print(i,end="")
        time.sleep(0.03)
        
def insertboard(board,possition,symbol):
    a=int(possition[0])
    b=int(possition[1])
    board[a][b]=symbol
    return board

def check(cordinates):
    cordinates=str(cordinates)
    ckeck="abc"
    core=""
    num=""
    a=cordinates[0]
    loop=0
    while loop==0:
        for i in ckeck:
            if a==i:
                num=str(ckeck.index(i))
                loop=1
            
        if num=="":
            a=cordinates[2]
    if a==cordinates[0]:
        core=cordinates[2]+num
    else:
        core=cordinates[0]+num
    return core    
        
    
    
def image(gameboard):
    display("   a ,b ,c \n   ________")
    string1="0 |"
    string2="1 |"
    string3="2 |"
    x=0
    for i in gameboard:
        unit=i
        if x==0:
            string=string1
        elif x==1:
            string=string2
        else:
            string=string3
        for j in unit:
            if j==0:
                string=string+"__,"
            else:
                string=string+j+" ,"
        display(string)
        x=x+1
        
             
               
def gamewon(board):
    win=""
    a=""
    for i in board:
        if i[0]==i[1]==i[2]!=0:
            win=i[0]
    for x in range(0,3):
        for i in board:
            a=a+str(i[x])
        if a[0]==a[1]==a[2]!="0":
            win=a[x]
            a=""
        else:
            a=""
    a=board
    if a[0][0]==a[1][1]==a[2][2]!=0:
        win=a[0][0]
    elif a[2][0]==a[1][1]==a[0][2]!=0:
        win=a[2][0]
    if win=="":
        return None
    else:
        print(win)
        return win
            
def reset(board):
    board=[[0,0,0],[0,0,0],[0,0,0]]
    return board       

def tie(gameboard):
    ti=False
    for i in gameboard:
        for j in i:
            if j==0:
                ti=True
    return ti

def invalid(a):
    if a[1]!=",":
        x=False
    else:
        cd=["a","b","c"]
        num=["0","1","2"]
        if a[0]or a[2]in cd and a[0]or a[2]in num:
            x=True
        else:
            x=False
    return x

def available(board,a):
    if board[int(a[0])][int(a[1])]==0:
        return True
    else:
        return False
    

display("start game")
display("Press y to continue:")
input1=input()

if input1=="y":
    gamecontrol=1
else:
    display("Game Over")
    gamecontrol=0

while gamecontrol==1:
    display("player 1 ,select your symbol o or *")
    player1=input()
    if player1=="o":
        player2="*"
        display("player 2 symbol is *")
    else:
        player2="o"
        display("player 2 symbol is o")

    display("\nThe game board is :\n")
    display("   a ,b ,c \n   ________\n0 |__,__,__\n1 |__,__,__\n2 |__,__,__")
    
    display("\n**for playing in any possition input the indexes as X,X as shown in the table borders**")

    win=0
    turn=1
    while win==0:
        if turn%2==0:
            player="player 2"
            symbol=player2
        else:
            player="player 1"
            symbol=player1
        turn=turn+1
        string="\n"+player+" choose your cordinates"
        display(string)
        
        cordin=1
        while cordin==1:
            cordinates=input()
            if invalid(cordinates)==False:
                display("Invalid Cordinates")
                display("re-enter cordinates")
            else:
                cord=check(cordinates)
                if available(gameboard,cord)==True:
                    cordin=0
                else:
                    display("Possiton Not Available")
                    display("re-enter cordiantes")
                    cordin=1

                    
        gameboard=insertboard(gameboard,cord,symbol)
        image(gameboard)
        winner=gamewon(gameboard)
        if winner==None:
            t=tie(gameboard)
            if t==False:
                display("The game is draw")
                gamecontrol=0
                win=1
            else:
                None
        else:
            if winner==player1:
                display("Player1 wins the game")
                gamecontrol=0
                win=1
            else:
                display("Player2 wins the game")
                gamecontrol=0
                win=1
        if gamecontrol==0:
            gameboard=reset(gameboard)
            display("\nGAME OVER")
            display("\nDo you want to play again y/n")
            lastin=input()
            if lastin=="y":
                gamecontrol=1
            else:
                gamecontrol=0
        else:
            None
    
        
    
    
    
    
