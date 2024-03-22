
class Rectangle:

    def __init__(self, point, longueur, hauteur):
        self.point = point
        self.longueur = longueur
        self.hauteur = hauteur

    def perimetre(self):
        return 2 * (self.longueur + self.hauteur)

    def surface(self):
        return self.longueur * self.hauteur

    def pointDansRectangle(self, point):
        return self.point.x <= point.x <= self.point.x + self.longueur and self.point.y <= point.y <= self.point.y + self.hauteur