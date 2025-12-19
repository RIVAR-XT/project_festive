import pygame
pygame.init()


pygame.font.init()

class Button:
    def __init__(self, x, y, width, height, function, scale1 , scale2, text, bt_color , image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.function = function
        self.scale = scale1
        self.scale2 = scale2
        self.text = text
        self.bt_color = bt_color
        self.width_image = image.get_width()
        self.hight_image = image.get_height()
        self.image = pygame.transform.scale(image ,(int(self.hight_image * self.scale) , (self.width_image * self.scale2)))
        self.image_rect = image.get_rect()

        self.image_rect.topleft = (x , y)

        # Create button surface
        self.surface = pygame.Surface((width, height))

        self.rect = pygame.Rect(x , y , width , height)

        # Font
        self.font = pygame.font.Font(None, 32)

        self.clicked = False
        

    def draw(self, screen , margin_x , margin_y):
        action = False

        # Get mouse position
        pos = pygame.mouse.get_pos()

        # Button click handling
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                print("Button clicked!")
                self.clicked = True
                self.function()
                action =True
         

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        # Draw button
        pygame.draw.rect(screen, self.bt_color, self.rect)

        # Draw text
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        screen.blit(text_surface, (self.rect.x + margin_x , self.rect.y + margin_y))


        return action
    
    def draw_image(self , screen):
        action = False
        get_pos = pygame.mouse.get_pos()
        print(get_pos)
        if self.image_rect.collidepoint(get_pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                print("image hi")
                self.clicked = True
                self.function()
                action = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
            


        screen.blit(self.image , (self.image_rect.x , self.image_rect.y))

        return action

    def text_box(self):
        active = False
        mousepos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
          if self.rect.collidepoint(mousepos):
             active = True
          else :
            active =False

            
        user_input = ''
        if event.type == pygame.KEYDOWN :
            if active == True:
               if event.key == pygame.K_BACKSPACE:
                  user_input = user_input[0 : -1]
                
            else:
                user_input += event.unicode
                print('hi')
        pygame.draw.rect(screen, self.bt_color, self.rect)
        text_surface = self.font.render(user_input, True, (255, 255, 255))
        screen.blit(text_surface, (self.rect.x + 5 , self.rect.y + 5))
        self.rect.w = max(100 , text_surface.get_width()+10)



    



screen_h = 500
screen_w = 800






screen = pygame.display.set_mode((screen_w , screen_h))
pygame.display.set_caption('Festive Card')


run = True


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
    global state_menu
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






color = ((100,100,100))
image1 = pygame.image.load("/home/moath/Documents/py projects/pygamepr/first.jpg").convert_alpha()
image2 = pygame.image.load("/home/moath/Documents/py projects/pygamepr/second.jpg").convert_alpha()
image3 = pygame.image.load("/home/moath/Documents/py projects/pygamepr/third.jpg").convert_alpha()

start = Button(315, 149 , 144 , 60 , dunny  , 0.7 , 0.5 , 'Start' , color , image1)
ex = Button(315 , 230 , 144 , 60 , exi , 0.5 , 0.3 ,'exit' , color ,   image1)
im1 = Button(70, 60 , 144 , 60 , thridmenustates  , 3.85 , 1.25 , 'Start' , color , image1)
im2 = Button(70, 60 , 144 , 60 , thridmenustates  , 3.85 , 1.25 , 'Start' , color , image2)
im3 = Button(70, 60 , 144 , 60 , thridmenustates  , 3.85 , 1.25 , 'Start' , color , image3)
back = Button(452 , 451 , 100 , 40 , dunny , 0.5 , 0.3 ,'exit' , color ,   image1)
next_bt= Button(400 , 400 , 100 , 40 , inmenu , 0.5 , 0.3 ,'next' , color ,   image1)
textbox= Button(400 , 400 , 100 , 40 , inmenu , 0.5 , 0.3 ,'next' , color ,   image1)







while run :



    match state_menu :
        case 'Menu_start' :
             screen.fill((202 , 228 , 241))
             pso_che = pygame.mouse.get_pos()
             print(pso_che)
             if start.draw(screen , 53 ,20 ):
                 print('start')
    
    
             if ex.draw(screen , 53 , 30):
                 print('exit')
        case 'pic_Menu':
                screen.fill((202 , 228 , 241))
                im1.draw_image(screen)
                if back.draw(screen , 10 ,10):
                      print('back bt is operationel')
                if next_bt.draw(screen , 10 , 10):
                    print('opper')
        case 'Menu_pic1':
                screen.fill((202 , 228 , 241))
                im2.draw_image(screen)
                if back.draw(screen , 10 ,10):
                      print('back bt is operationel')
                if next_bt.draw(screen , 10 , 10):
                    print('opper')
        case 'Menu_pic2' :
                screen.fill((202 , 228 , 241))
                im3.draw_image(screen)
                if back.draw(screen , 10 ,10):
                      print('back bt is operationel')
        case 'Menu4':
            screen.fill((202 , 228 , 241))
            textbox.text_box()




            



   
    







    









    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False



    pygame.display.update()


pygame.quit()