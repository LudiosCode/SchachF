import pygame
import os
import Figur

board = pygame.image.load('Bilder/Feld2.png')

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

# pygame.transform.scale(board, (500, 500))


width = 720
height = 720
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Schach by Luis")

pieces = [None] * 64


lastPieceKlicked = 0
possibleWays = []


def draw(piece, index):
    if piece.color == 'w':
        zuZeichnen = weiss[piece.image]
    else:
        zuZeichnen = schwarz[piece.image]

    # pygame.draw.rect(win, (0, 0, 255), (90, 90, 90, 90), 0)

    win.blit(zuZeichnen, (index % 8 * 90, index // 8 * 90))

def move(piece, index):

    pieces[pieces.index(piece)] = None

    pieces[index] = piece
    piece.index = index


def windowUpdate():
    win.blit(board, (0, 0))
    # pygame.draw.rect(win, (0, 0, 255), (90, 90, 90, 90), 0)

    for x in range(len(pieces)):

        if pieces[x] is not None:
            draw(pieces[x], x)


    pygame.display.update()


def figurenErstellen(SF, CF):
    
    for x in range(16):
        f = Figur.Pawn()

        if x < 8:
            pieces[x+8] = f
        else:
            pieces[x+40] = f

    for x in (0, 7, 56, 63):
        r = Figur.Rook()
        pieces[x] = r

    for x in (1, 6, 57, 62):
        k = Figur.Knight()
        pieces[x] = k

    for x in (2, 5, 58, 61):
        r = Figur.Rook()
        pieces[x] = r

    k = Figur.King()
    k2 = Figur.King()

    q = Figur.Queen()
    q2 = Figur.Queen()

    if SF == 'w':
        pieces[59] = q
        pieces[60] = k

        pieces[3] = q2
        pieces[4] = k2


    else:
        pieces[59] = k
        pieces[60] = q

        pieces[3] = k2
        pieces[4] = q2

    for x in range(16):
        p = pieces[x]

        p.side = 'top'
        p.color = CF
        p.index = x

    for x in range(48, 63):
        p = pieces[x]

        p.side = 'bot'
        p.color = SF
        p.index = x


def klicked(x, y):
    global lastPieceKlicked
    global possibleWays

    # spalte und reihe werden anhand der mausposition errechnet

    spalte = (x // 90)
    reihe = (y // 90)

    geklicktesFeld = reihe * 8 + spalte



    if geklicktesFeld in possibleWays:

        move(pieces[lastPieceKlicked], geklicktesFeld)

        possibleWays = []
        windowUpdate()

    else:

        if pieces[geklicktesFeld] is not None:

            possibleWays = pieces[geklicktesFeld].ways(pieces)

            for w in possibleWays:
                print(w)

                pygame.draw.circle(win, (255, 0, 0), (

                    #figure this out

                    45 + w % 8 * 90, 45 + w // 8 * 90 * 90



                ), 15)


                pygame.display.update()


            lastPieceKlicked = pieces[geklicktesFeld]

        else:
            print("keine Figur")
            windowUpdate()

    pygame.display.update()


def main():
    pieceSelected = False

    figurenErstellen('b', 'w')

    windowUpdate()

    run = True
    while run:

        # windowUpdate()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()

                print(x, y)

                klicked(x, y)


main()