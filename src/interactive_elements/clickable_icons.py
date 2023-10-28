```python
import pygame
from pygame.locals import *

class ClickableIcon(pygame.sprite.Sprite):
    def __init__(self, image_path, position, demo_function):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.demo_function = demo_function

    def is_clicked(self, event):
        if event.type == MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.demo_function()

def demo1():
    print("Demo 1 is running...")

def demo2():
    print("Demo 2 is running...")

def demo3():
    print("Demo 3 is running...")

def demo4():
    print("Demo 4 is running...")

def demo5():
    print("Demo 5 is running...")

pygame.init()
screen = pygame.display.set_mode((800, 600))

icon1 = ClickableIcon('icon1.png', (50, 50), demo1)
icon2 = ClickableIcon('icon2.png', (150, 50), demo2)
icon3 = ClickableIcon('icon3.png', (250, 50), demo3)
icon4 = ClickableIcon('icon4.png', (350, 50), demo4)
icon5 = ClickableIcon('icon5.png', (450, 50), demo5)

all_sprites = pygame.sprite.Group(icon1, icon2, icon3, icon4, icon5)

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        else:
            for sprite in all_sprites:
                sprite.is_clicked(event)

    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
```