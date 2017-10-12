b1=["_", "_", "_"]
b2=["_", "_", "_"]
b3=["_", "_", "_"]
a=[b1, b2 , b3]

player1='X'
player2='O'


def played(symbol):
    if symbol!='_':
        return True
    else:
        return False


def checkForWinner(connected, symbol):
    
    if connected==3:
        
        if symbol=='X':
            winner="player1(X)"
            
        elif symbol=='O':
            winner="player2(O)"
            
        print(winner + " wins!")

        return True
    return False

def check(colrowdiag):
    
    if colrowdiag=="COLUMN":
        for i in range(3):
            connected=0
            for j in range(3):
                if j==0 and played(a[i][j]):
                    symbol=a[i][j]
                    
                if symbol==a[i][j]:
                    connected+=1
                    
                if connected==3:
                    return connected, symbol
                
        return connected, symbol

    
    if colrowdiag=="ROW":
        for j in range(3):
            connected=0
            for i in range(3):
                if i==0 and played(a[i][j]):
                    symbol=a[i][j]
                    
                if symbol==a[i][j]:
                    connected+=1
                    
                if connected==3:
                    return connected, symbol
                
        return connected, symbol
    
    
    if colrowdiag=="DIAGONAL":
        pobeda=0
        for i in range(3):
            connected=0
            
            if i==0 and played(a[i][i]):
                symbol=a[i][i]
                
            else:
                break
            
            if a[i][i]==symbol:
                connected+=1

            if connected==3:
                pobeda=1
                return connected, symbol, pobeda

        return connected, symbol, pobeda

        for i in range(2,-1,-1):
            connected=0
            if i==0 and played(a[i][i]):
                symbol=a[i][i]
                    
            if symbol==a[i][i]:
                connected+=1
                
            if connected==3:
                    return connected, symbol, pobeda
                
        return connected, symbol, pobeda
            
                

while 1:
    player1x, player1y = int(input()), int(input())
    if a[player1x][player1y]!='_':
        print("polje je popunjeno!")
        player1x, player1y = int(input()), int(input())
    a[player1x][player1y]=player1
    
    for i in range(3):
        for j in range(3):
            print(a[i][j],end=' ')
        print()

    
    connected, symbol = check("ROW")
    
    if checkForWinner(connected, symbol):
        break

    connected, symbol = check("COLUMN")

    if checkForWinner(connected, symbol):
        break

    connected, symbol, pobeda = check("DIAGONAL")

    print(pobeda)
    
    if checkForWinner(connected, symbol):
        break
    

    player2x, player2y = int(input()), int(input())
    if a[player2x][player2y]!='_':
        print("polje je popunjeno!")
        player2x, player2y = int(input()), int(input())
    a[player2x][player2y]=player2
    
    for i in range(3):
        for j in range(3):
            print(a[i][j], end=' ')
        print()


    connected, symbol = check("ROW")
    
    if checkForWinner(connected, symbol):
        break

    connected, symbol = check("COLUMN")

    if checkForWinner(connected, symbol):
        break
    
    connected, symbol, pobeda = check("DIAGONAL")
    
    if checkForWinner(connected, symbol):
        break




    
