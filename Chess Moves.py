BOARDDIMENSION = 8

def enumerate_moves(x, y):
    potential_moves = []     # moves before clean up function

# ------------------------------------------------------------------------------
##    # resolve pawn moves. 4 possible moves maximally
##    if board[x][y] == "bPawn":
##
##        potential_moves.append([[x+1], [y]])
##
##        # if the pawn is in the second rank (has not moved)
##        try:
##            if board[x+2][y] == "" and x == 1 and board[x+1][y] == "":
##                potential_moves.append([[x+2], [y]])
##        except IndexError:
##            pass
##
##        try:
##            if board[x+1][y+1][0] == "w":
##                potential_moves.append([x+1], [y+1])
##        except IndexError:
##            pass
##
##        try:
##            if board[x+1][y-1][0] == "w":
##                potential_moves.append([x+1], [y-1])
##        except IndexError:
##            pass

# resolve pawn moves. 4 possible moves maximally
    if Board[x][y] == "bPawn":

        potential_moves.append((x+1, y))

        if x == 1:  # if the pawn is in the second rank (has not moved)
            potential_moves.append((x+2, y))

        if x < 7 and y < 7 and Board[x+1][y+1][0] == "w":
            potential_moves.append((x+1, y+1))

        if x < 7 and 0 < y and Board[x+1][y-1][0] == "w":
            potential_moves.append((x+1, y-1))


# ------------------------------------------------------------------------------
##    # resolve knight moves. 8 possible moves maximally
##    elif board[x][y] == "bKnight":
##
##        potential_moves.append([[x+2], [y+1]])
##        potential_moves.append([[x+2], [y-1]])
##        potential_moves.append([[x+1], [y+2]])
##        potential_moves.append([[x+1], [y+2]])
##        potential_moves.append([[x-2], [y-1]])
##        potential_moves.append([[x-2], [y+1]])
##        potential_moves.append([[x-1], [y+2]])
##        potential_moves.append([[x-1], [y-2]])

# resolve knight moves. 8 possible moves maximally
    elif Board[x][y] == "bKnight":
        potential_moves += [(x+2, y+1), (x+2, y-1)
                           ,(x+1, y+2), (x+1, y-2)
                           ,(x-2, y-1), (x-2, y+1)
                           ,(x-1, y+2), (x-1, y-2)]

# ------------------------------------------------------------------------------
##    elif board[x][y] == "bBishop":
##
##        # down and right
##        a = x + 1
##        b = y + 1
##        while (7 > a >= 0 and 7 > b >= 0) and (board[a][b] == ""):
##            potential_moves.append([[a], [b]])
##            try:
##                if board[a+1][b+1][0] == "w":
##                    potential_moves.append([[a+1], [b+1]])
##            except IndexError:
##                pass
##            a += 1
##            b += 1
##
##        # down and left
##        a = x + 1
##        b = y - 1
##        while (7 > a >= 0 and 7 > b >= 0) and (board[a][b] == ""):
##            potential_moves.append([[a], [b]])
##            try:
##                if board[a+1][b-1][0] == "w":
##                    potential_moves.append([[a+1], [b-1]])
##            except IndexError:
##                pass
##            a += 1
##            b -= 1
##
##        # up and right
##        a = x - 1
##        b = y + 1
##        while (7 > a >= 0 and 7 > b >= 0) and (board[a][b] == ""):
##            potential_moves.append([[a], [b]])
##            try:
##                if board[a-1][b+1][0] == "w":
##                    potential_moves.append([[a-1], [b+1]])
##            except IndexError:
##                pass
##            a -= 1
##            b += 1
##
##        # up and left
##        a = x - 1
##        b = y - 1
##        while (7 > a >= 0 and 7 > b >= 0) and (board[a][b] == ""):
##            potential_moves.append([[a], [b]])
##            try:
##                if board[a-1][b-1][0] == "w":
##                    potential_moves.append([[a-1], [b-1]])
##            except IndexError:
##                pass
##            a -= 1
##            b -= 1

    elif Board[x][y] == "bBishop":
        ur = [(x+i, y+i) for i in range(1,8) if 0<=x<8 and 0<=y<8]
        dr = [(x+i, y-i) for i in range(1,8) if 0<=x<8 and 0<=y<8]
        ul = [(x-i, y+i) for i in range(1,8) if 0<=x<8 and 0<=y<8]
        dl = [(x-i, y-i) for i in range(1,8) if 0<=x<8 and 0<=y<8]
        potential_moves += ur + dr + ul + dl  #ur = up/right, etc.

