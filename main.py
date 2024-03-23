from pygame import * 
from random import randint
from time import time as timer

window = display.set_mode((700, 600))
display.set_caption('Джангл')
#backround = transform.scale(image.load('background.jpg'), (700, 900))
mixer.init()
mixer.music.load('3d-z_uki-na-_oyne.mp3')
mixer.music.play()
#damage = mixer.Sound('dead.mp3')
#ssssssswon = mixer.Sound('win.mp3')

#шрифт

font.init()
font = font.Font(None, 70)
win = font.render('Москва твоя', True, (0, 255, 0))
lose = font.render('Москва не твоя', True, (255, 0 ,0))

#font2 = font.Font(None, 30)

clock = time.Clock()
FPS = 60
game = True

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, pl_x, pl_y, pl_speed, p_s_x, p_s_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (p_s_x, p_s_y))
        self.speed = pl_speed
        self.rect = self.image.get_rect()
        self.rect.x = pl_x
        self.rect.y = pl_y
        
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    
    
    def update(self):
        global last_time
        global num_fire
        global rel_time
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.y < 535:
            self.rect.y += self.speed
        if key_pressed[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if key_pressed[K_d] and self.rect.x < 635:
            self.rect.x += self.speed

        if key_pressed[K_SPACE]:

        
            if num_fire < 5 and rel_time == False:


                num_fire += 1
                self.fire()
            if num_fire >= 5 and rel_time == False:

                last_time = timer()
                rel_time = True
    def fire(self):
        bullet = Bullet('gitler.png', self.rect.x, self.rect.y, 10, 30, 30 )
        bullets.add(bullet)

class Enemy(GameSprite):
    direct = 'left'
    def update(self):
        if self.rect.x <= 450:
            self.direct = 'right'
        if self.rect.x >= 650:
            self.direct = 'left'
        
        if self.direct == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
lost = 0
class NewEnemy1(GameSprite):
    direct = 'left'
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > 600:
            self.rect.y = 0
            self.rect.x = randint(50, 600-50)
            lost = lost + 1
 
            
class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <= 0:
            self.kill()



class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_hight):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.hight = wall_hight
        self.image = Surface((self.width, self.hight))
        self.image.fill((color_1,color_2,color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y)) 

w1 = Wall(154, 205, 50, 100, 20, 450, 10)
w2 = Wall(154, 205, 50, 100, 480, 350, 10)
w3 = Wall(154, 205, 50, 100, 20, 10, 380)
w4 = Wall(154, 205, 50, 100, 480, 10, 600)
w5 = Wall(154, 205, 50, 450, 200, 10, 600)


backround = GameSprite('background.jpg', 0, 0, 0, 700, 600)
hero = Player('gitler.png', 20, 500, 5, 65, 65)
enemy1 = Enemy('klipartz.com (1).png', 500, 350, 5, 50, 100)
past = GameSprite('kreml.png', 600, 500, 0, 100, 100)
newenemy = NewEnemy1('klipartz.com (1).png', 350, 200, 5, 50, 100)
newenemy2 = NewEnemy1('klipartz.com (1).png', 400, 100, 5, 50, 100)
newenemy3 = NewEnemy1('klipartz.com (1).png', 200, 300, 5, 50, 100)

#newenemys = sprite.Group()
#for i in range(1, 3):
    #newenemy = NewEnemy('klipartz.com (1).png', 400, 350, 5, 50, 100)
    #newenemys.add(newenemy)

# nein = mixer.Sound('hitler-nein23443.mp3')

last_time = 0
num_fire = 0
rel_time = False


bullets = sprite.Group()
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    
    backround.reset()
    hero.reset()
    enemy1.reset()
    past.reset()
    newenemy.reset()
    newenemy2.reset()
    newenemy3.reset()
    w1.draw_wall()
    w2.draw_wall()
    w3.draw_wall()
    w4.draw_wall()
    w5.draw_wall()
    bullets.draw(window)



    hero.update()
    enemy1.update()
    newenemy.update()
    newenemy2.update()
    newenemy3.update()
    bullets.update()
    w1.update()
    w2.update()
    w3.update()
    w4.update()
    w5.update()
    # key_pressed = key.get_pressed()
    # if key_pressed[K_r]: 
    #     nein.play()

    if rel_time == True:
            now_time = timer()
            if now_time - last_time < 3:
                #reload_bullets = font2.render('Релоад', 1, (255, 0, 0))
                #window.blit(reload_bullets, (260, 460))
                pass
            else:
                num_fire = 0                
                rel_time = False

    #проверка победы

    if sprite.collide_rect(hero, past):
        window.blit(win, (200,200))

    #if sprite.collide_rect(bullets, newenemy) or sprite.collide_rect(bullets, newenemy2) or sprite.collide_rect(bullets, newenemy3):
        #newenemy.rect.x = 600
        #newenemy2.rect.x = 600
        #     newenemy3.rect.x = 600

        
    
    # проверка поражения

    if sprite.collide_rect(hero, enemy1)or sprite.collide_rect(hero, newenemy)or sprite.collide_rect(hero, newenemy2) or sprite.collide_rect(hero, newenemy3)  or sprite.collide_rect(hero, w1) or sprite.collide_rect(hero, w2) or sprite.collide_rect(hero, w3) or sprite.collide_rect(hero, w4) or sprite.collide_rect(hero, w5):
        window.blit(lose, (200,200))
        hero.rect.x = 0
        hero.rect.y = 450

    
    display.update()
    clock.tick(FPS)