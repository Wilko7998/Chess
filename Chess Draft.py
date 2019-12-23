#Need to use Classes in final version

BOARDDIMENSION = 8 #Length and Width of Board

def CreateBoard(): #Creates List for horizontal and vertical attributes of board
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
  if GameChoice == "S":
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
  else:
    for RowNo in range(1, BOARDDIMENSION + 1):
      for ColumnNo in range(1, BOARDDIMENSION + 1):
        if RowNo == 2:
          Board[RowNo][ColumnNo] = "BP"
        elif RowNo == 7:
          Board[RowNo][ColumnNo] = "WP"
        elif RowNo == 1 or RowNo == 8:
          if RowNo == 1:
            Board[RowNo][ColumnNo] = "B"
          if RowNo == 8:
            Board[RowNo][ColumnNo] = "W"
          if ColumnNo == 1 or ColumnNo == 8:
            Board[RowNo][ColumnNo] = Board[RowNo][ColumnNo] + "R"
          elif ColumnNo == 2 or ColumnNo == 7:
            Board[RowNo][ColumnNo] = Board[RowNo][ColumnNo] + "k"
          elif ColumnNo == 3 or ColumnNo == 6:
            Board[RowNo][ColumnNo] = Board[RowNo][ColumnNo] + "B"
          elif ColumnNo == 4:
            Board[RowNo][ColumnNo] = Board[RowNo][ColumnNo] + "Q"
          elif ColumnNo == 5:
            Board[RowNo][ColumnNo] = Board[RowNo][ColumnNo] + "K"
        else:
          Board[RowNo][ColumnNo] = "  "

#Make List of pieces and call values 
def InitialiseNew(Board, GameChoice):
  if GameChoice == "N": #New game chosen
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

#Pawn #Done, has 2-space beginning move, can change into any piece when reaches back (not Pawn/King)
def CheckPawnMoveIsLegal(Board, StartRow, StartColumn, FinishRow, FinishColumn, ColourOfPiece):
  CheckPawnMoveIsLegal = False
  if ColourOfPiece == "W": #White piece 
    if StartRow == 2:
      if FinishRow == StartRow + 2 or FinishRow == StartRow + 1: #Checks for 1 or 2-space first move
        if FinishColumn == StartColumn and Board[FinishRow][FinishColumn] == "  ":
          CheckPawnMoveIsLegal = True
    if FinishRow == StartRow + 1:
      if FinishColumn == StartColumn and Board[FinishRow][FinishColumn] == "  ":
        CheckPawnMoveIsLegal = True
      elif abs(FinishColumn - StartColumn) == 1 and Board[FinishRow][FinishColumn][0] == "B":
        CheckPawnMoveIsLegal = True
  elif StartRow == 7: #Black piece
    if FinishRow == StartRow - 2 or FinishRow == StartRow - 1:
      if FinishColumn == StartColumn and Board[FinishRow][FinishColumn] == "  ":
        CheckPawnMoveIsLegal = True
  elif FinishRow == StartRow - 1:
    if FinishColumn == StartColumn and Board[FinishRow][FinishColumn] == "  ":
      CheckPawnMoveIsLegal = True
    elif abs(FinishColumn - StartColumn) == 1 and Board[FinishRow][FinishColumn][0] == "W":
      CheckPawnMoveIsLegal = True
  return CheckPawnMoveIsLegal

#King #Done #Needs Check/mate function
#Check = Check attempted King move with other 1-turn moves of opposition pieces, do not allow move if final squares are the same for each move
#Checkmate = Enumerate all possible King moves with 1-turn moves of opposition, do not allow if final squares for King and opposition are equal
#Checkmate Cont. = Check for Check and Checkmate at start of each players turn for each side
#Checkmate Cont.2 = Checkmate only if no possible King moves and if a piece cannot be sacrificed to guard
def CheckKingMoveIsLegal(Board, StartRow, StartColumn, FinishRow, FinishColumn):
  CheckKingMoveIsLegal = False
  if abs(FinishColumn - StartColumn) <= 1 and abs(FinishRow - StartRow) <= 1: #Move is within 1-space from start
    CheckKingMoveIsLegal = True
  return CheckKingMoveIsLegal

