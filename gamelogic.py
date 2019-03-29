import graphics

def cycle(screen, data):
    #determine if world map needs to be regenerated, if so, do it
    if data['world_changed']:
        world = data['world']
        data['world_screen'] = graphics.generate_world_screen(world)

    #regenerate unit map
    if data['units_changed']:
        units = data['units']
        data['units_screen'] = None#graphics.generate_units_screen(units)

    #blit them both on screen
    screen.blit(data['world_screen'], (0, 0), None)

    #other calculations for state


    return screen, data
