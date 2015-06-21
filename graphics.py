import pygame

tilex = 32
tiley = 32

def regenerate_world_screen(world):
    width = world.worldx * tilex
    height = world.worldy * tiley
    a = new_surface(width, height)
    render_color(a, 1,1,0,0, (255,255,255))
    return a

#def generate_units_screen(units):

def render_unit(unit, units_screen):
    x = unit.x * tilex
    y = unit.y * tiley
    units_screen.blit(unit.surface, 

def render_color(screen, x, y, width, height, color):
    r = pygame.Rect(x, y, width, height)
    if width==0:
      r=None
    elif height==0:
      r=None
    screen.fill(color, r)

def new_surface(x, y):
    return pygame.Surface((x, y))
