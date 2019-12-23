## x = Column
## y = Row
##Board[x][y]
####only board set up correctly again, movement needs sorting still
BOARDDIMENSION = 8

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
        print("|" + Board[ColumnNo][RowNo], end="")
      print("|")
    print("     _______________________")
    print()
    print("      A  B  C  D  E  F  G  H") #Column values
    print()
    print()

  def InitialiseSample(Board, GameChoice): #Sample game in-progress
    for ColumnNo in range(1, BOARDDIMENSION + 1):
      for RowNo in range(1, BOARDDIMENSION + 1):
        Board[ColumnNo][RowNo] = "  "
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
    for ColumnNo in range(1, BOARDDIMENSION + 1):
      for RowNo in range(1, BOARDDIMENSION + 1):
        Board[ColumnNo][RowNo] = "  "
    Board[1][1] = "WR" #Places pieces in starting places on board
    Board[2][1] = "Wk"
    Board[3][1] = "WB"
    Board[4][1] = "WQ"
    Board[5][1] = "WK"
    Board[6][1] = "WB"
    Board[7][1] = "Wk"
    Board[8][1] = "WR"
    Board[1][2] = "WP"
    Board[2][2] = "WP"
    Board[3][2] = "WP"
    Board[4][2] = "WP"
    Board[5][2] = "WP"
    Board[6][2] = "WP"
    Board[7][2] = "WP"
    Board[8][2] = "WP"
    Board[1][7] = "BP"
    Board[2][7] = "BP"
    Board[3][7] = "BP"
    Board[4][7] = "BP"
    Board[5][7] = "BP"
    Board[6][7] = "BP"
    Board[7][7] = "BP"
    Board[8][7] = "BP"
    Board[1][8] = "BR"
    Board[2][8] = "Bk"
    Board[3][8] = "BB"
    Board[4][8] = "BQ"
    Board[5][8] = "BK"
    Board[6][8] = "BB"
    Board[7][8] = "Bk"
    Board[8][8] = "BR"

####

class ChessPiece:

##

  def EnumerateMoves(x, y):
    PotentialMoves = []
    if Board[x][y] == "bPawn":
      PotentialMoves.append((x+1, y))
      if x == 2:  # if the pawn is in the second rank (has not moved)
        PotentialMoves.append((x+2, y))
      if x < BOARDDIMENSION and y < BOARDDIMENSION and Board[x+1][y+1][0] == "w":
        PotentialMoves.append((x+1, y+1))
      if x < BOARDDIMENSION and 0 < y and Board[x+1][y-1][0] == "w":
        PotentialMoves.append((x+1, y-1))
    elif Board[x][y] == "bRook":
      U = [(x, y+i) for i in range(1, BOARDDIMENSION) if 0<=x<BOARDDIMENSION and 0<=y<BOARDDIMENSION]
      D = [(x, y-i) for i in range(1, BOARDDIMENSION) if 0<=x<BOARDDIMENSION and 0<=y<BOARDDIMENSION]
      L = [(x-i, y) for i in range(1, BOARDDIMENSION) if 0<=x<BOARDDIMENSION and 0<=y<BOARDDIMENSION]
      R = [(x+i, y) for i in range(1, BOARDDIMENSION) if 0<=x<BOARDDIMENSION and 0<=y<BOARDDIMENSION]
      PotentialMoves += U + D + L + R
    elif Board[x][y] == "bKnight":
      PotentialMoves += [(x+2, y+1), (x+2, y-1)
                          , (x+1, y+2), (x+1, y-2)
                          , (x-2, y-1), (x-2, y+1)
                          , (x-1, y+2), (x-1, y-2)]
    elif Board[x][y] == "bBishop":
      Ur = [(x+i, y+i) for i in range(1, BOARDDIMENSION) if 0<=x<BOARDDIMENSION and 0<=y<BOARDDIMENSION]
      Dr = [(x+i, y-i) for i in range(1, BOARDDIMENSION) if 0<=x<BOARDDIMENSION and 0<=y<BOARDDIMENSION]
      Ul = [(x-i, y+i) for i in range(1, BOARDDIMENSION) if 0<=x<BOARDDIMENSION and 0<=y<BOARDDIMENSION]
      Dl = [(x-i, y-i) for i in range(1, BOARDDIMENSION) if 0<=x<BOARDDIMENSION and 0<=y<BOARDDIMENSION]
      potential_moves += Ur + Dr + Ul + Dl  #ur = up/right, etc.
    elif Board[x][y] == "bQueen":
      Ur = [(x+i, y+i) for i in range(1, BOARDDIMENSION) if 0<=x<BOARDDIMENSION and 0<=y<BOARDDIMENSION]
      Dr = [(x+i, y-i) for i in range(1, BOARDDIMENSION) if 0<=x<BOARDDIMENSION and 0<=y<BOARDDIMENSION]
      Ul = [(x-i, y+i) for i in range(1, BOARDDIMENSION) if 0<=x<BOARDDIMENSION and 0<=y<BOARDDIMENSION]
      Dl = [(x-i, y-i) for i in range(1, BOARDDIMENSION) if 0<=x<BOARDDIMENSION and 0<=y<BOARDDIMENSION]
      U = [(x, y+i) for i in range(1, BOARDDIMENSION) if 0<=x<BOARDDIMENSION and 0<=y<BOARDDIMENSION]
      D = [(x, y-i) for i in range(1, BOARDDIMENSION) if 0<=x<BOARDDIMENSION and 0<=y<BOARDDIMENSION]
      L = [(x-i, y) for i in range(1, BOARDDIMENSION) if 0<=x<BOARDDIMENSION and 0<=y<BOARDDIMENSION]
      R = [(x+i, y) for i in range(1, BOARDDIMENSION) if 0<=x<BOARDDIMENSION and 0<=y<BOARDDIMENSION]
      PotentialMoves += Ur + Dr + Ul + Dl + U + D + L + R
    elif Board[x][y] == "King":
      PotentialMoves += [(x+1, y+1), (x-1, y-1)
                         , (x+1, y-1), (x-1, y+1)
                         , (x+1, y+0), (x+0, y+1)
                         , (x-1, y+0), (x+0, y-1)]

    Moves = append_strip_negatives(PotentialMoves)
    return Moves

