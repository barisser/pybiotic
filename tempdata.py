import worldlogic
import graphics

def init():
    world = worldlogic.init()
    data = {}
    data['world'] = world
    data['units'] = []
    data['world_screen'] = graphics.regenerate_world_screen(world)
    data['units_screen'] = None#graphics.generate_units_screen(data['units'])
    data['world_changed'] = False
    data['units_changed'] = True


    return data
