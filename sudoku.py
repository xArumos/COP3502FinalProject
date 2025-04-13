import pygame, sys
from constants import *
from Board import *
from Cell import *
from sudoku_generator import *

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")

def main():
    def game_start():
        start_title_font = pygame.font.Font(None, 100)
        button_font = pygame.font.Font(None, 70)

        screen.fill(BG_COLOR)

        title_surface = start_title_font.render("SUDOKU", 0, BLACK)
        title_rectangle = title_surface.get_rect(
            center=(WIDTH // 2, HEIGHT // 2 - 150)
        )
        screen.blit(title_surface, title_rectangle)

        easy_text = button_font.render("Easy", 0, BLACK)
        medium_text = button_font.render("Medium", 0, BLACK)
        hard_text = button_font.render("Hard", 0, BLACK)
        quit_text = button_font.render("Quit", 0, BLACK)

        easy_surface = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))
        easy_surface.fill(GREY)
        easy_surface.blit(easy_text, (10, 10))

        medium_surface = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))
        medium_surface.fill(GREY)
        medium_surface.blit(medium_text, (10, 10))

        hard_surface = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
        hard_surface.fill(GREY)
        hard_surface.blit(hard_text, (10, 10))

        quit_surface = pygame.Surface((quit_text.get_size()[0] + 20, quit_text.get_size()[1] + 20))
        quit_surface.fill(GREY)
        quit_surface.blit(quit_text, (10, 10))

        easy_rectangle = easy_surface.get_rect(
            center=(WIDTH // 2 - 180, HEIGHT // 2)
        )
        medium_rectangle = medium_surface.get_rect(
            center=(WIDTH // 2, HEIGHT // 2)
        )
        hard_rectangle = hard_surface.get_rect(
            center=(WIDTH // 2 + 180, HEIGHT // 2)
        )
        quit_rectangle = quit_surface.get_rect(
            center=(WIDTH // 2, HEIGHT // 2 + 150))

        screen.blit(quit_surface, quit_rectangle)
        screen.blit(easy_surface, easy_rectangle)
        screen.blit(medium_surface, medium_rectangle)
        screen.blit(hard_surface, hard_rectangle)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if quit_rectangle.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()
                    elif easy_rectangle.collidepoint(event.pos):
                        board = Board(WIDTH, HEIGHT, screen, "easy")
                        board.draw()
                    elif medium_rectangle.collidepoint(event.pos):
                        board = Board(WIDTH, HEIGHT, screen, "medium")
                        board.draw()
                    elif hard_rectangle.collidepoint(event.pos):
                        board = Board(WIDTH, HEIGHT, screen, "hard")
                        board.draw()
            pygame.display.flip()

    def game_over():
        pass

    def game_in_progress():
        pass


    game_start()

main()