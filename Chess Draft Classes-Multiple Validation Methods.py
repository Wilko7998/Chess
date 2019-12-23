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
##          MoveIsLegal = ChessPiece.Pawn.CheckPawnMoveIsLegal(Board, StartRow, StartColumn, FinishRow, FinishColumn, PieceColour)
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
##          MoveIsLegal = ChessPiece.Knight.CheckKnightMoveIsLegal(Board, StartRow, StartColumn, FinishRow, FinishColumn)
          KnightMoves = ChessPiece.Knight.GetMoves(Board, StartColumn, StartRow)
          print (KnightMoves)
          if Board[FinishColumn][FinishRow] in KnightMoves:
            MoveIsLegal = True
        elif Type == "B":
##          MoveIsLegal = ChessPiece.Bishop.CheckBishopMoveIsLegal(Board, StartRow, StartColumn, FinishRow, FinishColumn)
          BishopMoves = ChessPiece.Bishop.GetMoves(Board, StartColumn, StartRow)
          print (BishopMoves)
          if Board[FinishColumn][FinishRow] in BishopMoves:
            MoveIsLegal = True
        elif Type == "Q":
##          MoveIsLegal = ChessPiece.Queen.CheckQueenMoveIsLegal(Board, StartRow, StartColumn, FinishRow, FinishColumn)
          QueenMoves = ChessPiece.Queen.GetMoves(Board, StartColumn, StartRow)
          print (QueenMoves)
          if Board[FinishColumn][FinishRow] in QueenMoves:
            MoveIsLegal = True
        elif Type == "K":
##          MoveIsLegal = ChessPiece.King.CheckKingMoveIsLegal(Board, StartRow, StartColumn, FinishRow, FinishColumn)
          KingMoves = ChessPiece.King.GetMoves(Board, StartColumn, StartRow)
          print (KingMoves)
          if Board[FinishColumn][FinishRow] in KingMoves:
            MoveIsLegal = True
      else:
        MoveIsLegal = False
    return MoveIsLegal

##

  class Pawn:
##    def CheckPawnMoveIsLegal(Board, StartRow, StartColumn, FinishRow, FinishColumn, ColourOfPiece):
##      CheckPawnMoveIsLegal = False
##      PotentialMoves = []
##      if ColourOfPiece == "W":
##        if Board[StartColumn][StartRow][1] == "P":
##          PotentialMoves.append((StartColumn+1, StartRow))
##          if StartRow == 2:  # if first move
##            PotentialMoves.append((StartColumn+2, StartRow))
##          if StartColumn < BOARDDIMENSION and StartRow < BOARDDIMENSION and Board[StartColumn+1][StartRow+1][0] == "B":
##            PotentialMoves.append((StartColumn+1, StartRow+1))
##          if StartColumn < BOARDDIMENSION and 0 < StartRow and Board[StartColumn+1][StartRow-1][0] == "B":
##            PotentialMoves.append((StartColumn+1, StartRow-1))
##      elif ColourOfPiece == "B":
##        if Board[StartColumn][StartRow][1] == "P":
##          PotentialMoves.append((StartColumn+1, StartRow))
##          if StartColumn == 7:  # if first move
##            PotentialMoves.append((StartColumn-2, StartRow))
##          if StartColumn < BOARDDIMENSION and StartRow < BOARDDIMENSION and Board[StartColumn-1][StartRow+1][0] == "B":
##            PotentialMoves.append((StartColumn-1, StartRow+1))
##          if StartColumn < BOARDDIMENSION and 0 < StartRow and Board[StartColumn-1][StartRow-1][0] == "B":
##            PotentialMoves.append((StartColumn-1, StartRow-1))
####      Moves = append_strip_negatives(PotentialMoves)
##      if Board[FinishColumn][FinishRow] in PotentialMoves:
##        CheckPawnMoveIsLegal = True
##      return CheckPawnMoveIsLegal
    
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
##      Moves = append_strip_negatives(PotentialMoves)
      print (PotentialMoves)
      return PotentialMoves

##

