import pygame
class Levels():
    def __init__(self) -> None:
      self.width,self.height = pygame.display.get_window_size()
      self.rect_list = []

    def draw(self, screen, level_dat):
        self.rect_list = []
        #draw border
        #for b in self.border:
            #self.rect_list.append(b.rect)
            #b.draw(screen)
      
        #draw level
        for object in level_dat:
            try:
                self.rect_list.append(object.rect)
            except AttributeError:
                pass #putting exception for now, but to check for lava I need to fix this!
            if object != None:
              object.draw(screen)

    def draw_editor_stuf(self,screen, obj_in_hand):
        if obj_in_hand != None:
          obj_in_hand.draw(screen)
