
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        if width < 0:
            raise ValueError("La largeur ne peut pas être négative")
        self.width = width

    def set_height(self, height):
        if height < 0:
            raise ValueError("La hauteur ne peut pas être négative")
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Trop grand pour faire une image"
        return "".join(["* " * self.width + "\n" for _ in range(self.height)])

    def get_amount_inside(self, shape):
        return self.get_area() // shape.get_area()

class Carree(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __str__(self):
        return f"Carree(side={self.width})"

    def set_side(self, side):
        self.set_height(side)
        self.set_width(side)


