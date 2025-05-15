import pygame
pygame.init()
gui_font = pygame.font.Font(None,30)

class Button:
    def __init__(self,screen,text,width,height,pos=(0,0),elevation = 6) -> None:
        self.screen = screen

        #Core attributes
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.orignal_y_pos = pos[1]

        #top rectangle
        self.top_rect = pygame.Rect(pos,(width,height))
        self.top_color = '#475F77'

        #bottom rectangle
        self.bottom_rect = pygame.Rect(pos,(width,elevation))
        self.bottom_color = '#354B5E'

        #text
        self.text_surf = gui_font.render(text,True, '#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)
    
    def clicked(self):
        self.draw()
        return self.check_click()

    def draw(self):
        #elevation login
        self.top_rect.y = self.orignal_y_pos - self.dynamic_elevation
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation
        

        pygame.draw.rect(self.screen,self.bottom_color,self.bottom_rect, border_radius = 12)
        pygame.draw.rect(self.screen, self.top_color,self.top_rect, border_radius = 12)
        self.screen.blit(self.text_surf,self.text_rect)
        
    
    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            #D74B4B
            self.top_color = '#D74B4B'
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 50/100 * self.elevation
                self.pressed = True
            else:
                self.dynamic_elevation = self.elevation
                if self.pressed == True:
                    self.pressed = False
                    return True
        else:
            self.top_color = '#475F77'
            self.dynamic_elevation = self.elevation
            self.pressed = False
        return False
