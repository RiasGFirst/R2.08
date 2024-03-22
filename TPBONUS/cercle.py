class Cercle:
    def __init__(self, rayon, point):
        self.rayon = rayon
        self.point = point

    def diametre(self):
        return 2 * self.rayon

    def perimetre(self):
        return 2 * 3.14 * self.rayon

    def surface(self):
        return 3.14 * self.rayon**2

    def colision(self, cercle):
        return self.point.distancePoint(cercle.point) <= self.rayon + cercle.rayon

    def pointDansCercle(self, point):
        return self.point.distancePoint(point) <= self.rayon
