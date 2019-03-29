import pygame
import gamelogic
import io
import tempdata
import worldlogic
import graphics
import image_loader

screen_width = 1200
screen_height = 800
frame_rate = 50


def init():
    pygame.init()
    image_loader.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    return screen


def main_loop():
    clock = pygame.time.Clock()
    screen = init()
    done = False

    data = tempdata.init()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            else:
                pressed = pygame.key.get_pressed()
            #    tempdata = io.respond_to_inputs(event, pressed, tempdata)

        screen.fill((0, 0, 0))
        screen, data = gamelogic.cycle(screen, data)

        pygame.display.flip()
        clock.tick(frame_rate)

if __name__ == '__main__':
    main_loop()