# This code does not allow Black Pawn to move 1 space forward for first, only 2
##      CheckPawnMoveIsLegal = False
##      if ColourOfPiece == "W": #White piece 
##        if StartRow == 2:
##          if FinishRow == StartRow + 2 or FinishRow == StartRow + 1: #Checks for 1 or 2-space first move
##            if FinishRow == StartRow + 2:
##              if Board[StartRow + 1][StartColumn] == "  " and Board[FinishRow][FinishColumn] == "  " and FinishColumn == StartColumn:#Checks no piece in path
##                CheckPawnMoveIsLegal = True
####            elif FinishColumn == StartColumn and Board[FinishRow][FinishColumn] == "  ":
####              CheckPawnMoveIsLegal = True
##        if FinishRow == StartRow + 1:
##          if FinishColumn == StartColumn and Board[FinishRow][FinishColumn] == "  ":
##            CheckPawnMoveIsLegal = True
##          elif abs(FinishColumn - StartColumn) == 1 and Board[FinishRow][FinishColumn][0] == "B":
##            CheckPawnMoveIsLegal = True
##      elif StartRow == 7: #Black piece
##        if FinishRow == StartRow - 2 or FinishRow == StartRow - 1:
##          if FinishRow == StartRow - 2:
##              if Board[StartRow - 1][StartColumn] == "  " and Board[FinishRow][FinishColumn] == "  " and FinishColumn == StartColumn: #Checks no piece in path
##                CheckPawnMoveIsLegal = True
####          elif FinishColumn == StartColumn and Board[FinishRow][FinishColumn] == "  ":
####            CheckPawnMoveIsLegal = True
##      elif FinishRow == StartRow - 1:
##        if FinishColumn == StartColumn and Board[FinishRow][FinishColumn] == "  ":
##          CheckPawnMoveIsLegal = True
##        elif abs(FinishColumn - StartColumn) == 1 and Board[FinishRow][FinishColumn][0] == "W":
##          CheckPawnMoveIsLegal = True
##      return CheckPawnMoveIsLegal

##

  class Rook:
##    def CheckRookMoveIsLegal(Board, StartRow, StartColumn, FinishRow, FinishColumn):
##      CheckRookMoveIsLegal = False
##      RowDifference = FinishRow - StartRow
##      ColumnDifference = FinishColumn - StartColumn
##      if RowDifference == 0: #Vertical movement
##        if ColumnDifference >= 1: #+ve vertical movement
##          CheckRookMoveIsLegal = True
##          for Count in range(1, ColumnDifference):
##            if Board[StartRow][StartColumn + Count] != "  ": #Checks has not moved through piece(s)
##              CheckRookMoveIsLegal = False
##        elif ColumnDifference <= -1: #-ve vertical movement
##          CheckRookMoveIsLegal = True
##          for Count in range(-1, ColumnDifference, -1): 
##            if Board[StartRow][StartColumn + Count] != "  ": #Checks has not moved through piece(s)
##              CheckRookMoveIsLegal = False
##      elif ColumnDifference == 0: #Horizontal movement
##        if RowDifference >= 1: #+ve horizontal movement
##          CheckRookMoveIsLegal = True
##          for Count in range(1, RowDifference): 
##            if Board[StartRow + Count][StartColumn] != "  ": #Checks has not moved through piece(s)
##              CheckRookMoveIsLegal = False
##        elif RowDifference <= -1: #-ve horizontal movement
##          CheckRookMoveIsLegal = True
##          for Count in range(-1, RowDifference, -1): 
##            if Board[StartRow + Count][StartColumn] != "  ": #Checks has not moved through piece(s)
##              CheckRookMoveIsLegal = False
##      return CheckRookMoveIsLegal

    def GetMoves(Board, StartColumn, StartRow):
      PotentialMoves = []
      print (PotentialMoves)
      if Board[StartColumn][StartRow][1] == "R":
##        if 0<StartColumn<BOARDDIMENSION and 0<StartRow<BOARDDIMENSION:
##          for i in range (1, BOARDDIMENSION):
##            PotentialMoves.append((StartColumn+i, StartRow), (StartColumn-i, StartRow), (StartColumn, StartRow-i), (StartColumn, StartRow+i))    
        U = [(StartColumn+i, StartRow) for i in range(1, BOARDDIMENSION) if 0<=StartColumn<BOARDDIMENSION and 0<=StartRow<BOARDDIMENSION]
        D = [(StartColumn-i, StartRow) for i in range(1, BOARDDIMENSION) if 0<=StartColumn<BOARDDIMENSION and 0<=StartRow<BOARDDIMENSION]
        L = [(StartColumn, StartRow-i) for i in range(1, BOARDDIMENSION) if 0<=StartColumn<BOARDDIMENSION and 0<=StartRow<BOARDDIMENSION]
        R = [(StartColumn, StartRow+i) for i in range(1, BOARDDIMENSION) if 0<=StartColumn<BOARDDIMENSION and 0<=StartRow<BOARDDIMENSION]
