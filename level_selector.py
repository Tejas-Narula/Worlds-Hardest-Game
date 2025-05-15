import pygame
from button import Button
import level_editor
import game
import os
from transition import fade_in,fade_out

pygame.init()
clock = pygame.time.Clock()

class Screen():
  def __init__(self, screen) -> None:
    self.screen = screen
    
    self.width,self.height = pygame.display.get_window_size()

    self.btn_starting_Xpos = 10
    self.levels_dir = os.listdir('levels')

    self.screen.fill((0,0,0))  
  def load_buttons(self):
    button_list= []
    levels_num = len([name for name in self.levels_dir])
    for i in range(levels_num):
      button_list.append(Button(self.screen, str(i),50,50,(self.btn_starting_Xpos + 60*i,10),6))
    
    #new level btn
    button_list.append(Button(self.screen, "+",50,50,(self.btn_starting_Xpos + 60*levels_num,10),6))
    return button_list
  
  def run(self, type):
    #get all levels and create a button for each
    self.button_list = self.load_buttons()
      
    running = True
    while running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()
        
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
            running = False
        
      self.screen.fill((255,255,255))
      if type == "editor":
        for level in range(len(self.button_list)-1):
          if self.button_list[level].clicked(): level_editor.Main(level).run()

        #add level btn
        if self.button_list[-1].clicked():
          print("start")
          level_editor.Main(len(self.button_list)-1).run()
          print("end")
          running = False
      elif type == "play":
        for level in range(len(self.button_list)-1):
          
          if self.button_list[level].clicked(): game.game.run(level)

      pygame.display.update()
      clock.tick(60)