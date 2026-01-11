import pygame
import apifortemp2  
import apifortemp1 
import apifortemp3
import random
import time
#initialize pygame
pygame.init()
pygame.font.init()
pygame.mixer.init()
pygame.mixer.music.load("click.mp3")
pygame.mixer.music.set_volume(0.7)
pygame.display.set_caption('Festive Card')
clock = pygame.time.Clock()
FPS = 30
# Global variables
id_pic = 0
sent_api = False
screen_h = 500
screen_w = 800
cleared = True
run = True
screen = pygame.display.set_mode((screen_w , screen_h))
rotation_angle = 0
image1 = pygame.image.load("first.jpg").convert_alpha()
image2 = pygame.image.load("second.jpg").convert_alpha()
image3 = pygame.image.load("third.jpg").convert_alpha()
font = pygame.font.Font(None, 32)
# Snowflake animation
snowflakes = []
for i in range(20):  # Create 20 snowflakes
    snowflakes.append({
        'x': random.randint(0, 800),
        'y': random.randint(-50, 500),
        'speed': random.uniform(1, 3)
    })








# class with all button functions

class Button:
    def __init__(self, x, y, width, height, function, scale1 , scale2, text, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.function = function
        self.text = text
        self.user_input = ''
        self.bt_color = 'plain'
        self.width_image = image.get_width()
        self.hight_image = image.get_height()
        self.image = pygame.transform.scale(image ,(int(self.hight_image * scale1) , (self.width_image * scale2)) )
        self.image_rect = image.get_rect()
        self.active = False
        self.active_color = (255,0,0)
        self.ionactive_color = (0,255,0)
        self.inactive_bt_color = (100,100,100)
        self.active_bt_color = (179,179,179)

        self.image_rect.topleft = (x , y)

        # Create button surface
        self.surface = pygame.Surface((width, height))

        self.rect = pygame.Rect(x , y , width , height)

        # Font
       

        self.clicked = False
        

    def draw(self, screen , margin_x , margin_y):
        action = False
        active = False

        # Get mouse position
        pos = pygame.mouse.get_pos()

        # Button click handling
        if self.rect.collidepoint(pos):
            active = True

            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                print("Button clicked!")
                pygame.mixer.music.play()
                self.clicked = True
                self.function()
                action =True
         

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        # Draw button
        if active:
            self.bt_color = self.active_bt_color
        else:
            self.bt_color = self.inactive_bt_color
        pygame.draw.rect(screen, self.bt_color, self.rect)

        # Draw text
        text_surface = font.render(self.text, True, (255, 255, 255))
        screen.blit(text_surface, (self.rect.x + margin_x , self.rect.y + margin_y))


        return action
    
    def draw_image(self , screen):
        action = False
        get_pos = pygame.mouse.get_pos()
        print(get_pos)
        if self.image_rect.collidepoint(get_pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                print("image hi")
                pygame.mixer.music.play()
                self.clicked = True
                self.function()
                action = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
            


        screen.blit(self.image , (self.image_rect.x , self.image_rect.y))

        return action

    def text_box(self , screen , event):
        if event is not None:
            if event.type == pygame.MOUSEBUTTONDOWN:
                 self.active = self.rect.collidepoint(event.pos)
            if event.type == pygame.KEYDOWN and self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.user_input = self.user_input[:-1]
                elif event.key == pygame.K_RETURN:
                    print(self.user_input)
                else:
                    self.user_input += event.unicode
        
        active_color = self.active_color if self.active else self.ionactive_color
        pygame.draw.rect(screen, active_color, self.rect, 2)    
        text_surface = font.render(self.user_input, True, (0, 0, 0))
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5 ))
        return self.user_input
   
        
              
 

    














# functions to change states
state_menu = 'Menu_start'
id_pic = 'placeholder'
def dummy():
    pass

def exi():
    global run
    run = False
def dunny ():
    global state_menu
    match state_menu:
        case 'Menu_start' :
            state_menu = 'pic_Menu'
        case 'pic_Menu':
            state_menu = 'Menu_start'
        case 'Menu_pic1':
            state_menu='pic_Menu'
        case 'Menu_pic2':
            state_menu = 'Menu_pic1'
def inmenu():
    global state_menu 
    match state_menu:
        case 'pic_Menu':
            state_menu = 'Menu_pic1'
        case 'Menu_pic1':
            state_menu = 'Menu_pic2'
        case 'Menu_pic2':
            state_menu = 'Menu_pic1'
