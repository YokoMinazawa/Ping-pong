from pygame import*

class GameSprite(sprite.Sprite):
    def __init__(self,player_image, player_x,player_y,player_speed):
        super().__init__()
        self.image=transform.scale(image.load(player_image),(17,130))
        self.speed=player_speed
        self.rect=self.image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class BallSprite(sprite.Sprite):
    def __init__(self,player_image, player_x,player_y,player_speed):
        super().__init__()
        self.image=transform.scale(image.load(player_image),(60,60))
        self.speed=player_speed
        self.rect=self.image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        key_pressed=key.get_pressed()
        if key_pressed[K_UP] and self.rect.y>0:
            self.rect.y-= self.speed
        if key_pressed[K_DOWN] and self.rect.y<375:
            self.rect.y+= self.speed
    def move(self):
        key_pressed=key.get_pressed()
        if key_pressed[K_w] and self.rect.y>0:
            self.rect.y-= self.speed
        if key_pressed[K_s] and self.rect.y<375:
            self.rect.y+= self.speed

window=display.set_mode((700,500))
display.set_caption("Ping-pong!")
back=(150,150,250)

plat_1=Player('box.jpg',5,200,3)
plat_2=Player('box.jpg',677,200,3)
ball=BallSprite('ball.png',350,250,3)

font.init()
font1=font.SysFont('Arial',60)
lose_1=font1.render('Player 1 lose!',1,(255,251,251))
lose_2=font1.render('Player 2 lose!',1,(255,251,251))

clock=time.Clock()
FPS=60

speed_x=3
speed_y=3

game=True
finish=False
while game:
    for e in event.get():
        if e.type==QUIT:
            game=False
    if finish != True:
        window.fill(back)
        clock.tick(FPS)
        plat_1.reset()
        plat_2.reset()
        plat_1.move()
        plat_2.update()
        ball.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
    if ball.rect.y > 430 or ball.rect.y < 0:
        speed_y *= -1
    if sprite.collide_rect(plat_1,ball) or sprite.collide_rect(plat_2,ball):
        speed_x *= -1
    if ball.rect.x < 0:
        finish=True
        window.blit(lose_1,(200,200))
    if ball.rect.x > 670:
        finish=True
        window.blit(lose_2,(200,200))
    display.update()