from triangle import Triangle_rectangle
from rectangle import Rectangle
from cercle import Cercle
from point import Point


def main():
    p1 = Point(1, 1)
    p2 = Point(2, 2)
    p3 = Point(3, 3)
    p4 = Point(4, 4)
    c1 = Cercle(2, p1)
    c2 = Cercle(5, p2)
    r1 = Rectangle(p2, 3, 2)
    t1 = Triangle_rectangle(3, 4, p4)

    print(f"Distance entre p1 et p2: {p1.distancePoint(p2)}")
    print(f"Distance entre p1 et p3: {p1.distancePoint(p3)}")
    print(f"Distance entre p2 et p3: {p2.distancePoint(p3)}")
    print(f"Distance entre c1 et c2: {c1.point.distancePoint(c2.point)}")

    print(f"Perimetre de r1: {r1.perimetre()}")
    print(f"Surface de r1: {r1.surface()}")
    print(f"Point p1 dans r1: {r1.pointDansRectangle(p1)}")
    print(f"Point p2 dans r1: {r1.pointDansRectangle(p2)}")
    print(f"Point p3 dans r1: {r1.pointDansRectangle(p3)}")

    print(f"Diametre de c1: {c1.diametre()}")
    print(f"Perimetre de c1: {c1.perimetre()}")
    print(f"Surface de c1: {c1.surface()}")
    print(f"Collision entre c1 et c2: {c1.colision(c2)}")
    print(f"Point p1 dans c1: {c1.pointDansCercle(p1)}")
    print(f"Point p2 dans c1: {c1.pointDansCercle(p2)}")
    print(f"Point p3 dans c1: {c1.pointDansCercle(p3)}")

    print(f"Diametre de c2: {c2.diametre()}")
    print(f"Perimetre de c2: {c2.perimetre()}")
    print(f"Surface de c2: {c2.surface()}")
    print(f"Collision entre c2 et c1: {c2.colision(c1)}")
    print(f"Point p1 dans c2: {c2.pointDansCercle(p1)}")
    print(f"Point p2 dans c2: {c2.pointDansCercle(p2)}")
    print(f"Point p3 dans c2: {c2.pointDansCercle(p3)}")

    print(f"Perimetre de t1: {t1.perimetre()}")
    print(f"Surface de t1: {t1.surface()}")
    print(f"Point p1 dans t1: {t1.pointDansTriangle(p1)}")
    print(f"Point p2 dans t1: {t1.pointDansTriangle(p2)}")
    print(f"Point p3 dans t1: {t1.pointDansTriangle(p3)}")


if __name__ == "__main__":
    main()