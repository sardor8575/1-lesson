import pygame
import random
import sys

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("catch game")

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

player_width = 100
player_height = 20
player_x = (screen_width - player_width) // 2
player_y = screen_height - player_height
player_speed = 15

object_width = 30
object_height = 30
object_speeed = 10


def create_object():
    object_x = random.randint(0, screen_width - object_width)
    object_y = 0
    return {"x": object_x, "y": object_y}


def game_loop():
    global player_x
    objects = []
    score = 0

    clock = pygame.time.Clock()

    while True:
        screen.fill(white)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed

        if player_x < 0:
            player_x = 0
        elif player_x > screen_width - player_width:
            player_x = screen_width - player_width

        if len(objects) < 5:
            objects.append(create_object())

        for obj in objects:
            obj["y"] += object_speeed
            pygame.draw.rect(screen, red, (obj["x"], obj["y"], object_width, object_height))

            if obj["y"] + object_height >= player_y and player_x <= obj["x"] <= player_x + player_width:
                score += 1
                objects.remove(obj)

        pygame.draw.rect(screen, black, (player_x, player_y, player_width, player_height))

        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, black)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(30)

game_loop()




