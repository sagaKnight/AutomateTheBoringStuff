# Write your code here :-)
chessBoard = {
    "a1": "wrook",
    "b1": "wknight",
    "c1": "wbishop",
    "d1": "wqueen",
    "e1": "wking",
    "f1": "wbishop",
    "g1": "wknight",
    "h1": "wrook",
    "a2": "wpawn",
    "b2": "wpawn",
    "c2": "wpawn",
    "d2": "wpawn",
    "e2": "wpawn",
    "f2": "wpawn",
    "g2": "wpawn",
    "h2": "wpawn",
    "a8": "brook",
    "b8": "bknight",
    "c8": "bbishop",
    "d8": "bqueen",
    "e8": "bking",
    "f8": "bbishop",
    "g8": "bknight",
    "h8": "brook",
    "a7": "bpawn",
    "b7": "bpawn",
    "c7": "bpawn",
    "d7": "bpawn",
    "e7": "bpawn",
    "f7": "bpawn",
    "g7": "bpawn",
    "h7": "bpawn",
}


def isValidChessBoard(chessBoard):
    """
    //We need to be able to tell if the key is within a-h and between 1-8
    1. We would need to see if the starting character is between a and h. done.
    2. the 2nd character is 1-8. Meaning that we should splice the key name. done. And if more than 2 coordinates characters it'll stop working.
    3. Checks white or black. Done.
    4. We should check that the value is equal to or less than 2 for non-pawns. Pawns should be equal to less than 8
        - I need to make it so that w and b are seperate. If w has 2 or more rooks, bishops, etc. It should give an error
    """


whitePieces = 0
blackPieces = 0
wPawnCount = 0
bPawnCount = 0

for k, v in chessBoard.items():
    if len(k) > 2:
        print("false1")
    elif k[0] not in {"a", "b", "c", "d", "e", "f", "g", "h"}:
        print("false2")
    elif k[1] not in {"1", "2", "3", "4", "5", "6", "7", "8"}:
        print("false3")
    elif v[0] not in {"w", "b"}:
        print("false4")
    elif v[0] == "w":
        if v[1:] == "pawn":
            wPawnCount += 1
            whitePieces += 1
            if wPawnCount > 8:
                print("false5")
        else:
            whitePieces += 1
            if whitePieces > 16:
                print("false5")
    elif v[0] == "b":
        if v[1:] == "pawn":
            bPawnCount += 1
            blackPieces += 1
            if bPawnCount > 8:
                print("false6")
        else:
            blackPieces += 1
            if blackPieces > 16:
                print("false6")
    else:
        print('Looking good')

isValidChessBoard(chessBoard)