# ------------------------------------------------------------------------------
##    elif board[x][y] == "bRook":
##        # down
##        a = x + 1
##        b = y
##        while (7 > a >= 0 and 7 > b >= 0) and (board[a][b] == ""):
##            potential_moves.append([[a], [b]])
##            try:
##                if board[a+1][b][0] == "w":
##                    potential_moves.append([[a+1], [b]])
##            except IndexError:
##                pass
##            a += 1
##
##        # left
##        a = x
##        b = y - 1
##        while (7 > a >= 0 and 7 > b >= 0) and (board[a][b] == ""):
##            potential_moves.append([[a], [b]])
##            try:
##                if board[a][b-1][0] == "w":
##                    potential_moves.append([[a], [b-1]])
##            except IndexError:
##                pass
##            b -= 1
##
##        # up
##        a = x - 1
##        b = y
##        while (7 > a >= 0 and 7 > b >= 0) and (board[a][b] == ""):
##            potential_moves.append([[a], [b]])
##            try:
##                if board[a-1][b][0] == "w":
##                    potential_moves.append([[a-1], [b]])
##            except IndexError:
##                pass
##            a -= 1
##
##        # right
##        a = x
##        b = y + 1
##        while (7 > a >= 0 and 7 > b >= 0) and (board[a][b] == ""):
##            potential_moves.append([[a], [b]])
##            try:
##                if board[a][b+1][0] == "w":
##                    potential_moves.append([[a], [b+1]])
##            except IndexError:
##                pass
##            b += 1

    elif Board[x][y] == "bRook":
        u = [(x, y+i) for i in range(1,8) if 0<=x<8 and 0<=y<8]
        d = [(x, y-i) for i in range(1,8) if 0<=x<8 and 0<=y<8]
        l = [(x-i, y) for i in range(1,8) if 0<=x<8 and 0<=y<8]
        r = [(x+i, y) for i in range(1,8) if 0<=x<8 and 0<=y<8]
        potential_moves += u + d + l + r

