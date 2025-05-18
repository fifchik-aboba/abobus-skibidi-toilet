from pygame import *



class GameSprite(sprite.Sprite):
    #конструктор класса
       #конструктор класса
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height): # добавить еще два параметра при создании и задавать размер прямоугольгника для картинки самим
        super().__init__()
 
        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (wight, height)) # вместе 55,55 - параметры
        self.speed = player_speed
 
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))







class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed



back = (255, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)




font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))


ball = GameSprite("boom.png", 400, 250, 5, 40, 40)
reverse1 = Player("reverse.png", 50, 250, 5, 60, 60)
reverse2 = Player("reverse.png", 500, 250, 5, 60, 60)



game = True
finish = False
clock = time.Clock()
FPS = 60


speed_x = -3
speed_y = 3


while game:
    for e in event.get():
        if e.type == QUIT:
            game =  False

    if finish != True:
        window.fill(back)
        ball.reset()
        reverse1.reset()
        reverse2.reset()
        reverse1.update_l()
        reverse2.update_r()
        display.update()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(reverse1, ball) or sprite.collide_rect(reverse2, ball):
            speed_x *= -1


        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200,200))
           

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200,200))
            

    display.update()
    clock.tick(FPS)
