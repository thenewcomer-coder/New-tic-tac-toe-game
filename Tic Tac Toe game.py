
import pygame

pygame.init()

sw = 800
sh = 600

board = pygame.image.load(r'C:\Users\Dinesh Topale\Downloads\board.jpg')
x_img = pygame.image.load(r'C:\Users\Dinesh Topale\Downloads\x.png')
o_img = pygame.image.load(r'C:\Users\Dinesh Topale\Downloads\o.png')

win = pygame.display.set_mode((sw, sh))

clock = pygame.time.Clock()

boardVals = [[0,0,0], [0,0,0], [0,0,0]]

piecesOnBoard = []

moveCount = 0

gameOver = False

isTwoPlayer = True

class Piece(object):
    def __init__(self, x, y, isX):
        self.x = x
        self.y = y
        self.isX = isX
        self.xTrue = self.x - (self.x % 200)
        self.yTrue = self.y - (self.y % 200)
        if isX:
            self.image = x_img
        else:
            self.image = o_img

    def draw(self, win):

        win.blit(self.image, (self.xTrue, self.yTrue))


def redrawGameWindow():
    win.blit(board, (0,0))
    pygame.draw.rect(win, (0,0,0), [600, 0, 200, 600])
    font = pygame.font.SysFont('arial', 50)
    smallFont = pygame.font.SysFont('arial', 25)
    if moveCount % 2 == 0:
        turn = 'X'
    else:
        turn = 'O'
    turnText = font.render(turn + "'s Turn", 1, (255, 255, 255))
    win.blit(turnText, (sw - turnText.get_width() -10, 10))

    if gameOver is True:
        gameOverText = smallFont.render("Game Over", 1, (255, 255, 255))
        win.blit(gameOverText, (sw - gameOverText.get_width() - 35, 20 + turnText.get_height()))

    for piece in piecesOnBoard:
        piece.draw(win)


    pygame.display.update()

def isGameOver(boardVals):
    zeroFound = False
    for i in boardVals:
        for j in i:
            if j == 0:
                zeroFound = True
    if not zeroFound:
        return True

    # Horizonal Win
    for i in boardVals:
        if i[0] == i[1] and i[0] == i[2] and i[0] != 0:
            return True

    # Vertical Win
    if boardVals[0][0] == boardVals[1][0] and boardVals[0][0] == boardVals[2][0]:
        if boardVals[0][0] != 0:
            return True
    if boardVals[0][1] == boardVals[1][1] and boardVals[0][1] == boardVals[2][1]:
        if boardVals[0][1] != 0:
            return True
    if boardVals[0][2] == boardVals[1][2] and boardVals[0][2] == boardVals[2][2]:
        if boardVals[0][2] != 0:
            return True

    #Diagonal Check
    if boardVals[0][0] == boardVals[1][1] and boardVals[0][0] == boardVals[2][2]:
        if boardVals[0][0] != 0:
            return True

    if boardVals[0][2] == boardVals[1][1] and boardVals[0][2] == boardVals[2][0]:
        if boardVals[0][2] != 0: # Change boardVals[0][0] to boardVals[0][2]
            return True

    # Add return false
    return False

run = True
while run:
    clock.tick(10)

    if not gameOver:
        mouseX, mouseY = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if isTwoPlayer:
            if click != (0,0,0):
                if moveCount % 2 == 0:
                    if boardVals[mouseY//200][mouseX//200] == 0:
                        piecesOnBoard.append(Piece(mouseX, mouseY, True))
                        boardVals[mouseY//200][mouseX//200] = 1
                        moveCount += 1
                else:
                    if boardVals[mouseY // 200][mouseX // 200] == 0:
                        piecesOnBoard.append(Piece(mouseX, mouseY, False))
                        boardVals[mouseY // 200][mouseX // 200] = -1
                        moveCount += 1

            gameOver = isGameOver(boardVals)
        else:
            if moveCount % 2 == 0:
                if click != (0, 0, 0):
                    if boardVals[mouseY // 200][mouseX // 200] == 0:
                        piecesOnBoard.append(Piece(mouseX, mouseY, True))
                        boardVals[mouseY // 200][mouseX // 200] = 1
                        moveCount += 1
                        print(boardVals)
            
            


    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        boardVals = [[0,0,0], [0,0,0], [0,0,0]]
        piecesOnBoard.clear()
        moveCount = 0
        gameOver = False
    if keys[pygame.K_1]:
        isTwoPlayer = False
    if keys[pygame.K_2]:
        isTwoPlayer = True


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    redrawGameWindow()


pygame.quit()