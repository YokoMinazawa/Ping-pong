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

clock=time.Clock()
FPS=60

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
    display.update()