# ------------------------------------------------------------------------------
##    elif board[x][y] == "bQueen":
##        # down and right
##        a = x + 1
##        b = y + 1
##        while (7 > a >= 0 and 7 > b >= 0) and (board[a][b] == ""):
##            potential_moves.append([[a], [b]])
##            try:
##                if board[a+1][b+1][0] == "w":
##                    potential_moves.append([[a+1], [b+1]])
##            except IndexError:
##                pass
##            a += 1
##            b += 1
##
##        # down and left
##        a = x + 1
##        b = y - 1
##        while (7 > a >= 0 and 7 > b >= 0) and (board[a][b] == ""):
##            potential_moves.append([[a], [b]])
##            try:
##                if board[a+1][b-1][0] == "w":
##                    potential_moves.append([[a+1], [b-1]])
##            except IndexError:
##                pass
##            a += 1
##            b -= 1
##
##        # up and right
##        a = x - 1
##        b = y + 1
##        while (7 > a >= 0 and 7 > b >= 0) and (board[a][b] == ""):
##            potential_moves.append([[a], [b]])
##            try:
##                if board[a-1][b+1][0] == "w":
##                    potential_moves.append([[a-1], [b+1]])
##            except IndexError:
##                pass
##            a -= 1
##            b += 1
##
##        # up and left
##        a = x - 1
##        b = y - 1
##        while (7 > a >= 0 and 7 > b >= 0) and (board[a][b] == ""):
##            potential_moves.append([[a], [b]])
##            try:
##                if board[a-1][b-1][0] == "w":
##                    potential_moves.append([[a-1], [b-1]])
##            except IndexError:
##                pass
##            a -= 1
##            b -= 1
##
##        # down
##        a = x + 1
##        b = y
##        while (7 > a >= 0 and 7 > b >= 0) and (board[a][b] == ""):
##            potential_moves.append([[a], [b]])
##            try:
##                if board[a+1][b][0] == "w":
##                    potential_moves.append([[a+1], [b]])
##            except IndexError:
##                pass
##            a += 1
##
##        # left
##        a = x
##        b = y - 1
##        while (7 > a >= 0 and 7 > b >= 0) and (board[a][b] == ""):
##            potential_moves.append([[a], [b]])
##            try:
##                if board[a][b-1][0] == "w":
##                    potential_moves.append([[a], [b-1]])
##            except IndexError:
##                pass
##            b -= 1
##
##        # up
##        a = x - 1
##        b = y
##        while (7 > a >= 0 and 7 > b >= 0) and (board[a][b] == ""):
##            potential_moves.append([[a], [b]])
##            try:
##                if board[a-1][b][0] == "w":
##                    potential_moves.append([[a-1], [b]])
##            except IndexError:
##                pass
##            a -= 1
##
##        # right
##        a = x
##        b = y + 1
##        while (7 > a >= 0 and 7 > b >= 0) and (board[a][b] == ""):
##            potential_moves.append([[a], [b]])
##            try:
##                if board[a][b+1][0] == "w":
##                    potential_moves.append([[a], [b+1]])
##            except IndexError:
##                pass
##            b += 1

    elif Board[x][y] == "bQueen":
        ur = [(x+i, y+i) for i in range(1,8) if 0<=x<8 and 0<=y<8]
        dr = [(x+i, y-i) for i in range(1,8) if 0<=x<8 and 0<=y<8]
        ul = [(x-i, y+i) for i in range(1,8) if 0<=x<8 and 0<=y<8]
        dl = [(x-i, y-i) for i in range(1,8) if 0<=x<8 and 0<=y<8]
        u = [(x, y+i) for i in range(1,8) if 0<=x<8 and 0<=y<8]
        d = [(x, y-i) for i in range(1,8) if 0<=x<8 and 0<=y<8]
        l = [(x-i, y) for i in range(1,8) if 0<=x<8 and 0<=y<8]
        r = [(x+i, y) for i in range(1,8) if 0<=x<8 and 0<=y<8]
        potential_moves += ur + dr + ul + dl + u + d + l + r

# ------------------------------------------------------------------------------

    elif Board[x][y] == "bKing":

        potential_moves.append([[x+1], [y]])
        potential_moves.append([[x+1], [y+1]])
        potential_moves.append([[x], [y+1]])
        potential_moves.append([[x-1], [y+1]])
        potential_moves.append([[x-1], [y]])
        potential_moves.append([[x-1], [y-1]])
        potential_moves.append([[x], [y-1]])
        potential_moves.append([[x+1], [y-1]])

# ------------------------------------------------------------------------------

    moves = append_strip_negatives(potential_moves)
    return moves

