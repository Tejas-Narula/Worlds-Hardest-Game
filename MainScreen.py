import level_selector
import pygame,sys
from button import Button
from transition import fade_in, fade_out

pygame.init()

screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
pygame.display.set_caption('Main screen')

clock = pygame.time.Clock()

SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_window_size()

StartGame_btn = Button(screen, 'Play',200,40,(SCREEN_WIDTH/2-100,SCREEN_HEIGHT/2))
levelHandler_btn = Button(screen, 'Level editor',200,40,(SCREEN_WIDTH/2-100,SCREEN_HEIGHT/2+60))




while True:
    screen.fill('#DCDDD8')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit() 

    if StartGame_btn.clicked():
        level_selector.Screen(screen).run("play")
    if levelHandler_btn.clicked():
        level_selector.Screen(screen).run("editor")

    pygame.display.update()
    clock.tick(60)