#Rook #Done
def CheckRookMoveIsLegal(Board, StartRow, StartColumn, FinishRow, FinishColumn):
  CheckRookMoveIsLegal = False
  RowDifference = FinishRow - StartRow
  ColumnDifference = FinishColumn - StartColumn
  if RowDifference == 0: #Vertical movement
    if ColumnDifference >= 1:
      CheckRookMoveIsLegal = True
      for Count in range(1, ColumnDifference): #+ve vertical movement
        if Board[StartRow][StartColumn + Count] != "  ": 
          CheckRookMoveIsLegal = False
    elif ColumnDifference <= -1:
      CheckRookMoveIsLegal = True
      for Count in range(-1, ColumnDifference, -1): #-ve vertical movement
        if Board[StartRow][StartColumn + Count] != "  ":
          CheckRookMoveIsLegal = False
  elif ColumnDifference == 0: #Horizontal movement
    if RowDifference >= 1:
      CheckRookMoveIsLegal = True
      for Count in range(1, RowDifference): #+ve horizontal movement
        if Board[StartRow + Count][StartColumn] != "  ":
          CheckRookMoveIsLegal = False
    elif RowDifference <= -1:
      CheckRookMoveIsLegal = True
      for Count in range(-1, RowDifference, -1): #-ve horizontal movement
        if Board[StartRow + Count][StartColumn] != "  ":
          CheckRookMoveIsLegal = False
  return CheckRookMoveIsLegal

#Bishop #Done
def CheckBishopMoveIsLegal(Board, StartRow, StartColumn, FinishRow, FinishColumn):
  CheckBishopMoveIsLegal = False
  if abs(FinishColumn - StartColumn) >= 1 and abs(FinishRow - StartRow) >= 1: #Diagonal movement unlimited
    CheckBishopMoveIsLegal = True
  return CheckBishopMoveIsLegal

#Queen #Done
def CheckQueenMoveIsLegal(Board, StartRow, StartColumn, FinishRow, FinishColumn):
  CheckQueenMoveIsLegal = False
  if abs(FinishColumn - StartColumn) >= 1 and abs(FinishRow - StartRow) >= 1: #Bishop check move sequence
    CheckQueenMoveIsLegal = True
  RowDifference = FinishRow - StartRow #Rook check move sequence
  ColumnDifference = FinishColumn - StartColumn
  if RowDifference == 0:
    if ColumnDifference >= 1:
      CheckQueenMoveIsLegal = True
      for Count in range(1, ColumnDifference):
        if Board[StartRow][StartColumn + Count] != "  ":
          CheckQueenMoveIsLegal = False
    elif ColumnDifference <= -1:
      CheckQueenMoveIsLegal = True
      for Count in range(-1, ColumnDifference, -1):
        if Board[StartRow][StartColumn + Count] != "  ":
          CheckQueenMoveIsLegal = False
  elif ColumnDifference == 0:
    if RowDifference >= 1:
      CheckQueenMoveIsLegal = True
      for Count in range(1, RowDifference):
        if Board[StartRow + Count][StartColumn] != "  ":
          CheckRookMoveIsLegal = False
    elif RowDifference <= -1:
      CheckQueenMoveIsLegal = True
      for Count in range(-1, RowDifference, -1):
        if Board[StartRow + Count][StartColumn] != "  ":
          CheckQueenMoveIsLegal = False
  return CheckQueenMoveIsLegal

#Knight #Done
def CheckKnightMoveIsLegal(Board, StartRow, StartColumn, FinishRow, FinishColumn):
  CheckKnightMoveIsLegal = False
  if (abs(FinishColumn - StartColumn) == 2 and abs(FinishRow - StartRow) == 1) or (abs(FinishColumn - StartColumn) == 1 and abs(FinishRow - StartRow) == 2): #X +|- 1|2, Y +|- 1|2
    CheckKnightMoveIsLegal = True
  return CheckKnightMoveIsLegal

