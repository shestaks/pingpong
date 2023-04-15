from pygame import *
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
        display.update()
        clock.tick(FPS)
print("завершение игры")