##
#### issue with calling functions (if statements)

  def CheckMoveIsLegal(Board, StartColumn, StartRow, FinishColumn, FinishRow, WhoseTurn):
    MoveIsLegal = True
    print ((FinishColumn == StartColumn), (FinishRow == StartRow))
    if (FinishColumn == StartColumn) and (FinishRow == StartRow): #Piece does not move
      MoveIsLegal = False
    else:
      print ("test")
#### Column/Row need swapping somewhere
      Colour = Board[StartColumn][StartRow][0]
      Type = Board[StartColumn][StartRow][1]
      print (Colour, Type)
      print ("test2")
      if WhoseTurn == "W": #Check movement for White turn
        if Colour != "W":
          MoveIsLegal = False
        if Board[FinishColumn][FinishRow][0] == "W":
          MoveIsLegal = False
      else: #Check movement for Black turn
        if Colour != "B":
          MoveIsLegal = False
        if Board[FinishColumn][FinishRow][0] == "B":
          MoveIsLegal = False
      if MoveIsLegal == True: #If colour movement acceptable, checks piece movement
        if Type == "P":
          PawnMoves = ChessPiece.Pawn.GetMoves(Board, StartColumn, StartRow, Colour)
          print (PawnMoves)
          if Board[FinishColumn][FinishRow] in PawnMoves:
            MoveIsLegal = True
        elif Type == "R":
          RookMoves = ChessPiece.Rook.GetMoves(Board, StartColumn, StartRow)
          print (RookMoves)
          if Board[FinishColumn][FinishRow] in RookMoves:
            MoveIsLegal = True
        elif Type == "k":
          KnightMoves = ChessPiece.Knight.GetMoves(Board, StartColumn, StartRow)
          print (KnightMoves)
          if Board[FinishColumn][FinishRow] in KnightMoves:
            MoveIsLegal = True
        elif Type == "B":
          BishopMoves = ChessPiece.Bishop.GetMoves(Board, StartColumn, StartRow)
          print (BishopMoves)
          if Board[FinishColumn][FinishRow] in BishopMoves:
            MoveIsLegal = True
        elif Type == "Q":
          QueenMoves = ChessPiece.Queen.GetMoves(Board, StartColumn, StartRow)
          print (QueenMoves)
          if Board[FinishColumn][FinishRow] in QueenMoves:
            MoveIsLegal = True
        elif Type == "K":
          KingMoves = ChessPiece.King.GetMoves(Board, StartColumn, StartRow)
          print (KingMoves)
          if Board[FinishColumn][FinishRow] in KingMoves:
            MoveIsLegal = True
      else:
        MoveIsLegal = False
    return MoveIsLegal

