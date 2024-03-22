class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distanceCoord(self, x, y):
        return ((self.x - x)**2 + (self.y - y)**2)**0.5

    def distancePoint(self, point):
        return self.distanceCoord(point.x, point.y)