import time
import sys
import pygame

pygame.init()

background_colour = (234, 212, 252)

SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800

screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption('Akinator')
screen.fill(background_colour)
pygame.display.flip()

start_img = pygame.image.load('start_btn.png').convert_alpha()
exit_img = pygame.image.load('exit_btn.png').convert_alpha()
yes_img = pygame.image.load('yes_btn.png').convert_alpha()
no_img = pygame.image.load('no_btn.png').convert_alpha()

font = pygame.font.Font('font.ttf', 12)
font1 = pygame.font.Font('font.ttf', 20)
purple = (205,96,144)

class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
    
    def draw(self):
        action = False 
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action

def lbl(txt, speed=0.01):
    for char in txt:
        print(char, end='')
        sys.stdout.flush()
        time.sleep(speed)
    print('')

def textt(text, x, y):
 x = x
 y = y
 mes = font.render(text,True, purple)
 textRect = mes.get_rect()
 textRect.center = (x // 2, y // 2)
 screen.blit(mes, textRect)
 pygame.display.update()

def textt1(text, x, y):
 x = x
 y = y
 mes = font1.render(text,True, purple)
 textRect = mes.get_rect()
 textRect.center = (x // 2, y // 2)
 screen.blit(mes, textRect)
 pygame.display.update()  

textt1('Welcome to Akinator!', 780, 300)
textt('Think about someone in COM. I will try to guess who is it :>', 785, 410)
textt('Answer the questions with 1 for Yes or 2 for No.', 785, 500)

def game():
 yes_button = Button(150, 350, yes_img, 0.6)
 no_button = Button(500, 350, no_img, 0.6)

 not_used = ['Is this person a woman?', "Is this person's hair long?", "Is this person's hair curly/wavy?", "Is this person a student?", "Does this person watch anime?", "Is this person kyrgyz?", "Does this person wear glasses?"]
 for question in not_used:

  screen.fill(background_colour)
  
  for i in question:
   sys.stdout.write(i)
   sys.stdout.flush()
   time.sleep(0.05)
  textt1('', 785, 410)

  if yes_button.draw():
   answer.append(1)
  elif no_button.draw():
   answer.append(2)
   
  textt1(question, 785, 410)

def results():
 if answer == Alymbek:
  textt1("We guess this person is Alymbek.", 785, 410) 
 elif answer == Dovlyat:
  textt1("We guess this person is Dovlyat.", 785, 410)
 elif answer == Burul:
  textt1("We guess this person is miss Burul.", 785, 410)
 elif answer == Ruslan:
  textt1("We guess this person is Ruslan Isaev.", 785, 410)
 elif answer == Abiy:
  textt1("We guess this person is Abiy.", 785, 410)
 elif answer == Kurstan:
  textt1("We guess this person is Kurstan.", 785, 410)
 elif answer == SaeYeon:
  textt1("We guess this person is Sae Yeon.", 785, 410)
 elif answer == Erik:
  textt1("We guess this person is Erik.", 785, 410)
 elif answer == Zhumaniiaz:
  textt1("We guess this person is Zhumaniiaz Mamataliev.", 785, 410)
 elif answer == Adel:
  textt1("We guess this person is Adel.", 785, 410)
 elif answer == Akylai:
  textt1("We guess this person is Akylai.", 785, 410)
 elif answer == Aruuke:
  textt1("We guess this person is Aruuke.", 785, 410)
 elif answer == Aliia:
  textt1("We guess this person is Aliia.", 785, 410)
 elif answer == Roza:
  textt1("We guess this person is Roza.", 785, 410)
 else: 
  textt1("Your person is too hard to guess.", 785, 410)
  textt1("Are you sure you answered correctly?", 785, 500)

Alymbek = [2, 2, 2, 1, 1, 1, 2] 
Dovlyat = [2, 2, 2, 1, 2, 2, 1]
Burul = [1, 1, 2, 2, 2, 1, 2]
Ruslan = [2, 2, 2, 2, 1, 2, 2]
Abiy = [2, 2, 1, 1, 1, 1, 2]
Kurstan = [2, 2, 2, 1, 1, 1, 1]
SaeYeon = [1, 1, 2, 1, 1, 2, 2]
Erik = [2, 2, 2, 1, 1, 2, 1]
Zhumaniiaz = [2, 2, 2, 2, 2, 1, 1]
Adel = [1, 1, 2, 1, 1, 1, 1]
Akylai = [1, 2, 2, 1, 1, 1, 2]
Aruuke = [1, 1, 1, 1, 2, 1, 2]
Aliia = [1, 1, 2, 1, 1, 1, 2]
Roza = [1, 2, 1, 1, 2, 1, 2]
answer = []

start_button = Button(150, 350, start_img, 0.6)
exit_button = Button(500, 350, exit_img, 0.6)

running = True
while running:
 if start_button.draw():
  screen.fill(background_colour)
  game()
  screen.fill(background_colour)
  results()
 if exit_button.draw():
  running = False

 for event in pygame.event.get():
  if event.type == pygame.QUIT:
   running = False
 pygame.display.update()

pygame.quit()