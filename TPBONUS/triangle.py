from point import Point

class Triangle_rectangle:

        def __init__(self, cote1, cote2, point):
            self.cote1 = cote1
            self.cote2 = cote2
            self.point = point

        def perimetre(self):
            return self.cote1 + self.cote2 + self.point.distancePoint(Point())

        def surface(self):
            return (self.cote1 * self.cote2) / 2

        def pointDansTriangle(self, point):
            if point.x <= self.point.x and point.y <= self.point.y:
                return True
            return False