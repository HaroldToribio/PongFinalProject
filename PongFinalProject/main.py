import pygame
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Classic")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

PADDLE_WIDTH = 15
PADDLE_HEIGHT = 100
PADDLE_SPEED = 7

BALL_SIZE = 20

font = pygame.font.SysFont(None, 48)

MENU = 0
PLAYING = 1
GAME_OVER = 2

game_state = MENU


def reset_game():
    paddle_x = WIDTH - 40
    paddle_y = HEIGHT // 2 - PADDLE_HEIGHT // 2

    ball_x = WIDTH // 2
    ball_y = HEIGHT // 2

    ball_speed_x = 5
    ball_speed_y = 5

    score = 0

    return (
        paddle_x,
        paddle_y,
        ball_x,
        ball_y,
        ball_speed_x,
        ball_speed_y,
        score
    )


(
    paddle_x,
    paddle_y,
    ball_x,
    ball_y,
    ball_speed_x,
    ball_speed_y,
    score
) = reset_game()

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if game_state == MENU:

                if event.key == pygame.K_RETURN:
                    game_state = PLAYING

                if event.key == pygame.K_ESCAPE:
                    running = False

            elif game_state == GAME_OVER:

                if event.key == pygame.K_r:

                    (
                        paddle_x,
                        paddle_y,
                        ball_x,
                        ball_y,
                        ball_speed_x,
                        ball_speed_y,
                        score
                    ) = reset_game()

                    game_state = PLAYING

                if event.key == pygame.K_ESCAPE:
                    running = False

    screen.fill(BLACK)

    if game_state == MENU:

        title = font.render("PONG CLASSIC", True, WHITE)

        start_text = font.render(
            "Press ENTER to Start",
            True,
            WHITE
        )

        exit_text = font.render(
            "Press ESC to Exit",
            True,
            WHITE
        )

        screen.blit(
            title,
            (WIDTH // 2 - title.get_width() // 2, 180)
        )

        screen.blit(
            start_text,
            (WIDTH // 2 - start_text.get_width() // 2, 260)
        )

        screen.blit(
            exit_text,
            (WIDTH // 2 - exit_text.get_width() // 2, 320)
        )

    elif game_state == PLAYING:

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            paddle_y -= PADDLE_SPEED

        if keys[pygame.K_DOWN]:
            paddle_y += PADDLE_SPEED

        if paddle_y < 0:
            paddle_y = 0

        if paddle_y > HEIGHT - PADDLE_HEIGHT:
            paddle_y = HEIGHT - PADDLE_HEIGHT

        ball_x += ball_speed_x
        ball_y += ball_speed_y

        if ball_y <= 0:
            ball_speed_y *= -1

        if ball_y >= HEIGHT - BALL_SIZE:
            ball_speed_y *= -1

        if ball_x <= 0:
            ball_speed_x *= -1

        paddle_rect = pygame.Rect(
            paddle_x,
            paddle_y,
            PADDLE_WIDTH,
            PADDLE_HEIGHT
        )

        ball_rect = pygame.Rect(
            ball_x,
            ball_y,
            BALL_SIZE,
            BALL_SIZE
        )

        if ball_rect.colliderect(paddle_rect):
            ball_speed_x *= -1
            score += 1

        if ball_x > WIDTH:
            game_state = GAME_OVER

        pygame.draw.rect(
            screen,
            WHITE,
            paddle_rect
        )

        pygame.draw.ellipse(
            screen,
            WHITE,
            ball_rect
        )

        score_text = font.render(
            f"Score: {score}",
            True,
            WHITE
        )

        screen.blit(score_text, (20, 20))

    elif game_state == GAME_OVER:

        game_over_text = font.render(
            "GAME OVER",
            True,
            RED
        )

        score_text = font.render(
            f"Final Score: {score}",
            True,
            WHITE
        )

        restart_text = font.render(
            "Press R to Play Again",
            True,
            WHITE
        )

        exit_text = font.render(
            "Press ESC to Exit",
            True,
            WHITE
        )

        screen.blit(
            game_over_text,
            (
                WIDTH // 2 - game_over_text.get_width() // 2,
                180
            )
        )

        screen.blit(
            score_text,
            (
                WIDTH // 2 - score_text.get_width() // 2,
                250
            )
        )

        screen.blit(
            restart_text,
            (
                WIDTH // 2 - restart_text.get_width() // 2,
                320
            )
        )

        screen.blit(
            exit_text,
            (
                WIDTH // 2 - exit_text.get_width() // 2,
                380
            )
        )

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()