#Implement Check process for each move
def CheckMoveIsLegal(Board, StartRow, StartColumn, FinishRow, FinishColumn, WhoseTurn):
  MoveIsLegal = True
  if (FinishColumn == StartColumn) and (FinishRow == StartRow): #Piece does not move
    MoveIsLegal = False
  else:
    PieceType = Board[StartRow][StartColumn][1]
    PieceColour = Board[StartRow][StartColumn][0]
    if WhoseTurn == "W": #Checks movement for White turn
      if PieceColour != "W":
        MoveIsLegal = False
      if Board[FinishRow][FinishColumn][0] == "W":
        MoveIsLegal = False
    else: #Check movement for Black turn
      if PieceColour != "B":
        MoveIsLegal = False
      if Board[FinishRow][FinishColumn][0] == "B":
        MoveIsLegal = False
    if MoveIsLegal == True: #If colour movement acceptable, checks piece movement
      if PieceType == "P":
        MoveIsLegal = CheckPawnMoveIsLegal(Board, StartRow, StartColumn, FinishRow, FinishColumn, PieceColour)
      elif PieceType == "K":
        MoveIsLegal = CheckKingMoveIsLegal(Board, StartRow, StartColumn, FinishRow, FinishColumn)
      elif PieceType == "Q":
        MoveIsLegal = CheckQueenMoveIsLegal(Board, StartRow, StartColumn, FinishRow, FinishColumn)
      elif PieceType == "R":
        MoveIsLegal = CheckRookMoveIsLegal(Board, StartRow, StartColumn, FinishRow, FinishColumn)
      elif PieceType == "B":
        MoveIsLegal = CheckBishopMoveIsLegal(Board, StartRow, StartColumn, FinishRow, FinishColumn)
      elif PieceType == "k":
        MoveIsLegal = CheckKnightMoveIsLegal(Board, StartRow, StartColumn, FinishRow, FinishColumn)
  return MoveIsLegal

####

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

####

if __name__ == "__main__":
  Board = CreateBoard() #0th index not used #Calls class
  StartSquare = 0 
  FinishSquare = 0
  PlayAgain = 1
  while PlayAgain == 1:
##  PlayAgain = "Y"
##  while PlayAgain == "Y": #Replay option
    WhoseTurn = "W"
    GameOver = False
    GameChoice = input("Do you want to play the sample game or a new game(enter S for Sample or N for New)? ")
    if ord(GameChoice) == 83: #Accepts upper and lowercase values
      GameChoice = chr(ord(GameChoice))
      InitialiseSample(Board, GameChoice)
    elif ord(GameChoice) == 115:
      GameChoice = chr(ord(GameChoice) - 32)
      InitialiseSample(Board, GameChoice)
    elif ord(GameChoice) == 78:
      GameChoice = chr(ord(GameChoice))
      InitialiseNew(Board, GameChoice)
    elif ord(GameChoice) == 110:
      GameChoice = chr(ord(GameChoice) - 32)
    InitialiseNew(Board, GameChoice)
    while not(GameOver): #Game is not over
      DisplayBoard(Board)
      DisplayWhoseTurnItIs(WhoseTurn)
      MoveIsLegal = False
      while not(MoveIsLegal):
        StartSquare, FinishSquare = GetMove(StartSquare, FinishSquare)
        StartRow = StartSquare % 10 #Gets char [1]
        StartColumn = StartSquare // 10 #Gets char [0]
        FinishRow = FinishSquare % 10
        FinishColumn = FinishSquare // 10
        MoveIsLegal = CheckMoveIsLegal(Board, StartRow, StartColumn, FinishRow, FinishColumn, WhoseTurn)
        if not(MoveIsLegal):
          print("That is not a legal move - please try again")
      GameOver = CheckIfGameWillBeWon(Board, FinishRow, FinishColumn)
      MakeMove(Board, StartRow, StartColumn, FinishRow, FinishColumn, WhoseTurn)
      if GameOver:
        DisplayWinner(WhoseTurn)
      if WhoseTurn == "W":
        WhoseTurn = "B"
      else:
        WhoseTurn = "W"
    PlayAgain = input("Do you want to play again (enter Y for Yes)? ")
    if ord(PlayAgain) >= 97 and ord(PlayAgain) <= 122: #Accepts upper and lowercase value
      PlayAgain = 1
##      PlayAgain = chr(ord(PlayAgain) - 32)
