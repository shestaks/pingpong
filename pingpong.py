from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, image_file, player_x, player_y, player_speed, width, height ):
        super().__init__()
        #self.image = transform.scale(image.load(image_file), (width,height))
        self.image = Surface((width,height))
        self.image.fill((0,0,0))
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
player1 = Player1('rocket.png', 10, 190, 10, 25, 100)
        
class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed
player2 = Player2('rocket.png', 660, 190, 10, 25, 100)

class Ball(GameSprite):
    def __init__(self, image_file, player_x, player_y, player_speed, width, height):
        super().__init__(image_file, player_x, player_y, player_speed, width, height)
        self.speed_x = player_speed
        self.speed_y = player_speed
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if (self.rect.y < 0) or (self.rect.y > 490):
            self.speed_y *= -1
ball= Ball('rocket.png', 100, 400, 2, 25, 25)

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

player1_lose = font2.render('player1 lose!', True, (255, 0, 0))
player2_lose = font2.render('player2 lose!', True, (255, 0, 0))

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
        player2.reset()
        player2.update()
        ball.reset()
        ball.update()
        

        if sprite.collide_rect(ball, player1):
            ball.speed_x *= -1

        if sprite.collide_rect(ball, player2):
            ball.speed_x *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(player1_lose, (400, 200))

        if ball.rect.x > 700:
            finish = True
            window.blit(player2_lose, (400, 200))



        display.update()
        clock.tick(FPS)
print("завершение игры")

