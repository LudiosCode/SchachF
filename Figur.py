
class Piece:
    image = -1

    def __init__(self):

        self.color = 0
        self.side = 0
        self.index = 0


class King(Piece):
    image = 0

    def ways(self, pieces):

        squares = []

        for i in (-9, -8, -7, -1, 1, 7, 8, 9):
            if 0 <= self.index + i <= 63:
                if moveIsLegal(self.index + i):
                    squares.append(self.index + i)

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




        if self.side == 'down':
            s = (self.column, self.row - 1)
            if s not in oPieceLocs:
                squares.append(s)

            if self.canMoveTwo:
                s = (self.column, self.row - 2)

                squares.append(s)

                # if s not in aPieceLocs:
                #     squares.append(s)
                # elif s in oPieceLocs:
                #     if self.movelegal(s):
                #         squares.append(s)

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


def moveIsLegal(index):
    return True


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


