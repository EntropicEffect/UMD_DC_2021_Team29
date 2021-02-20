class MapNode():
    def __init__(self, latitude, longitude):
        self.lat = float(latitude)
        self.long = float(longitude)
    
    # You can now do print(node) instead of node.print()
    def __repr__(self):
        return f'({self.lat}, {self.long})'