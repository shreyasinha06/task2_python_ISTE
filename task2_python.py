def displayBoard(b):
    print('     |     |')
    print('  ' + b[0] + '  |  ' + b[1] + '  |  ' + b[2])
    print('     |     |')
    print('-----------------')
    print('     |     |')
    print('  ' + b[3] + '  |  ' + b[4] + '  |  ' + b[5])
    print('     |     |')
    print('-----------------')
    print('     |     |')
    print('  ' + b[6] + '  |  ' + b[7] + '  |  ' + b[8])

    
def checkWin(b, m):
    return ((b[0] == m and b[1] == m and b[2] == m) or  # H top
            (b[3] == m and b[4] == m and b[5] == m) or  # H mid
            (b[6] == m and b[7] == m and b[8] == m) or  # H bot
            (b[0] == m and b[3] == m and b[6] == m) or  # V left
            (b[1] == m and b[4] == m and b[7] == m) or  # V centre
            (b[2] == m and b[5] == m and b[8] == m) or  # V right
            (b[0] == m and b[4] == m and b[8] == m) or  # LR diag
            (b[2] == m and b[4] == m and b[6] == m))  # RL diag

def checkDraw(b):
    return ' ' not in b

def getBoardCopy(b):
    
    dupeBoard = []
    for j in b:
        dupeBoard.append(j)
    return dupeBoard

def testWinMove(b, mark, i):
    
    bCopy = getBoardCopy(b)
    bCopy[i] = mark
    return checkWin(bCopy, mark)
    
    
def testForkMove(b, mark, i):
   
    bCopy = getBoardCopy(b)
    bCopy[i] = mark
    winningMoves = 0
    for j in range(0, 9):
        if testWinMove(bCopy, mark, j) and bCopy[j] == ' ':
            winningMoves += 1
    return winningMoves >= 2

def getComputerMove(b):

    for i in range(0, 9):
        if b[i] == ' ' and testWinMove(b, 'X', i):
            return i

    for i in range(0, 9):
        if b[i] == ' ' and testWinMove(b, '0', i):
            return i

    for i in range(0, 9):
        if b[i] == ' ' and testForkMove(b, 'X', i):
            return i
   
    playerForks = 0
    for i in range(0, 9):
        if b[i] == ' ' and testForkMove(b, '0', i):
            playerForks += 1
            tempMove = i
    if playerForks == 1:
        return tempMove
    elif playerForks == 2:
        for j in [1, 3, 5, 7]:
            if b[j] == ' ':
                return j

    if b[4] == ' ':
        return 4

    for i in [0, 2, 6, 8]:
        if b[i] == ' ':
            return i

    for i in [1, 3, 5, 7]:
        if b[i] == ' ':
            return i    
            
            
Playing = True
while Playing:
    InGame = True
    board = [' '] * 9
    print('Would you like to go first or second? (1/2)')
    if input() == '1':
        playerMarker = '0'
    else:
        playerMarker = 'X'
    displayBoard(board)

    while InGame:
        if playerMarker == '0':
            print('Player go: (0-8)')
            move = int(input())
            if board[move] != ' ':
                print('Invalid move!')
                continue
        else:
            move = getComputerMove(board)
        board[move] = playerMarker
        if checkWin(board, playerMarker):
            InGame = False
            displayBoard(board)
            if playerMarker == '0':
                print('Noughts won!')
            else:
                print('Crosses won!')
            continue
        if checkDraw(board):
            InGame = False
            displayBoard(board)
            print('It was a draw!')
            continue
        displayBoard(board)
        if playerMarker == '0':
            playerMarker = 'X'
        else:
            playerMarker = '0'

    print('Type y to keep playing')
    inp = input()
    if inp != 'y' and inp != 'Y':
        Playing = False 