##

  class Pawn:
    
    def GetMoves(Board, StartColumn, StartRow, Colour):
      PotentialMoves = []
      if Colour == "W":
        if Board[StartColumn][StartRow][1] == "P":
          PotentialMoves.append((StartColumn, StartRow+1))
          if StartRow == 2:  # if first move
            PotentialMoves.append((StartColumn, StartRow+2))
          if StartRow < BOARDDIMENSION and StartColumn < BOARDDIMENSION and Board[StartColumn+1][StartRow+1][0] == "B":
            PotentialMoves.append((StartColumn+1, StartRow+1))
          if StartRow < BOARDDIMENSION and 0 < StartColumn and Board[StartColumn-1][StartRow+1][0] == "B":
            PotentialMoves.append((StartColumn-1, StartRow+1))
      elif Colour == "B":
        if Board[StartColumn][StartRow][1] == "P":
          PotentialMoves.append((StartColumn, StartRow-1))
          if StartRow == 7:  # if first move
            PotentialMoves.append((StartColumn, StartRow-2))
          if StartRow < BOARDDIMENSION and StartColumn < BOARDDIMENSION and Board[StartColumn+1][StartRow-1][0] == "W":
            PotentialMoves.append((StartColumn+1, StartRow-1))
          if StartRow < BOARDDIMENSION and 0 < StartColumn and Board[StartColumn-1][StartRow-1][0] == "W":
            PotentialMoves.append((StartColumn-1, StartRow-1))
      print (PotentialMoves)
      return PotentialMoves
##

  class Rook:

    def GetMoves(Board, StartColumn, StartRow):
      PotentialMoves = []
      print (PotentialMoves)
      if Board[StartColumn][StartRow][1] == "R":
##        if 0<=StartColumn<BOARDDIMENSION and 0<=StartRow<BOARDDIMENSION:
##          for i in range (1, BOARDDIMENSION):
##            PotentialMoves.append(StartColumn+i, StartRow)
##            PotentialMoves.append(StartColumn-i, StartRow)
##            PotentialMoves.append(StartColumn, StartRow-i)
##            PotentialMoves.append(StartColumn, StartRow+i)    
##        U = [(StartColumn+i, StartRow) for i in range(1, BOARDDIMENSION) if 0<=StartColumn<BOARDDIMENSION and 0<=StartRow<BOARDDIMENSION]
##        D = [(StartColumn-i, StartRow) for i in range(1, BOARDDIMENSION) if 0<=StartColumn<BOARDDIMENSION and 0<=StartRow<BOARDDIMENSION]
##        L = [(StartColumn, StartRow-i) for i in range(1, BOARDDIMENSION) if 0<=StartColumn<BOARDDIMENSION and 0<=StartRow<BOARDDIMENSION]
##        R = [(StartColumn, StartRow+i) for i in range(1, BOARDDIMENSION) if 0<=StartColumn<BOARDDIMENSION and 0<=StartRow<BOARDDIMENSION]
##        PotentialMoves = ''.join(U)
##        PotentialMoves.append(D)
##        PotentialMoves.append(L)
##        PotentialMoves.append(R)
        PotentialMoves.append((StartColumn+i, StartRow) for i in range(1, BOARDDIMENSION) if 0<=StartColumn<BOARDDIMENSION and 0<=StartRow<BOARDDIMENSION)
        print (PotentialMoves)
        PotentialMoves.append((StartColumn-i, StartRow) for i in range(1, BOARDDIMENSION) if 0<=StartColumn<BOARDDIMENSION and 0<=StartRow<BOARDDIMENSION)
        PotentialMoves.append((StartColumn, StartRow+i) for i in range(1, BOARDDIMENSION) if 0<=StartColumn<BOARDDIMENSION and 0<=StartRow<BOARDDIMENSION)
        PotentialMoves.append((StartColumi, StartRow-1) for i in range(1, BOARDDIMENSION) if 0<=StartColumn<BOARDDIMENSION and 0<=StartRow<BOARDDIMENSION)
      return PotentialMoves

