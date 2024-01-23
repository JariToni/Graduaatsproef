import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE
from checkers.game import Game

FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

checkers_rect = pygame.Rect(WIDTH // 2 - 75, 300, 150, 50)
quit_rect = pygame.Rect(WIDTH // 2 - 75, 400, 150, 50)

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def draw_main_screen():
    WIN.fill((50, 121, 168))

    welcome_font = pygame.font.SysFont(None, 36)

    
    welcome_text = welcome_font.render("Welcome", True, (255, 255, 255)) 
    WIN.blit(welcome_text, (WIDTH // 2 - welcome_text.get_width() // 2, 250))

    button_font = pygame.font.SysFont(None, 28)

    # Checkers-knop
    checkers_button = button_font.render("Checkers", True, (255, 255, 255))
    pygame.draw.rect(WIN, (28, 28, 28), checkers_rect)
    
    WIN.blit(checkers_button, (checkers_rect.centerx - checkers_button.get_width() // 2, checkers_rect.centery - checkers_button.get_height() // 2))

    # Quit-knop
    quit_button = button_font.render("Quit", True, (255, 255, 255))
    pygame.draw.rect(WIN, (28, 28, 28), quit_rect)
    WIN.blit(quit_button, (quit_rect.centerx - quit_button.get_width() // 2, quit_rect.centery - quit_button.get_height() // 2))

    pygame.display.flip()

def main():
    pygame.init()

    run_main_screen = True
    run_checkers_game = False
    clock = pygame.time.Clock()
    game = None

    while run_main_screen:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_main_screen = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                # Checkers-knop
                if checkers_rect.collidepoint(pos):
                    run_main_screen = False
                    run_checkers_game = True

                # Quit-knop
                elif quit_rect.collidepoint(pos):
                    run_main_screen = False

        draw_main_screen()

    if run_checkers_game:
        game = Game(WIN)

        while True:
            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    row, col = get_row_col_from_mouse(pos)
                    game.select(row, col)

            game.update()

    pygame.quit()

if __name__ == "__main__":
    main()
