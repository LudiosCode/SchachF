import pygame
import os
import Figur

board = pygame.image.load('Bilder/Feld2.png')

# pygame.transform.scale(board, (500, 500))


width = 720
height = 720
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Schach by Luis")

pieces = []

lastPieceKlicked = 0
possibleWays = []


def windowUpdate():
    win.blit(board, (0, 0))
    # pygame.draw.rect(win, (0, 0, 255), (90, 90, 90, 90), 0)

    for p in pieces:
        p.draw(win)

    pygame.display.update()


def figurenErstellen(SF, CF):
    
    for x in range(8):
        f = Figur.Pawn()
        f.color = SF
        f.row = 6
        f.column = x
        f.side = 'down'
        pieces.append(f)

        f = Figur.Pawn()
        f.color = CF
        f.row = 1
        f.column = x
        f.side = 'top'
        pieces.append(f)



    SQ = 0
    SK = 0
    CQ = 0
    CK = 0

    if SF == 'w':

        SQ = (7, 3)
        SK = (7, 4)

        CQ = (0, 3)
        CK = (0, 4)
    else:

        SQ = (7, 4)
        SK = (7, 3)

        CQ = (0, 4)
        CK = (0, 3)

    r = Figur.Queen()
    r.color = SF
    r.row = SQ[0]
    r.column = SQ[1]
    r.side = 'down'
    pieces.append(r)

    r = Figur.King()
    r.color = SF
    r.row = SK[0]
    r.column = SK[1]
    r.side = 'down'
    pieces.append(r)

    r = Figur.Queen()
    r.color = CF
    r.row = CQ[0]
    r.column = CQ[1]
    r.side = 'top'
    pieces.append(r)

    r = Figur.King()
    r.color = CF
    r.row = CK[0]
    r.column = CK[1]
    r.side = 'top'
    pieces.append(r)

    r = Figur.Rook()
    r.color = SF
    r.row = 7
    r.column = 0
    r.side = 'down'
    pieces.append(r)

    r = Figur.Rook()
    r.color = SF
    r.row = 7
    r.column = 7
    r.side = 'down'
    pieces.append(r)

    r = Figur.Knight()
    r.color = SF
    r.row = 7
    r.column = 1
    r.side = 'down'
    pieces.append(r)

    r = Figur.Knight()
    r.color = SF
    r.row = 7
    r.column = 6
    r.side = 'down'
    pieces.append(r)

    r = Figur.Bishop()
    r.color = SF
    r.row = 7
    r.column = 2
    r.side = 'down'
    pieces.append(r)

    r = Figur.Bishop()
    r.color = SF
    r.row = 7
    r.column = 5
    r.side = 'down'
    pieces.append(r)

    r = Figur.Rook()
    r.color = CF
    r.row = 0
    r.column = 0
    r.side = 'top'
    pieces.append(r)

    r = Figur.Rook()
    r.color = CF
    r.row = 0
    r.column = 7
    r.side = 'top'
    pieces.append(r)

    r = Figur.Knight()
    r.color = CF
    r.row = 0
    r.column = 1
    r.side = 'top'
    pieces.append(r)

    r = Figur.Knight()
    r.color = CF
    r.row = 0
    r.column = 6
    r.side = 'top'
    pieces.append(r)

    r = Figur.Bishop()
    r.color = CF
    r.row = 0
    r.column = 2
    r.side = 'top'
    pieces.append(r)

    r = Figur.Bishop()
    r.color = CF
    r.row = 0
    r.column = 5
    r.side = 'top'
    pieces.append(r)

    # r = Figur.King()
    # r.color = 'w'
    # r.row = 2
    # r.column = 5
    # pieces.append(r)


def pieceLocations():
    locs = []

    for p in pieces:
        locs.append((p.row, p.column))

    return locs


def klicked(x, y):
    global lastPieceKlicked
    global possibleWays

    # spalte und reihe werden anhand der mausposition errechnet

    spalte = (x // 90)
    reihe = (y // 90)

    print(spalte, reihe)

    pw = 0

    if (spalte, reihe) in possibleWays:

        #eliminieren der geschlagenen Figur
        for p in pieces:
            if spalte == p.column and reihe == p.row:
                p.move((-1, -1))
        lastPieceKlicked.move((spalte, reihe))
        possibleWays = []
        windowUpdate()
    else:

        hit = False

        for p in pieces:
            if p.row == reihe and p.column == spalte:

                # print(type(p))

                windowUpdate()

                # print(p.ways())
                # pw = p.ways()

                #pygame.display.update()

                possibleWays = p.ways(pieces)

                for w in possibleWays:
                    print(w)

                    pygame.draw.circle(win, (255, 0, 0), (45 + w[0] * 90, 45 + w[1] * 90), 15)

                lastPieceKlicked = p

                hit = True

        if not hit:
            print("keine Figur")
            windowUpdate()

    pygame.display.update()


def main():
    pieceSelected = False

    figurenErstellen('w', 'b')

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