##

  class Knight:

    def GetMoves(Board, StartColumn, StartRow):
      PotentialMoves = []
      PotentialMoves.append((StartColumn+2, StartRow+1))
      PotentialMoves.append((StartColumn+2, StartRow-1))
      PotentialMoves.append((StartColumn+1, StartRow+2))
      PotentialMoves.append((StartColumn+1, StartRow-2))
      PotentialMoves.append((StartColumn-2, StartRow-1))
      PotentialMoves.append((StartColumn-2, StartRow+1))
      PotentialMoves.append((StartColumn-1, StartRow+2))
      PotentialMoves.append((StartColumn-1, StartRow-2))
      print (PotentialMoves)
      for i in range (0, 8):
        print (i+1)
        print (len(PotentialMoves))
        if PotentialMoves[i][0] <= 0 or PotentialMoves[i][0] >=9:
          del PotentialMoves[i]
        if PotentialMoves[i][1] <= 0 or PotentialMoves[i][1] >=9:
          del PotentialMoves[i]
        print (PotentialMoves)
      return PotentialMoves

#### 

##

  class Bishop: ##Can move through pieces atm

    def GetMoves(Board, StartColumn, StartRow):
      PotentialMoves = []
      Ur = [(StartColumn+i, StartRow+i) for i in range(1, BOARDDIMENSION) if 0<=x<BOARDDIMENSION and 0<=y<BOARDDIMENSION]
      Dr = [(StartColumn+i, StartRow-i) for i in range(1, BOARDDIMENSION) if 0<=x<BOARDDIMENSION and 0<=y<BOARDDIMENSION]
      Ul = [(StartColumn-i, StartRow+i) for i in range(1, BOARDDIMENSION) if 0<=x<BOARDDIMENSION and 0<=y<BOARDDIMENSION]
      Dl = [(StartColumn-i, StartRow-i) for i in range(1, BOARDDIMENSION) if 0<=x<BOARDDIMENSION and 0<=y<BOARDDIMENSION]
      PotentialMoves += Ur + Dr + Ul + Dl  #Ur = up/right, etc.
      return PotentialMoves

##

  class Queen: ##Can move through pieces atm via diagonal movement

    def GetMoves(Board, StartColumn, StartRow):
      PotentialMoves = []
##      for i in range(1, BOARDDIMENSION):
##        while Board[][] != " ":
      Ur = [(StartColumn+i, StartRow+i) for i in range(1, BOARDDIMENSION) if 0<=StartColumn<BOARDDIMENSION and 0<=StartRow<BOARDDIMENSION]
      Dr = [(StartColumn+i, StartRow-i) for i in range(1, BOARDDIMENSION) if 0<=StartColumn<BOARDDIMENSION and 0<=StartRow<BOARDDIMENSION]
      Ul = [(StartColumn-i, StartRow+i) for i in range(1, BOARDDIMENSION) if 0<=StartColumn<BOARDDIMENSION and 0<=StartRow<BOARDDIMENSION]
      Dl = [(StartColumn-i, StartRow-i) for i in range(1, BOARDDIMENSION) if 0<=StartColumn<BOARDDIMENSION and 0<=StartRow<BOARDDIMENSION]
      U = [(StartColumn, StartRow+i) for i in range(1, BOARDDIMENSION) if 0<=StartColumn<BOARDDIMENSION and 0<=StartRow<BOARDDIMENSION]
      D = [(StartColumn, StartRow-i) for i in range(1, BOARDDIMENSION) if 0<=StartColumn<BOARDDIMENSION and 0<=StartRow<BOARDDIMENSION]
      L = [(StartColumn-i, StartRow) for i in range(1, BOARDDIMENSION) if 0<=StartColumn<BOARDDIMENSION and 0<=StartRow<BOARDDIMENSION]
      R = [(StartColumn+i, StartRow) for i in range(1, BOARDDIMENSION) if 0<=StartColumn<BOARDDIMENSION and 0<=StartRow<BOARDDIMENSION]
      PotentialMoves += Ur + Dr + Ul + Dl + U + D + L + R
      return PotentialMoves

