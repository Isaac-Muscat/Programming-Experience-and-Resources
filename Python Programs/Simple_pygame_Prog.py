import pygame
pygame.init()

w = 500
h = 500

win = pygame.display.set_mode((w, h))
pygame.display.set_caption("Client")

class Player():
    def __init__(self, x, y, w, h, c):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.c = c
        self.vel = 3
        self.rect = (x, y, w, h)

    def draw(self, win):
        pygame.draw.rect(win, self.c, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.x -= self.vel

        if keys[pygame.K_d]:
            self.x += self.vel

        if keys[pygame.K_w]:
            self.y -= self.vel

        if keys[pygame.K_s]:
            self.y += self.vel

        self.rect = (self.x, self.y, self.w, self.h)

def redrawWindow(win, player):
    win.fill((255, 255, 255))
    player.draw(win)
    pygame.display.update()


def main():
    run = True
    player = Player(50, 50, 100, 100, (0, 255, 0))

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        player.move()
        redrawWindow(win, player)

main()