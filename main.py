# Ethan Lawrence 
# Feb 12 2025
# Pygame template ver 2

import pygame
import sys
import config

def init_game():
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True
def main():
    screen = init_game()
    clock = pygame.time.Clock()
    running = True

    # Fonts
    text_font1 = pygame.font.Font('DejaVuSans.ttf', 50)
    text_font2 = pygame.font.SysFont(None, 25, bold=True, italic=True)

    while running:
        running = handle_events()
        screen.fill(config.WHITE)
        draw_text(screen, 'Hello!', text_font1, config.BLACK, 200, 200)
        draw_text(screen, 'Welcome to my pygame script.', text_font2, config.GREY, 200, 300)
        
        pygame.display.flip()
        # Limit clock to FPS
        clock.tick(config.FPS)
        print(clock)
    pygame.quit()
    sys.exit()
def draw_text(screen, text, font, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

if __name__ == '__main__':
    main()