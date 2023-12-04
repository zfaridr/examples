


class Colour:
    red = 0
    green = 0
    blue = 0

    def __init__(self, r, g, b):
        self.red = r
        self.green = g
        self.blue = b

    def toHex(self):
        return '#%02x%02x%02x' % (self.red, self.green, self.blue)
    
class ColourAlpha(Colour):
    alpha = 1

    def __init__(self, r, g, b, a):
        self.red = r
        self.green = g
        self.blue = b
        self.alpha = a

gray = Colour(80, 80, 80)

red = ColourAlpha(255, 0, 0, 0.5)
