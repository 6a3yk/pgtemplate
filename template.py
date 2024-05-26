from pygame import *
from random import randint
import time as t

init()
mixer.init()
font.init()

class GameSprite(sprite.Sprite):  #обищй класс спрайт
    def __init__(self, player_image, player_x, player_y, player_speed,w,h):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (w, h))    
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

        

window = display.set_mode((0, 0), FULLSCREEN)
win_width,win_height = display.get_surface().get_size() 

FPS = 30
game = True
finish = False

score = 0


clock = time.Clock()
font0 = font.Font(None,100)
font1 = font.Font(None,30)
win_image = font0.render( 'YOU WIN!', True, (0,255,255) )
lose_image = font0.render( 'YOU LOSE!', True, (255,0,0) )

display.set_caption("Shooter")

background = transform.scale(image.load("файл-фон"), (win_width, win_height))

sprite = GameSprite('картинка',икс,игрек,скорость,ширина,высота)



while game:
    #обновление экрана
    display.update()     

    #задержка
    clock.tick(FPS)      

    #обработка событий
    for event0 in event.get():
        if event0.type == QUIT:
            game = False
        elif event0.type == MOUSEBUTTONDOWN and event0.button == 1:
            0
    if not(finish): 

        #игровая логика
        image_score = font1.render('Счёт: '+str(score), True, (255,255,255) )
        

        #отрисовка
        window.blit(background,(0, 0))          
        window.blit(image_score,(250,150))
        sprite.reset()






