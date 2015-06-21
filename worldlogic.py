
worldx = 200
worldy = 200

class World:
    def __init__(self):
        self.worldx = worldx
        self.worldy = worldy
        self.map = []
        for i in range(0, self.worldx):
            r = []
            for a in range(0, self.worldy):
                new_spot = Spot(i, a)
                r.append(new_spot)
            self.map.append(r)




class Spot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = 0


def init(): #supply a world
    return World()
