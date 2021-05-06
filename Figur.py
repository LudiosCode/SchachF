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




class Piece:

    image = -1

    def __init__(self):
        self.row = 0
        self.column = 0
        self.color = 0


    def move(self):
        pass

    def draw(self, win):
        if self.color == 'w':
            zuZeichnen = weiss[self.image]
        else:
            zuZeichnen = schwarz[self.image]

        #pygame.draw.rect(win, (0, 0, 255), (90, 90, 90, 90), 0)

        win.blit(zuZeichnen, ((self.column)*90, (self.row)*90))



class King(Piece):
    image = 0

    def ways(self, pieces):

        squares = []

        for x in range(-1, 1):
            for y in range(-1, 1):
                pass



        for p in pieces:
            if p.color == self.color:
                if (p.column, p.row) in squares:
                    squares.remove((p.column, p.row))



        return squares

class Queen(Piece):
    image = 1

class Bishop(Piece):
    image = 2

class Knight(Piece):
    image = 3

class Rook(Piece):
    image = 4

class Pawn(Piece):
    image = 5