class ChessBoard:

  def CreateBoard():
    Board = []
    for Count in range(BOARDDIMENSION + 1):
      Board.append([]) #Creates Array for Columns and Rows
      for Count2 in range(BOARDDIMENSION + 1):
        Board[Count].append("  ") #Gives Column/Row empty values
    return Board

  def DisplayBoard(Board): #Creates visual board of string for the user
    print()
    for RowNo in range(BOARDDIMENSION, 0, -1):
      print("     _______________________")
      print(RowNo, end="   ") #Displays Row values
      for ColumnNo in range(1, BOARDDIMENSION + 1):
        print("|" + Board[RowNo][ColumnNo], end="")
      print("|")
    print("     _______________________")
    print()
    print("      A  B  C  D  E  F  G  H") #Column values
    print()
    print()

  def InitialiseSample(Board, GameChoice): #Sample game in-progress
    for RowNo in range(1, BOARDDIMENSION + 1):
      for ColumnNo in range(1, BOARDDIMENSION + 1):
        Board[RowNo][ColumnNo] = "  "
    Board[1][2] = "BR"
    Board[1][4] = "BK"
    Board[1][8] = "WR"
    Board[2][1] = "WP"
    Board[3][1] = "WK"
    Board[3][2] = "Bk"
    Board[3][8] = "Bk"
    Board[6][8] = "BP"

#Make List of pieces and call values 
  def InitialiseNew(Board, GameChoice): #Creates new game with starting pieces
    for RowNo in range(1, BOARDDIMENSION + 1):
      for ColumnNo in range(1, BOARDDIMENSION + 1):
        Board[RowNo][ColumnNo] = "  "
    Board[1][1] = "WR" #Places pieces in starting places on board
    Board[1][2] = "Wk"
    Board[1][3] = "WB"
    Board[1][4] = "WQ"
    Board[1][5] = "WK"
    Board[1][6] = "WB"
    Board[1][7] = "Wk"
    Board[1][8] = "WR"
    Board[2][1] = "WP"
    Board[2][2] = "WP"
    Board[2][3] = "WP"
    Board[2][4] = "WP"
    Board[2][5] = "WP"
    Board[2][6] = "WP"
    Board[2][7] = "WP"
    Board[2][8] = "WP"
    Board[7][1] = "BP"
    Board[7][2] = "BP"
    Board[7][3] = "BP"
    Board[7][4] = "BP"
    Board[7][5] = "BP"
    Board[7][6] = "BP"
    Board[7][7] = "BP"
    Board[7][8] = "BP"
    Board[8][1] = "BR"
    Board[8][2] = "Bk"
    Board[8][3] = "BB"
    Board[8][4] = "BQ"
    Board[8][5] = "BK"
    Board[8][6] = "BB"
    Board[8][7] = "Bk"
    Board[8][8] = "BR"


####

class GameFunctions:

  def DisplayWhoseTurnItIs(WhoseTurn):
    if WhoseTurn == "W":
      print("It is White's turn")
    else:
      print("It is Black's turn")

  def DisplayWinner(WhoseTurn):
    if WhoseTurn == "W":
      print("Black's King has been captured.  White wins!")
    else:
      print("White's King has been captured.  Black wins!")

  def CheckIfGameWillBeWon(Board, FinishRow, FinishColumn):
    if Board[FinishRow][FinishColumn][1] == "K": #Checks if King piece is captured
      return True
    else:
      return False
                      
  def GetMove(StartSquare, FinishSquare):
    Columns = ["A", "B", "C", "D", "E", "F", "G", "H"] #String values for Column options
    FirstSquare = []
    LastSquare = []
    StartXY = input("Enter square containing piece to move (Column|Row): ") #Gets piece to move
    for i in range (1, len(Columns) + 1):
      if StartXY[0] == Columns[i - 1]: #Turns Column string values into integer values
        FirstSquare.append(str(i))
    FirstSquare.append(StartXY[1])
    FinishXY = input("Enter square to move piece to (Column|Row): ") #Gets square to move piece to
    for i in range (1, len(Columns) + 1):
      if FinishXY[0] == Columns[i - 1]:
        LastSquare.append(str(i))
    LastSquare.append(FinishXY[1])
    StartSquare = ''.join(FirstSquare)
    FinishSquare = ''.join(LastSquare)
    return int(StartSquare), int(FinishSquare)

  def MakeMove(Board, StartRow, StartColumn, FinishRow, FinishColumn, WhoseTurn):
    if WhoseTurn == "W" and FinishRow == 8 and Board[StartRow][StartColumn][1] == "P":
      PawnChange = input("What piece would you like to change your Pawn to? (Rook, Knight, Bishop or Queen)") #Allows Pawn piece change when reaches end of board
      if PawnChange == "Rook" or PawnChange == "Bishop" or PawnChange == "Queen":
        Board[FinishRow][FinishColumn] = "W"+str(PawnChange[0]) #For these 3, adds first letter of piece type
      else:
        Board[FinishRow][FinishColumn] = "Wk" #Provides Knight as an else
      Board[StartRow][StartColumn] = "  "
    elif WhoseTurn == "B" and FinishRow == 1 and Board[StartRow][StartColumn][1] == "P":
      PawnChange = input("What piece would you like to change your Pawn to? (Rook, Knight, Bishop or Queen)")
      if PawnChange == "Rook" or PawnChange == "Bishop" or PawnChange == "Queen":
        Board[FinishRow][FinishColumn] = "B"+str(PawnChange[0])
      else:
        Board[FinishRow][FinishColumn] = "Bk"
      Board[StartRow][StartColumn] = "  "
    else:
      Board[FinishRow][FinishColumn] = Board[StartRow][StartColumn]
      Board[StartRow][StartColumn] = "  "

