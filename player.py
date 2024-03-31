class Player():
    #runs when the player is created
    def __init__(self):
        self.dice = [[[1],[2],[3],[4],[5],[6]],[[1],[2],[3],[4],[5],[6]]]
        self.relics = []
        self.weapons = []
        self.health = 20 
        
    #runs every frame
    def update(self):
        pass