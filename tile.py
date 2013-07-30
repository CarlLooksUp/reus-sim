class Tile
    """A single space in the game world. 

       World consists of a ring linked list. Relevant neighbors can be 2 away"""

    def ___init___():
        self.terrain = "" #Can be WASTELAND, WET_WASTELAND, FOREST, SWAMP, DESERT, MOUNTAIN, OCEAN (or TOWN)
        self.town = "" #important for project bonuses
        self.source = "" #This will be a long list
        
        #store values
        self.food = 0
        self.tech = 0
        self.wealth = 0
        self.danger = 0
        self.awe = 0
        self.natura = 0

        #proximity info
        self.left = ""
        self.right = ""

     
        