if __name__ == "__main__":
  Board = ChessBoard.CreateBoard()
  StartSquare = 0 
  FinishSquare = 0
  PlayAgain = 1
  while PlayAgain == 1:
    WhoseTurn = "W"
    GameOver = False
    GameChoice = input("Do you want to play the sample game or a new game(enter S for Sample or N for New)? ")
    if ord(GameChoice) == 83 : #Accepts upper and lowercase values
      GameChoice = chr(ord(GameChoice))
      ChessBoard.InitialiseSample(Board, GameChoice)
    elif ord(GameChoice) == 115:
      GameChoice = chr(ord(GameChoice) - 32)
      ChessBoard.InitialiseSample(Board, GameChoice)
    elif ord(GameChoice) == 78:
      GameChoice = chr(ord(GameChoice))
      ChessBoard.InitialiseNew(Board, GameChoice)
    elif ord(GameChoice) == 110:
      GameChoice = chr(ord(GameChoice) - 32)
      ChessBoard.InitialiseNew(Board, GameChoice)
    while not(GameOver): #Game is not over
      ChessBoard.DisplayBoard(Board)
      GameFunctions.DisplayWhoseTurnItIs(WhoseTurn)
      MoveIsLegal = False
      while not(MoveIsLegal):
        StartSquare, FinishSquare = GameFunctions.GetMove(StartSquare, FinishSquare)
        StartRow = StartSquare % 10 #Gets char [1]
        StartColumn = StartSquare // 10 #Gets char [0]
        FinishRow = FinishSquare % 10
        FinishColumn = FinishSquare // 10
        MoveIsLegal = ChessPiece.CheckMoveIsLegal(Board, StartRow, StartColumn, FinishRow, FinishColumn, WhoseTurn)
        if not(MoveIsLegal):
          print("That is not a legal move - please try again")
      GameOver = GameFunctions.CheckIfGameWillBeWon(Board, FinishRow, FinishColumn)
      GameFunctions.MakeMove(Board, StartRow, StartColumn, FinishRow, FinishColumn, WhoseTurn)
      if GameOver:
        GameFunctions.DisplayWinner(WhoseTurn)
      if WhoseTurn == "W":
        WhoseTurn = "B"
      else:
        WhoseTurn = "W"
    PlayAgain = input("Do you want to play again (enter Y for Yes)? ")
    if ord(PlayAgain) >= 97 and ord(PlayAgain) <= 122: #Accepts upper and lowercase value
      PlayAgain = 1
