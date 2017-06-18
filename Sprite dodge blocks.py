import pygame
import random
 

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
number = 25
 
class Player(pygame.sprite.Sprite):
     
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        
        
class Bad_block(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.change_x = random.randrange(-3,4)
        self.change_y = random.randrange(1,4)
        self.left_boundary = 0
        self.right_boundary = 700
        self.top_boundary = 0
        self.bottom_boundary = 520

    def move(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y    

        if self.rect.right >= self.right_boundary:
            self.change_x = random.randrange(-1,0)
        if self.rect.left <= self.left_boundary:
            self.change_x = random.randrange(1,2)
        if self.rect.bottom >= self.bottom_boundary:
            self.rect.y = (-10)
        if self.rect.top <= self.top_boundary:
            self.rect.x = random.randrange(screen_width-20)



class Bullet(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def move(self):
        self.rect.y -= 5
        
        
        

   

pygame.init()

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255) 
 
screen_width = 700
screen_height = 500
screen = pygame.display.set_mode([screen_width, screen_height])
 
pygame.display.set_caption("Dodge blocks")

bb_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()
 


for i in range(8):
    block = Bad_block(BLACK, 20, 20)
    block.rect.x = random.randrange(screen_width-20)
    block.rect.y = random.randrange(-500,0)
    bb_list.add(block)
    all_sprites_list.add(block)

 

 
player = Player(GREEN ,20, 20)
player.rect.x = 350
player.rect.y = 250
all_sprites_list.add(player)

bullet = Bullet(RED ,5, 5)
bullet.rect.x = player.rect.x + 7.5
bullet.rect.y = player.rect.y - 5
bullet_list.add(bullet)
all_sprites_list.add(bullet)

        

done = False
change_x = 0
change_y = 0
good_sound = pygame.mixer.Sound("laser1.wav")
bad_sound = pygame.mixer.Sound("laser2.wav")
clock = pygame.time.Clock()
score = 0
end = False

while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                change_x = (-5)
                
            if event.key == pygame.K_RIGHT:
                change_x = (5)
                
            if event.key == pygame.K_UP:
                bullet = Bullet(RED ,5, 5)
                bullet.rect.x = player.rect.x + 7.5
                bullet.rect.y = player.rect.y - 5
                bullet_list.add(bullet)
                all_sprites_list.add(bullet)
                good_sound.play()
                
            if event.key == pygame.K_DOWN:
                change_y = (5)

            
                
        if event.type == pygame.KEYUP:
            
            if event.key == pygame.K_LEFT:
                change_x = 0
                
            if event.key == pygame.K_RIGHT:
                change_x = 0

            if event.key == pygame.K_UP:
                change_y = 0

            if event.key == pygame.K_DOWN:
                change_y = 0




    player.rect.x += change_x
    player.rect.y += change_y

    if player.rect.x >= 660:
            player.rect.x = 660

    if player.rect.x <= 20:
            player.rect.x = 20

    if player.rect.y >= 480:
            player.rect.y = 480

    if player.rect.y <= 480:
            player.rect.y = 480

    

    
    for i in bb_list:
        i.move()

    for i in bullet_list:
        i.move()

       
    screen.fill(WHITE)

    
    
    bb_hit_list = pygame.sprite.spritecollide(player, bb_list, True)
    bullet_hit_list = pygame.sprite.spritecollide(bullet, bb_list, True)

    

    for blocks in bb_hit_list:
        bad_sound.play()
        

    for blocks in bullet_hit_list:
        score += 1
        x = random.randrange(3)

        if x == 2:
            y = 2
        else:
            y = 1

        for i in range (y):
            block = Bad_block(BLACK, 20, 20)
            block.rect.x = random.randrange(screen_width-20)
            block.rect.y = random.randrange(-500,0)
            bb_list.add(block)
            all_sprites_list.add(block)
        
        
    
    if len(bb_hit_list) == 1:
        end = True
    

    all_sprites_list.draw(screen)

    
    font = pygame.font.SysFont('Calibri', 25, True, False)

    text = font.render(str(score), True, GREEN)

    screen.blit(text, [0,0])

    

    if end == True:

        screen.fill (BLACK)

        font = pygame.font.SysFont('Calibri', 25, True, False)

        text = font.render(str(score), True, GREEN)

        screen.blit(text, [250,250])

        done = True
    
 
    pygame.display.flip()
 
    clock.tick(60)

    
 
pygame.quit()

