class Edge:
    def __init__(self, p0, p1):
        self.p0 = p0
        self.p1 = p1
    def __repr__(self):
        return f'[{self.p0}, {self.p1}]'