##

  class King:

    def GetMoves(Board, StartColumn, StartRow):
      PotentialMoves = []
      PotentialMoves += [(StartColumn+1, StartRow+1), (StartColumn-1, StartRow-1)
                         , (StartColumn+1, StartRow-1), (StartColumn-1, StartRow+1)
                         , (StartColumn+1, StartRow+0), (StartColumn+0, StartRow+1)
                         , (StartColumn-1, StartRow+0), (StartColumn+0, StartRow-1)]
      return PotentialMoves

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

  def CheckIfGameWillBeWon(Board, FinishColumn, FinishRow):
    if Board[FinishColumn][FinishRow][1] == "K": #Checks if King piece is captured
      return True
    else:
      return False
                      
  def GetMove(StartSquare, FinishSquare):
    Columns = ["A", "B", "C", "D", "E", "F", "G", "H"] #String values for Column options
    FirstSquare = []
    LastSquare = []
    StartXY = input("Enter square containing piece to move (Column|Row): ") #Gets piece to move
    for i in range (1, len(Columns) + 1):
      if StartXY[0] == Columns[i - 1]: #Converts Column string values into integer values
        FirstSquare.append(str(i))
    FirstSquare.append(StartXY[1])
    FinishXY = input("Enter square to move piece to (Column|Row): ") #Gets square to move piece to
    for i in range (1, len(Columns) + 1):
      if FinishXY[0] == Columns[i - 1]:
        LastSquare.append(str(i))
    LastSquare.append(FinishXY[1])
    StartSquare = ''.join(FirstSquare)
##
    print (StartSquare)
##
    FinishSquare = ''.join(LastSquare)
##
    print (FinishSquare)
##
    return int(StartSquare), int(FinishSquare)

  def MakeMove(Board, StartColumn, StartRow, FinishColumn, FinishRow, WhoseTurn):
    if WhoseTurn == "W" and FinishRow == 8 and Board[StartColumn][StartRow][1] == "P": #If Pawn reaches last rank for either side
      PawnChange = input("What piece would you like to change your Pawn to? (Rook, Knight, Bishop or Queen)") #Asks user what piece Pawn shoudl become
      if PawnChange == "Rook" or PawnChange == "Bishop" or PawnChange == "Queen":
        Board[FinishColumn][FinishRow] = "W"+str(PawnChange[0]) #For these 3 adds first letter of piece type, changes Pawn into a different piece
      else:
        Board[FinishColumn][FinishRow] = "Wk" #Pawn becomes Knight as an else
      Board[StartColumn][StartRow] = "  "
    elif WhoseTurn == "B" and FinishRow == 1 and Board[StartColumn][StartRow][1] == "P":
      PawnChange = input("What piece would you like to change your Pawn to? (Rook, Knight, Bishop or Queen)")
      if PawnChange == "Rook" or PawnChange == "Bishop" or PawnChange == "Queen":
        Board[FinishColumn][FinishRow] = "B"+str(PawnChange[0])
      else:
        Board[FinishColumn][FinishRow] = "Bk"
      Board[StartColumn][StartRow] = "  "
    else:
      Board[FinishColumn][FinishRow] = Board[StartColumn][StartRow]
      Board[StartColumn][StartRow] = "  "

####

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
        StartColumn = StartSquare // 10 #Gets char [0]
        StartRow = StartSquare % 10 #Gets char [1]
####[Column][Row]
        print (StartColumn, StartRow)
        FinishColumn = FinishSquare // 10
        FinishRow = FinishSquare % 10
        print (FinishColumn, FinishRow)
        MoveIsLegal = ChessPiece.CheckMoveIsLegal(Board, StartColumn, StartRow, FinishColumn, FinishRow, WhoseTurn)
        if not(MoveIsLegal):
          print("That is not a legal move - please try again")
      GameOver = GameFunctions.CheckIfGameWillBeWon(Board, FinishColumn, FinishRow)
      GameFunctions.MakeMove(Board, StartColumn, StartRow, FinishColumn, FinishRow, WhoseTurn)
      if GameOver:
        GameFunctions.DisplayWinner(WhoseTurn)
      if WhoseTurn == "W":
        WhoseTurn = "B"
      else:
        WhoseTurn = "W"
    PlayAgain = input("Do you want to play again (enter Y for Yes)? ")
    if ord(PlayAgain) >= 97 and ord(PlayAgain) <= 122: #Accepts upper and lowercase value
      PlayAgain = 1
