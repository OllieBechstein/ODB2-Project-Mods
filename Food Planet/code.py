### The code for your custom game objects goes here.
class SwapMeatball(MapGenGuaranteePlanets):
    def __init__(self):
        MapGenGuaranteePlanets.__init__(self, [
        ("planet.meatball", 20, 30, ["planet.mining"]),
        ])