import pygame

w_King = pygame.image.load('Bilder/wKing.png')
w_Queen = pygame.image.load('Bilder/wQueen.png')
w_Knight = pygame.image.load('Bilder/wKnight.png')
w_Bishop = pygame.image.load('Bilder/wBishop.png')
w_Rook = pygame.image.load('Bilder/wRook.png')
w_Pawn = pygame.image.load('Bilder/wPawn.png')

b_King = pygame.image.load('Bilder/bKing.png')
b_Queen = pygame.image.load('Bilder/bQueen.png')
b_Knight = pygame.image.load('Bilder/bKnight.png')
b_Bishop = pygame.image.load('Bilder/bBishop.png')
b_Rook = pygame.image.load('Bilder/bRook.png')
b_Pawn = pygame.image.load('Bilder/bPawn.png')

weiss = [w_King, w_Queen, w_Bishop, w_Knight, w_Rook, w_Pawn]
schwarz = [b_King, b_Queen, b_Bishop, b_Knight, b_Rook, b_Pawn]

tWeiss = []
tSchwarz = []

squares = []

# alliedPieces
aPieceLocs = []

# opposedPieces
oPieceLocs = []


class Piece:
    image = -1

    def __init__(self):
        self.row = 0
        self.column = 0
        self.color = 0
        self.side = 0

    def move(self, square):

        # En Passant nur im selben Zug fehlt noch !

        self.column = square[0]
        self.row = square[1]

    def draw(self, win):
        if self.color == 'w':
            zuZeichnen = weiss[self.image]
        else:
            zuZeichnen = schwarz[self.image]

        # pygame.draw.rect(win, (0, 0, 255), (90, 90, 90, 90), 0)

        win.blit(zuZeichnen, ((self.column) * 90, (self.row) * 90))


class King(Piece):
    image = 0

    def ways(self, pieces):

        squares = []

        aPieceLocs = []

        oPieceLocs = []

        for p in pieces:
            if p.color == self.color:
                aPieceLocs.append((p.column, p.row))

        for x in range(-1, 1):
            for y in range(-1, 1):

                s = (self.column + x, self.row + y)

                if not (0 <= s[0] <= 7) or not (0 <= s[1] <= 7):
                    continue
                else:

                    if s not in aPieceLocs:
                        squares.append(s)
                    elif s in oPieceLocs:
                        if self.movelegal(s):
                            squares.append(s)

        return squares


class Queen(Piece):
    image = 1

    def ways(self, pieces):

        squares = []

        aPieceLocs = []

        oPieceLocs = []

        for p in pieces:
            if p.color == self.color:
                aPieceLocs.append((p.column, p.row))

        for d in range(8):
            for x in range(1, 8):

                if d == 0:
                    s = (self.column - x, self.row - x)
                elif d == 1:
                    s = (self.column + x, self.row - x)
                elif d == 2:
                    s = (self.column - x, self.row + x)
                elif d == 3:
                    s = (self.column + x, self.row + x)
                elif d == 4:
                    s = (self.column - x, self.row)
                elif d == 5:
                    s = (self.column + x, self.row)
                elif d == 6:
                    s = (self.column, self.row - x)
                elif d == 7:
                    s = (self.column, self.row + x)

                if not (0 <= s[0] <= 7) or not (0 <= s[1] <= 7):
                    break
                else:
                    if s in aPieceLocs:
                        break

                    # squares.append(s)

                    if s not in aPieceLocs:
                        squares.append(s)
                    elif s in oPieceLocs:
                        if self.movelegal(s):
                            squares.append(s)

        return squares


class Bishop(Piece):
    image = 2

    def ways(self, pieces):

        squares = []

        aPieceLocs = []

        oPieceLocs = []

        for p in pieces:
            if p.color == self.color:
                aPieceLocs.append((p.column, p.row))
            else:
                oPieceLocs.append((p.column, p.row))

        for d in range(4):
            for x in range(1, 8):

                if d == 0:
                    s = (self.column - x, self.row - x)
                elif d == 1:
                    s = (self.column + x, self.row - x)
                elif d == 2:
                    s = (self.column - x, self.row + x)
                elif d == 3:
                    s = (self.column + x, self.row + x)

                if not (0 <= s[0] <= 7) or not (0 <= s[1] <= 7):
                    break
                else:

                    if s in aPieceLocs:
                        break

                    # squares.append(s)

                    elif s in oPieceLocs:
                        squares.append(s)
                        # if self.movelegal(s):
                        #     squares.append(s)
                        break
                    else:
                        squares.append(s)

        return squares