def thridmenustates():
    global state_menu , cleared , id_pic
    match state_menu:
        case 'pic_Menu':
            state_menu = 'Menu4'
            id_pic = 1
        case 'Menu_pic1':
            state_menu = 'Menu4'
            id_pic = 2
        case 'Menu_pic2':
            state_menu = 'Menu4'
            id_pic =3
        case 'Menu4':
            state_menu = 'final_menu'
            
    cleared = False
    return id_pic
    







# construction of buttons
start = Button(315, 149 , 170 , 60 , dunny  , 0.7 , 0.5 , 'Start' , image1)
ex = Button(315 , 230 , 170 , 60 , exi , 0.5 , 0.3 ,'Exit' ,image1)
im1 = Button(70, 60 , 144 , 60 , thridmenustates  , 3.85 , 1.25 , 'Start' , image1)
im2 = Button(70, 60 , 144 , 60 , thridmenustates  , 3.85 , 1.25 , 'Start' , image2)
im3 = Button(70, 60 , 144 , 60 , thridmenustates  , 3.85 , 1.25 , 'Start' , image3)
back = Button(25 , 450 , 100 , 40 , dunny , 0.5 , 0.3 ,'Back' , image1)
next_bt= Button(675 , 450 , 100 , 40 , inmenu , 0.5 , 0.3 ,'Next' , image1)
textbox= Button(59, 75, 100, 40, inmenu, 1,1, 'next', image1)
textbox2= Button(59, 200, 100, 40, inmenu, 1, 1, 'next', image2)
textbox3= Button(59, 300, 100, 40, inmenu, 1, 1, 'next', image3)
Done = Button(675 , 425 , 100 , 40 , thridmenustates , 0.5 , 0.3 ,'Done' , image1)






