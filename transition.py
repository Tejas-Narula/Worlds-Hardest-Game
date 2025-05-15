import pygame

def fade_in(screen): 
    fade = pygame.Surface((2000,2000))
    fade.fill((0,0,0))
    for alpha in range(0, 100):
        fade.set_alpha(alpha)
        #redrawWindow()
        screen.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(10)

def fade_out(screen):
    screen_test = pygame.Surface((2000,2000))
    screen_test.fill((100,100,0))
    fade = pygame.Surface((2000,2000))
    fade.fill((0,0,0))
    for alpha in range(0, 255):
        fade.set_alpha(255 - alpha)
        screen.blit(screen_test,(0,0))
        screen.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(10)