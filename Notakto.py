

def printboard(boardlst):
    letter=[]
    if A in boardlst:
        letter.append('A')
    if B in boardlst:
        letter.append('B')
    if C in boardlst:
        letter.append('C')
    print('      '.join(map(str,letter)))
    zipped=list(zip(*boardlst))
    for i in zipped:
        temp=[]
        for j in i:
            temp.append(' '.join(map(str,j)))
        print('  '.join(map(str,temp)))
        
def winall() :
    if win(A) and win(B) and win(C):
        return True
    return False

def win(boardsym):
    for i in range(3):
        if boardsym[i][0]==boardsym[i][1]==boardsym[i][2] or boardsym[1][1]==boardsym[2][2]==boardsym[0][0] or boardsym[0][2]==boardsym[1][1]==boardsym[2][0] or boardsym[1][i]==boardsym[2][i]==boardsym[0][i]:
            return True
    return False

def checkvalid(playerinput):
    while True:
        if (playerinput[0]=='A' or 'B' or 'C') and len(playerinput)==2 and playerinput[1].isnumeric():
            if int(playerinput[1]) in range(9):
                if playerinput[0]=='A' and A in boardlst:
                    if A[int(playerinput[1])//3][int(playerinput[1])%3]!=pie:
                        break
                if playerinput[0]=='B' and B in boardlst:
                    if B[int(playerinput[1])//3][int(playerinput[1])%3]!=pie:
                        break
                if playerinput[0]=='C' and C in boardlst:
                    if C[int(playerinput[1])//3][int(playerinput[1])%3]!=pie:
                        break
        print('Invalid move, please input again')
        playerinput=input(f'Player {turn}: ')
    return playerinput

def ai():
    MAX = 0
    MIN = 10
    bestMove = ""
    
    for num,board in enumerate(boardlst):
        Bnum = remain[num]
        Rulescore = [0,0,0,0,0,0,0,0]

        print(f"\n=={Bnum}==")
        s,placed,emty = CalScore(board)  
        print(f"score for {Bnum} {s}")
        for n, rules in enumerate(potentialWIN):
            matched = 0
            for i in placed:
                if i in rules :
                    matched += 1
            Rulescore[n] = matched
            
        print(f"matched : {Rulescore}")
                
        if 2 in Rulescore and len(remain) >= 2:
            ruleNUM = Rulescore.index(2)
            winningRule = potentialWIN[ruleNUM]
            for i in winningRule:
                if i not in placed:
                    bestMove = Bnum + str(i)
                    print(f"\nBest Move = {bestMove}")
                    return bestMove
            
            
        elif len(placed) == 0 :

            bestMove = Bnum + "4"
            return bestMove

        else :
            if 2 in Rulescore:
                for Rnum, Rs in enumerate(Rulescore):
                    if Rs == 2:
                        for j in potentialWIN[Rnum]:
                            try:
                                emty.remove(j)
                            except:
                                continue
            elif 1 in Rulescore:
                for Rnum, Rs in enumerate(Rulescore):
                    if Rs == 1:
                        for j in potentialWIN[Rnum]:
                            try:
                                emty.remove(j)
                            except:
                                continue


            print(f"can consider: {emty}")
            for n,i in enumerate(s):
                if i >= MAX and (n in emty) and n != 4:
                    MAX = i
                    bestMove = Bnum + str(n)
            if len(placed) >= 2:
                return bestMove



    print(f"\nBest Move = {bestMove}")
    return bestMove
                
    
    
    

def CalScore(boardsym):
    score = [0,0,0,0,0,0,0,0,0]
    
    emty,placed = emtygrid(boardsym)

    
    for i in emty:
        for j in potentialWIN:
            if i in j:
                score[i] = score[i] + 1
    return score,placed,emty
    


def emtygrid(boardsym):
    
    emty = []
    placed =[]
    layer = 0
    for i in boardsym:
        for j in range(0,3):
            if i[j] != "X":
                emty.append(i[j])
            else:
                placed.append(j+layer)
        layer +=3
    print(f"emtygrid = {emty}")
    if len(placed)==0:
        print("all grid is avaliable")
    else:
        print(f"placedgrid = {placed}")
    return emty,placed
                
    
A=[[0,1,2],[3,4,5],[6,7,8]]
B=[[0,1,2],[3,4,5],[6,7,8]]
C=[[0,1,2],[3,4,5],[6,7,8]]
potentialWIN = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
boardlst=[A,B,C]
remain=['A','B','C']
s=3
pie='X'
cycle= {1:2,2:1}
turn=2
    
while winall() is False:
    print(f"remain : {remain}")
    printboard(boardlst)
    turn=cycle[turn]
    if turn == 1:
        print("ai1")
        playerinput= ai()
    else:

        playerinput=(input(f'Player {turn}: '))
    playerinput=checkvalid(playerinput)
    if playerinput[0]=='A':
        A[int(playerinput[1])//3][int(playerinput[1])%3]=pie
    if playerinput[0]=='B':
        B[int(playerinput[1])//3][int(playerinput[1])%3]=pie
    if playerinput[0]=='C':
        C[int(playerinput[1])//3][int(playerinput[1])%3]=pie
    for n,i in enumerate(boardlst):
        if win(i) is True:
            boardlst.remove(i)
            remain.remove(remain[n])
            
if winall():
    print(f'Player {cycle[turn]} wins game')