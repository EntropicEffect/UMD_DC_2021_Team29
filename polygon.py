from edge import Edge

class Polygon:
    def __init__(self, points):
        self.points = points
        self.edges = []
        for i in range(len(points) - 1):
            self.edges.append(Edge(points[i], points[i + 1]))
        self.edges.append(Edge(points[-1], points[0]))

    @staticmethod
    def is_within_threshold(x,y, threshold=10**-4):
        return abs(x - y) < threshold

    def intersect_edge(self, e, p):
        x1 = e.p0.x
        y1 = e.p0.y
        x2 = e.p1.x
        y2 = e.p1.y
        xp = p.x
        yp = p.y

        # Case 1: point is to the left of the edge
        if x1 < xp and x2 < xp:
            return 0
        # Case 2: half-line goes through the edge completely (horizontal edge)
        if self.is_within_threshold(y1, y2):
            xmin = min(x1, x2)
            xmax = max(x1, x2)
            if xmin <= xp and xp <= xmax and self.is_within_threshold(yp, y1):
                return 2
            else:
                return 0
        # Case 3: point is on the edge
        x = ((yp - y1) / (y2 - y1)) * (x2 - x1) + x1
        ymin = min(y1, y2)
        ymax = max(y1, y2)
        if self.is_within_threshold(x, xp) and (ymin <= yp and yp <= ymax):
            return 2
        # Case 4a: half-line intersects with edge's first endpoint
        if xp < x1 and self.is_within_threshold(yp, y1):
            if y1 < y2:
                return 1
            else:
                return 0
        # Case 4b: half-line intersects with edge's second endpoint
        if xp < x2 and self.is_within_threshold(yp, y2):
            if y2 < y1:
                return 1
            else:
                return 0
        # Case 5: half-line passes through edge
        if x > xp and (ymin < yp and yp < ymax):
            return 1
        else:
            return 0

    def point_inside(self, point):
        k = 0
        for edge in self.edges:
            m = self.intersect_edge(edge, point)
            if m == 2:
                return 2
            else:
                k += m
        return k % 2