from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, image_file, player_x, player_y, player_speed, width, height ):
        super().__init__()
        #self.image = transform.scale(image.load(image_file), (width,height))
        self.image = Surface((width,height))
        self.image.fill((0,128,200))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.direction = 'left'
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



class Player1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 400:
            self.rect.y += self.speed
player1 = Player1('rocket.png', 10, 10, 10, 25, 100)
        

clock=time.Clock()
FPS=60
background_color = (192,192,192)
background = Surface((700, 500))
background.fill(background_color)
window = display.set_mode((700, 500))
game = True
finish = False

font.init()
font2 = font.SysFont('Arial', 30)
win = font2.render('YOU WIN', True, (0,255,0))
lose = font2.render('YOU LOSE', True, (255,0,0))

while game == True:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish == False:
        window.blit(background,(0,0))
        player1.reset()
        player1.update()
        display.update()
        clock.tick(FPS)
print("завершение игры")

