import pygame ,sys

# pygame.init()
# screen=pygame.display.set_mode((800,400))
# pygame.display.set_caption('Hello World')
# while True:
#     for event in pygame.event.get():
#         if event.type== pygame.QUIT:
#             pygame.quit()
#             sys.exit()

# pygame.init()
# screen = pygame.display.set_mode((640, 480))
# pygame.display.set_caption('hello world')

# while True:
#      for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#         if event.type==pygame.KEYDOWN:
#             key=pygame.key.name(event.key) 
#             print (key, "Key is pressed")
#         if event.type == pygame.KEYUP:
#             key=pygame.key.name(event.key) 
#             print (key, "Key is released") 
# pygame.init()
# screen=pygame.display.set_mode((500,200))
# done=False
# red=(255,0,0)
# blue=(0,255,0)
# green=(0,0,255)
# white=(255,255,255)
# while not done:
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             done=True
#     pygame.draw.rect(screen, red, pygame.Rect(100, 30, 60, 60))
#     pygame.draw.polygon(screen, blue, ((25,75),(76,125),(275,200),(350,25),(60,280)))
#     pygame.draw.circle(screen, white, (180,180), 60)
#     pygame.draw.line(screen, red, (10,200), (300,10), 4)
#     pygame.draw.ellipse(screen, green, (250, 200, 130, 80)) 
#     pygame.display.update()
# from pygame.locals import *
# from sys import exit
# pygame.init()
# image_filename = 'D:\SABA\mahindra_thar_everest_white.png'
# screen=pygame.display.set_mode((800,400),0,40)
# pygame.display.set_caption('Moving image')
# a=pygame.image.load(image_filename)
# x=0
# while True:
#     screen.fill((255,255,255))
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             exit()
#     screen.blit(a,(x,100))
#     x=x+0.5

#     if x > 400:
#        x = x-400
#     pygame.display.update() 

    
import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False

font = pygame.font.SysFont("Arial", 14)
text1=font.render(" START ", True, 'white')
text2=font.render(" PLAY ", True, 'white')
text3=font.render(" STOP ", True, 'white')

rect1 = text1.get_rect(topleft=(10,10))
rect2 = text2.get_rect(topleft= (100,10))
rect3 = text3.get_rect(topleft= (200,10))
bg = (127,127,127)
msg=" "
screen = pygame.display.set_mode((400,300))
screen.fill(bg)
while not done:
   for event in pygame.event.get():
      screen.blit(text1, rect1)
      pygame.draw.rect(screen, (255,0,0),rect1,2)
      screen.blit(text2, rect2)
      pygame.draw.rect(screen, (255,0,0),rect2,2)
      pygame.draw.rect(screen, (255,0,0),rect3,2)
      screen.blit(text3, rect3)
      
      if event.type == pygame.QUIT:
         done = True
      if event.type == pygame.MOUSEBUTTONDOWN:
         if rect1.collidepoint(event.pos):
            msg = "START Button was pressed"
         if rect2.collidepoint(event.pos):
            msg = "PLAY Button was pressed"
         if rect3.collidepoint(event.pos):
            msg = "STOP Button was pressed"
      img=font.render(msg, True, (0,0,255))
      imgrect=img.get_rect()
      imgrect.center = (200 , 150 )
      pygame.draw.rect(screen, bg, imgrect)
      screen.blit(img, imgrect)

   pygame.display.update()