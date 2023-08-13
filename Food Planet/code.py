### The code for your custom game objects goes here.
class ChangeMapGen(MapGenGuaranteePlanets):
    def __init__(self):
        MapGenGuaranteePlanets.__init__(self, [
        ("planet.meatball", 100, 100, ["planet.mining"]),
        ])