# main loop
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if state_menu == 'Menu4':
            
            sendertxt =font.render("Sender Name :", True, (0, 0, 0))
            screen.blit(sendertxt, (59, 40))
            recipienttxt = font.render("Recipient Name :", True, (0, 0, 0))
            screen.blit(recipienttxt, (59, 150))
            yeartxt = font.render("Year :", True, (0, 0, 0))
            screen.blit(yeartxt, (59, 260))
            textbox.text_box(screen, event)
            sender = textbox.user_input
            textbox2.text_box(screen, event)
            recipient = textbox2.user_input
            textbox3.text_box(screen, event)
            year = textbox3.user_input
            Done.draw(screen, 25, 10)
            print(pygame.mouse.get_pos())
            
    
    match state_menu:
        # start menu
        case 'Menu_start':
            screen.fill((179, 45, 0))
            pygame.draw.rect(screen, (0, 153, 51), pygame.Rect(0, 225, 800, 25))
            pygame.draw.rect(screen, (0, 153, 51), pygame.Rect(385, 0, 25, 800))
            
            # Draw and update snowflakes
            for snowflake in snowflakes:
                pygame.draw.circle(screen, (255, 255, 255), (int(snowflake['x']), int(snowflake['y'])), 3)
                snowflake['y'] += snowflake['speed']
                snowflake['x'] += random.uniform(-0.5, 0.5)  # Drift side to side
                if snowflake['y'] > 500:
                    snowflake['y'] = -10
                    snowflake['x'] = random.randint(0, 800)
             
            if start.draw(screen, 60, 20):
                print('start')
            if ex.draw(screen, 60, 20):
                print('exit')
        # pic selection menu 1
        case 'pic_Menu':
            sent_api = False
            screen.fill((179, 45, 0))
            pygame.draw.rect(screen, (0, 153, 51), pygame.Rect(0, 225, 800, 25))
            pygame.draw.rect(screen, (0, 153, 51), pygame.Rect(385, 0, 25, 800))
                        # Draw and update snowflakes
            for snowflake in snowflakes:
                pygame.draw.circle(screen, (255, 255, 255), (int(snowflake['x']), int(snowflake['y'])), 3)
                snowflake['y'] += snowflake['speed']
                snowflake['x'] += random.uniform(-0.5, 0.5)  # Drift side to side
                if snowflake['y'] > 500:
                    snowflake['y'] = -10
                    snowflake['x'] = random.randint(0, 800)
            im1.draw_image(screen)
            if back.draw(screen, 25, 10):
                print('back bt is operationel')
            if next_bt.draw(screen, 25, 10):
                print('opper')
        # pic selection menu 2
        case 'Menu_pic1':
            sent_api = False
            screen.fill((179, 45, 0))
            pygame.draw.rect(screen, (0, 153, 51), pygame.Rect(0, 225, 800, 25))
            pygame.draw.rect(screen, (0, 153, 51), pygame.Rect(385, 0, 25, 800))
                        # Draw and update snowflakes
            for snowflake in snowflakes:
                pygame.draw.circle(screen, (255, 255, 255), (int(snowflake['x']), int(snowflake['y'])), 3)
                snowflake['y'] += snowflake['speed']
                snowflake['x'] += random.uniform(-0.5, 0.5)  # Drift side to side
                if snowflake['y'] > 500:
                    snowflake['y'] = -10
                    snowflake['x'] = random.randint(0, 800)
            im2.draw_image(screen)
            if back.draw(screen, 10, 10):
                print('back bt is operationel')
            if next_bt.draw(screen, 10, 10):
                print('opper')
        # pic selection menu 3
        case 'Menu_pic2':
            sent_api = False
            screen.fill((179, 45, 0))
            pygame.draw.rect(screen, (0, 153, 51), pygame.Rect(0, 225, 800, 25))
            pygame.draw.rect(screen, (0, 153, 51), pygame.Rect(385, 0, 25, 800))
                        # Draw and update snowflakes
            for snowflake in snowflakes:
                pygame.draw.circle(screen, (255, 255, 255), (int(snowflake['x']), int(snowflake['y'])), 3)
                snowflake['y'] += snowflake['speed']
                snowflake['x'] += random.uniform(-0.5, 0.5)  # Drift side to side
                if snowflake['y'] > 500:
                    snowflake['y'] = -10
                    snowflake['x'] = random.randint(0, 800)
            im3.draw_image(screen)
            if back.draw(screen, 10, 10):
                print('back bt is operationel')
        # menu to enter names
        case 'Menu4':
            if cleared == False:
        
               screen.fill((179, 45, 0))
               pygame.draw.rect(screen, (0, 153, 51), pygame.Rect(0, 225, 800, 25))
               pygame.draw.rect(screen, (0, 153, 51), pygame.Rect(385, 0, 25, 800))
               yellow = (255, 255, 0)
               dark_green = (0, 100, 0)
               white = (255, 255, 255)

               pygame.draw.circle(screen, white, (506, 74), 30)
               pygame.draw.circle(screen, dark_green, (670, 124), 30)
               pygame.draw.circle(screen, white, (573, 323), 30)
               pygame.draw.circle(screen, white, (718, 322), 30)
               pygame.draw.circle(screen, dark_green, (476, 429), 30)


               
   
               cleared = True
               
        # final menu to show the card
        case 'final_menu':
            
            screen.fill((179, 45, 0))
            pygame.draw.rect(screen, (0, 153, 51), pygame.Rect(0, 225, 800, 25))
            pygame.draw.rect(screen, (0, 153, 51), pygame.Rect(385, 0, 25, 800))
                        # Draw and update snowflakes
            for snowflake in snowflakes:
                pygame.draw.circle(screen, (255, 255, 255), (int(snowflake['x']), int(snowflake['y'])), 3)
                snowflake['y'] += snowflake['speed']
                snowflake['x'] += random.uniform(-0.5, 0.5)  # Drift side to side
                if snowflake['y'] > 500:
                    snowflake['y'] = -10
                    snowflake['x'] = random.randint(0, 800)
            if sent_api == False:
             if id_pic == 1:
                 apifortemp1.first_api(sender , recipient , year)
                 image_new = pygame.transform.scale(pygame.image.load("file.jpg").convert_alpha() , ( 300 , 171 ))
                 file_image =Button(70, 60 , 144 , 60 , dummy , 3.85 , 1.25 , 'Start' , image_new)
                 
                 sent_api = True
             elif id_pic == 2: 
                 apifortemp2.second_api(sender , recipient , year)
                 image_new = pygame.transform.scale(pygame.image.load("file.jpg").convert_alpha() , ( 300 , 171 ))
                 file_image =Button(70, 60 , 144 , 60 , dummy , 3.85 , 1.25 , 'Start' , image_new)
                 sent_api = True
             elif id_pic == 3:
                 apifortemp3.third_api(sender , recipient , year)
                 image_new = pygame.image.load("file.jpg").convert_alpha()
                 file_image =Button(70, 60 , 144 , 60 , dummy , 3.85 , 1.25 , 'Start' , image_new)
                 sent_api = True
             elif id_pic == 0:
                 print('no pic selected')
            
            
            
            file_image.draw_image(screen)

                
    
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
