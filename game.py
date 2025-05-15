import pygame
from pygame.locals import *
from level_handler import Levels
import file_handler
import pickle

BACKGROUND_COLOR = (255,255,255)

pygame.display.set_caption('Platformer!')
clock = pygame.time.Clock()

class Player():
  def __init__(self, x, y) -> None:
    self.height = 20
    self.width = 16
    self.x = x
    self.y = y

    self.speed = 0
    self.max_speed = 6
    self.acceleration = 0.25
    self.friction = 0.09
    self.gravity = 0

    self.jumping = False

  def draw(self):
    
    self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
    pygame.draw.rect(screen,(214, 76, 17),self.rect)    
  
  def move(self):
    if "w" in game.keys_pressed:
      self.jumping = True
    else:
      self.jumping = False
    if "s" in game.keys_pressed:
      pass
    if "a" in game.keys_pressed:
      if self.speed > -self.max_speed: self.speed -= self.acceleration
    if "d" in game.keys_pressed:
      if self.speed < self.max_speed: self.speed += self.acceleration

    #friction
    if self.speed > 0.1:
      self.speed -= self.friction
    elif self.speed < -0.1:
      self.speed += self.friction
    elif self.speed > 0 < 0.1:
      self.speed = 0
    elif self.speed < 0 > -0.1:
      self.speed = 0

    #stopping the player from going thru the walls and grounds
    number_of_non_collided_rect = 0
    for platform in levels.rect_list:
      if self.rect.colliderect(platform):
        if abs(platform.top - self.rect.bottom) < 15:
          self.gravity = 0
          self.y = platform.y - self.height + 1
          if self.jumping:
            self.gravity = -3
        else:
          self.gravity += 0.25
          if abs(platform.bottom - self.rect.top) < 10:
            self.gravity += 0.1
          if abs(platform.right - self.rect.left) < 10:
            self.speed = 0
            self.x = platform.right
          if abs(platform.left - self.rect.right) < 10:
            self.speed = 0
            self.x = platform.left - self.width
      else:
        number_of_non_collided_rect += 1
    
    if number_of_non_collided_rect == len(levels.rect_list):
      self.gravity += 0.25

    self.x += self.speed
    self.y += self.gravity
  
  def reset(self):
    self.x = playerX
    self.y = playerY

    self.speed = 0
    self.gravity = 0

    self.jump = False

class Game():
  def __init__(self):
    self.keys_pressed = []
  
  def load_level(self, level):
    global loaded_level
    loaded_level =  pickle.load(open(f"levels/level_{level}.supelvl","rb"))
    return loaded_level
  
  def get_playerPos(self, remove_marker = True):
      global playerX, playerY
      for obj in loaded_level:
        if obj.name == "player":
          playerX, playerY = obj.x, obj.y
          if remove_marker: #removing player marker from list
            loaded_level.remove(obj)
          return [playerX, playerY]
      
      raise Exception("No player object found in level..?")

  def run(self, level):
    
    global levels, player, fullscreen, screen, SCREEN_HEIGHT, SCREEN_WIDTH
    self.level = level
    file_handler.run()
    
    fullscreen = True
    if fullscreen: screen = pygame.display.set_mode((0, 0),pygame.FULLSCREEN)
    else: screen = pygame.display.set_mode((1000,600),)

    SCREEN_WIDTH,SCREEN_HEIGHT = pygame.display.get_window_size() #getting screen size, if in fullscreen
    
    self.loaded_level = self.load_level(self.level) #might take time
    
    playerX, playerY = self.get_playerPos()
    levels = Levels()
    player = Player(playerX, playerY)
    
    #main loop
    self.running = True
    
    while self.running:
      screen.fill((BACKGROUND_COLOR))

      #event handler
      for event in pygame.event.get():
        if event.type == KEYDOWN:
          if event.key == K_ESCAPE:
            self.running = False
            

          if event.key == K_w or event.key == K_UP: self.keys_pressed.append("w")
          if event.key == K_a or event.key == K_LEFT: self.keys_pressed.append("a")
          if event.key == K_s or event.key == K_DOWN: self.keys_pressed.append("s")
          if event.key == K_d or event.key == K_RIGHT: self.keys_pressed.append("d")
          if event.key == K_r: player.reset()

        
        if event.type == KEYUP:
          if event.key == K_w or event.key == K_UP: self.keys_pressed.remove("w")
          if event.key == K_a or event.key == K_LEFT: self.keys_pressed.remove("a")
          if event.key == K_s or event.key == K_DOWN: self.keys_pressed.remove("s")
          if event.key == K_d or event.key == K_RIGHT: self.keys_pressed.remove("d")
        
        if event.type == pygame.QUIT:
          self.running = False
          exit()
      
      player.draw()
      player.move()

      levels.draw(screen, self.loaded_level)


      clock.tick(60)
      pygame.display.update()
    
    

game = Game()
if __name__ == "__main__":
  level = input("\n Pls run game using main.py\nlevel: ")
  print("")
  game.run(int(level))
