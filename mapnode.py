class MapNode():
    def __init__(self, lattitude, longitude):
        self.lat = str(lattitude)
        self.long = str(longitude)
    
    # You can now do print(node) instead of node.print()
    def __repr__(self):
        return f'({self.lat}, {self.long})'