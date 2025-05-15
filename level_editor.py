#-------------------CAN ONLY BE RAN THROUGH THE LEVEL SELECTOR----------------#
import pygame
import pickle


block_size = 16

pygame.init()
clock = pygame.time.Clock()


class Ground():
  def __init__(self, x, y, width = 16, height = 16, color = (0,0,0)) -> None:
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.color = color
    self.name = "ground"

    self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
  
  def draw(self, screen):
    pygame.draw.rect(screen,(0,0,0),self.rect)

class Lava(): #surface obj causing problems, removed until fixed
  def __init__(self,x,y,width,height) -> None:
    self.name = "lava"
    self.screen = screen
    
    self.x = x
    self.y = y
    self.width = width
    self.height = height

    self.surface = pygame.Surface((self.width,16))

  def draw(self, screen):
    #create lava
    self.surface.fill((255,255,255))
    for i in range(block_size - 3):
      self.rect = pygame.Rect(0,i + 3,self.width,self.height)
      pygame.draw.rect(self.surface,(196, 38, 6),self.rect)
    
    screen.blit(self.surface, (self.x, self.y))

class Player():
    def __init__(self, x, y, width = 16, height = 20, color = (0,255,0)) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.name = "player"

        self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
    
    def draw(self, screen):
        pygame.draw.rect(screen,self.color,self.rect)

class Main():
    def __init__(self, level_num = 0) -> None:
        from level_handler import Levels
        self.Levels_class = Levels
        self.level_num = level_num
        self.obj_held = None
        self.obj = ""

    def load(self,level):
        global loaded_level
        try:
            loaded_level = pickle.load(open(f"levels/level_{level}.supelvl","rb"))
        except EOFError:
            loaded_level = []
        except FileNotFoundError:
            loaded_level = []
        return loaded_level

    def save(self, name: int, level_dat: list | dict):
        pickle.dump(level_dat, open(f"levels/level_{name}.supelvl","wb"))
    
    def in_hand(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        left, middle, right = pygame.mouse.get_pressed()
        if self.obj == "ground":
            self.obj_held =  Ground(mouse_x,mouse_y,16,16)
        elif self.obj == "ground_large":
            self.obj_held =  Ground(mouse_x,mouse_y,64,16)
        elif self.obj == "lava":
            self.obj_held =  Lava(mouse_x,mouse_y,16,16)
        elif self.obj == "player":
            self.obj_held = Player(mouse_x,mouse_y)
        else:
            self.obj_held = None

        if self.obj != "":
            if left:
                if self.obj == "player":
                    for obj in self.level:
                        if obj.name == "player":
                            self.level.remove(obj)
                    self.obj = ""
                
                self.level.append(self.obj_held)
    
    def draw_grids(self):
        grid_surface = pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT))
        for i in range(SCREEN_WIDTH):
            rect = pygame.Rect(i,0,2,SCREEN_HEIGHT)
            pygame.draw.rect(grid_surface,(255, 0, 0),rect)
        
        screen.blit(grid_surface,(0,0))
            

    def run(self):
        global screen, SCREEN_HEIGHT, SCREEN_WIDTH
        self.level = self.load(self.level_num)

        fullscreen = True
        if fullscreen: screen = pygame.display.set_mode((0, 0),pygame.FULLSCREEN)
        else: screen = pygame.display.set_mode((1000,600),)

        SCREEN_WIDTH,SCREEN_HEIGHT = pygame.display.get_window_size() #getting screen size, if in fullscreen
        
        running = True
        while running:
            
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE and self.obj== "":
                        running = False
                    elif event.key == pygame.K_ESCAPE and self.obj != "":
                        self.obj = ""
                        
                    if event.key == pygame.K_1:
                        self.obj = "ground"
                    if event.key == pygame.K_2:
                        self.obj = "ground_large"
                    if event.key == pygame.K_3:
                        pass
                        #self.obj = "Lava" #Lava - removed due to errors
                    if event.key == pygame.K_0:
                        self.obj = "player"
            
            self.draw_grids()
            self.in_hand()
            
            screen.fill((255,255,255))
            self.Levels_class().draw(screen,self.level)
            self.Levels_class().draw_editor_stuf(screen, self.obj_held)

            pygame.display.update()
            clock.tick(60)
        
        screen.fill((255,255,255))
        self.save(self.level_num,self.level)
