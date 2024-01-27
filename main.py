from pygame import *
from random import *
window = display.set_mode((700, 500))
display.set_caption("ping-pong")

clock = time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
   def update(self):
       keys = key.get_pressed()
       if keys[K_a]:
           self.rect.x -= self.speed
       if keys[K_d]:
           self.rect.x += self.speed



game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False


    display.update() 
    clock.tick(FPS)