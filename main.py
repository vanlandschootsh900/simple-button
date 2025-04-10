#Shay VanLandschoot
#--DATE--#
# Pygame game template

import pygame
import sys
import config # Import the config module

def init_game ():

    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT)) 
    pygame.display.set_caption(config.TITLE)
    return screen



def handle_events (button):
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            return False
        if events.type == pygame.MOUSEBUTTONDOWN:
            if button.collidepoint(events.pos):
                pygame.quit()
                sys.exit()
        elif events.type == pygame.KEYDOWN:
            if events.key == pygame.K_ESCAPE:
                return False
    return True

def main():
    
    screen = init_game()
    clock = pygame.time.Clock()

    airal = pygame.font.SysFont('airal',55)
    surf = airal.render('Quit', True, config.GREEN)

    button_length = 200
    button_width = 60 
    button_x = 300
    button_y = 125
    button = pygame.Rect(button_x,button_y,button_length,button_width)
    

    surf_rect = surf.get_rect()
    surf_rect.center = button.center

    running = True
    while running:
        running = handle_events(button)
        screen.fill(config.WHITE) # Use color from config
        
        # Add code to draw stuff (for example) below this comment
        mouse_x, mouse_y = pygame.mouse.get_pos() 
        
        if button.collidepoint(mouse_x, mouse_y):
            button_color=(config.RED)
        else:
            button_color=(config.GREEN)
        
        pygame.draw.rect(screen, button_color,button)
        screen.blit(surf,surf_rect)

        pygame.display.flip()
        # Limit the frame rate to the specified frames per second (FPS)
        clock.tick(config.FPS)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