##        PotentialMoves = ''.join(U)
##        PotentialMoves.append(D)
##        PotentialMoves.append(L)
##        PotentialMoves.append(R)
      return PotentialMoves

##

  class Knight:
##    def CheckKnightMoveIsLegal(Board, StartRow, StartColumn, FinishRow, FinishColumn):
##      CheckKnightMoveIsLegal = False
##      if abs(FinishColumn - StartColumn) == 2 and abs(FinishRow - StartRow) == 1\
##      or abs(FinishColumn - StartColumn) == 1 and abs(FinishRow - StartRow) == 2:
##        CheckKnightMoveIsLegal = True #X +- 2, Y +- 1 or X +- 1, Y +- 2
##      return CheckKnightMoveIsLegal
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
      return PotentialMoves

##

  class Bishop: ##Can move through pieces atm
##    def CheckBishopMoveIsLegal(Board, StartRow, StartColumn, FinishRow, FinishColumn):
##      CheckBishopMoveIsLegal = False
##      if abs(FinishColumn - StartColumn) >= 1 and abs(FinishRow - StartRow) >= 1: #Diagonal movement unlimited
##        CheckBishopMoveIsLegal = True
##        for x in range (FinishRow - StartRow):
##          for y in range (FinishColumn - StartColumn):
##            if Board[StartColumn + x][StartRow + y] == "  " or Board[StartColumn + x][StartRow - y] == "  "\
##               or Board[StartColumn - x][StartRow + y] == "  " or Board[StartColumn - x][StartRow - y] == "  ":
##              CheckBishopMoveIsLegal = True
##            else:
##              CheckBishopMoveIsLegal = False
##      return CheckBishopMoveIsLegal

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
##    def CheckQueenMoveIsLegal(Board, StartRow, StartColumn, FinishRow, FinishColumn):
##      CheckQueenMoveIsLegal = False
##      if abs(FinishColumn - StartColumn) >= 1 and abs(FinishRow - StartRow) >= 1: #Bishop check move sequence
##        CheckQueenMoveIsLegal = True
##      RowDifference = FinishRow - StartRow #Rook check move sequence
##      ColumnDifference = FinishColumn - StartColumn
##      if RowDifference == 0:
##        if ColumnDifference >= 1:
##          CheckQueenMoveIsLegal = True
##          for Count in range(1, ColumnDifference):
##            if Board[StartRow][StartColumn + Count] != "  ":
##              CheckQueenMoveIsLegal = False
##        elif ColumnDifference <= -1:
##          CheckQueenMoveIsLegal = True
##          for Count in range(-1, ColumnDifference, -1):
##            if Board[StartRow][StartColumn + Count] != "  ":
##              CheckQueenMoveIsLegal = False
##      elif ColumnDifference == 0:
##        if RowDifference >= 1:
##          CheckQueenMoveIsLegal = True
##          for Count in range(1, RowDifference):
##            if Board[StartRow + Count][StartColumn] != "  ":
##              CheckQueenMoveIsLegal = False
##        elif RowDifference <= -1:
##          CheckQueenMoveIsLegal = True
##          for Count in range(-1, RowDifference, -1):
##            if Board[StartRow + Count][StartColumn] != "  ":
##              CheckQueenMoveIsLegal = False
##      return CheckQueenMoveIsLegal

    def GetMoves(Board, StartColumn, StartRow):
      PotentialMoves = []
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
##    def CheckKingMoveIsLegal(Board, StartRow, StartColumn, FinishRow, FinishColumn):
##      CheckKingMoveIsLegal = False
##      if abs(FinishColumn - StartColumn) <= 1 and abs(FinishRow - StartRow) <= 1: #Move is within 1-space from start
##        CheckKingMoveIsLegal = True
##      return CheckKingMoveIsLegal

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
      if StartXY[0] == Columns[i - 1]: #Turns Column string values into integer values
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
    if WhoseTurn == "W" and FinishRow == 8 and Board[StartColumn][StartRow][1] == "P":
      PawnChange = input("What piece would you like to change your Pawn to? (Rook, Knight, Bishop or Queen)") #Allows Pawn piece change when reaches end of board
      if PawnChange == "Rook" or PawnChange == "Bishop" or PawnChange == "Queen":
        Board[FinishColumn][FinishRow] = "W"+str(PawnChange[0]) #For these 3, adds first letter of piece type
      else:
        Board[FinishColumn][FinishRow] = "Wk" #Provides Knight as an else
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