class Knight(Piece):
    image = 3

    def ways(self, pieces):

        squares = []

        aPieceLocs = []

        oPieceLocs = []

        for p in pieces:
            if p.color == self.color:
                aPieceLocs.append((p.column, p.row))

        for x in range(8):
            # oben Links
            if x == 0:
                s = (self.column - 2, self.row - 1)
            elif x == 1:
                s = (self.column - 1, self.row - 2)

            # oben Rechts
            elif x == 2:
                s = (self.column + 1, self.row - 2)
            elif x == 3:
                s = (self.column + 2, self.row - 1)

            # unten Rechts
            elif x == 4:
                s = (self.column + 2, self.row + 1)
            elif x == 5:
                s = (self.column + 1, self.row + 2)

            # unten Links
            elif x == 6:
                s = (self.column - 1, self.row + 2)
            elif x == 7:
                s = (self.column - 2, self.row + 1)

            if not (0 <= s[0] <= 7) or not (0 <= s[1] <= 7):
                continue
            else:

                if s in aPieceLocs:
                    continue

                # squares.append(s)

                if s not in aPieceLocs:
                    squares.append(s)
                elif s in oPieceLocs:
                    if self.movelegal(s):
                        squares.append(s)

        return squares


class Rook(Piece):
    image = 4

    def ways(self, pieces):

        squares = []

        aPieceLocs = []

        oPieceLocs = []

        for p in pieces:
            if p.color == self.color:
                aPieceLocs.append((p.column, p.row))

        for d in range(4):
            for x in range(1, 8):

                if d == 0:
                    s = (self.column - x, self.row)
                elif d == 1:
                    s = (self.column + x, self.row)
                elif d == 2:
                    s = (self.column, self.row - x)
                elif d == 3:
                    s = (self.column, self.row + x)

                if not (0 <= s[0] <= 7) or not (0 <= s[1] <= 7):
                    break
                else:

                    if s in aPieceLocs:
                        break

                    # squares.append(s)

                    if s not in aPieceLocs:
                        squares.append(s)
                    elif s in oPieceLocs:
                        if self.movelegal(s):
                            squares.append(s)

        return squares


class Pawn(Piece):
    # checkt noch nicht nach legalität

    image = 5

    canMoveTwo = True

    movedTwo = False

    def move(self, square):

        # En Passant nur im selben Zug fehlt noch !

        self.canMoveTwo = False

        if self.color == 'w':
            if square[1] == self.row - 2:
                self.movedTwo = True
            elif self.movedTwo:
                self.movedTwo = False
        else:
            if square[1] == self.row + 2:
                self.movedTwo = True
            elif self.movedTwo:
                self.movedTwo = False

        self.column = square[0]
        self.row = square[1]

    def ways(self, pieces):

        squares = []

        aPieceLocs = []

        oPieceLocs = []

        for p in pieces:
            if p.color == self.color:
                aPieceLocs.append((p.column, p.row))
            else:
                oPieceLocs.append((p.column, p.row))

        if self.canMoveTwo:
            s = (self.column, self.row - 2)

            squares.append(s)

            # if s not in aPieceLocs:
            #     squares.append(s)
            # elif s in oPieceLocs:
            #     if self.movelegal(s):
            #         squares.append(s)


        if self.side == 'down':
            s = (self.column, self.row - 1)
            if s not in oPieceLocs:
                squares.append(s)

            if (self.column - 1, self.row - 1) in oPieceLocs:
                squares.append((self.column - 1, self.row - 1))

            if (self.column + 1, self.row - 1) in oPieceLocs:
                squares.append((self.column + 1, self.row - 1))



            if (self.column + 1, self.row) in oPieceLocs:
                for p in pieces:
                    if p.column == self.column + 1 and p.row == self.row:
                        if p.movedTwo:
                            squares.append((self.column + 1, self.row - 1))

            if (self.column - 1, self.row) in oPieceLocs:
                for p in pieces:
                    if p.column == self.column - 1 and p.row == self.row:
                        if p.movedTwo:
                            squares.append((self.column - 1, self.row - 1))


        else:
            s = (self.column, self.row + 1)
            if s not in oPieceLocs:
                if legalmove(self, pieces, (self.column, self.row), s):
                    squares.append(s)

            if self.canMoveTwo:
                s = (self.column, self.row + 2)

                squares.append(s)

                # if s not in aPieceLocs:
                #     squares.append(s)
                # elif s in oPieceLocs:
                #     if self.movelegal(s):
                #         squares.append(s)



            if (self.column - 1, self.row + 1) in oPieceLocs:
                squares.append((self.column - 1, self.row + 1))

            if (self.column + 1, self.row + 1) in oPieceLocs:
                squares.append((self.column + 1, self.row + 1))




            if (self.column + 1, self.row) in oPieceLocs:
                for p in pieces:
                    if p.column == self.column + 1 and p.row == self.row:
                        if p.movedTwo:
                            squares.append((self.column + 1, self.row + 1))

            if (self.column - 1, self.row) in oPieceLocs:
                for p in pieces:
                    if p.column == self.column - 1 and p.row == self.row:
                        if p.movedTwo:
                            squares.append((self.column - 1, self.row + 1))

        return squares


def legalmove(piece, pieces, start, ziel):

    checkPieces = pieces
    farbe = 0
    kingSquare = 0
    Tiefe = 0

    for p in checkPieces:
        if p.column == start[0] and p.row == start[1]:
            farbe = p.color
            p.move(ziel)

        if p.color == piece.color:
            if type(p) == King:
                kingSquare = (p.column, p.row)

    for p in checkPieces:
        if p.color != farbe:
            if kingSquare in p.ways(pieces):
                return False

    return True


