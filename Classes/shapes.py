import math
import turtle


# abstract class
# base class

class shapes():
    def draw(self): pass

    def get_sides(self): pass

    def area(self): pass

    def perimeter(self): pass

    def get_sides(self): pass

"""can be derived from the sections of a Cone"""
class conics(shapes):
    def parametric_form(self):
        pass

class ellipse(conics):
    
    def __init__(self, a=3,b = 2):
        self.property = "Can be derived from the sections of a Cone"
        self.__a = a
        self.__b = b

    def parametric_form(self):
        print("acos(x) + bsin(x)")

    def get_radius(self):
        return "Major -" + str(self.__a) + "Minor" + str(self.__b)

    def set_radius(self, a=3,b = 2):
        self.__a = a
        self.__b = b

    def area(self):
        return math.pi*self.__a*self.__b


# derived class
class triangle(shapes):
    def __init__(self, a=1, b=1, c=1):
        self.__a = a
        self.__b = b
        self.__c = c

    def get_sides(self):
        return self.__a, self.__b, self.__c

    def set_sides(self, a=1, b=1, c=1):  # POLYMORPHISM
        self.__a = a
        self.__b = b
        self.__c = c

    def perimeter(self):
        return self.__a + self.__b + self.__c

    def area(self):
        s = self.perimeter()/2
        return (s*(s-self.__a)*(s-self.__c)*(s-self.__b))**0.5

    def draw(self):
        turtle.clear()
        x, y = turtle.pos()
        turtle.forward(self.__a)
        rot = math.acos((self.__a**2 + self.__b**2 -
                         self.__c**2)/(2*self.__a*self.__b))
        rot = math.degrees(rot)
        print(rot)
        turtle.left(rot)
        turtle.forward(self.__b)
        turtle.setposition(x, y)

    def validate(self):
        if (self.perimeter() - max(self.get_sides())) <= max(self.get_sides()):
            print("Not a valid traingle with sides {0}".format(
                self.get_sides()))
        else:
            print("This is a valid traingle")


class rectangle(shapes):
    def __init__(self, x=2, y=1):
        self.x = x
        self.y = y

    def get_side(self):
        return self.x, self.y

    def set_side(self, x=2, y=1):
        self.x = x
        self.y = y

    def perimeter(self):
        return 2*(self.x + self.y)

    def area(self):
        return self.y*self.x

    def draw(self):
        turtle.clear()
        turtle.forward(self.x)
        turtle.left(90)
        turtle.forward(self.y)
        turtle.left(90)
        turtle.forward(self.x)
        turtle.left(90)
        turtle.forward(self.y)

# SQUARE INHERITED FROM RECTANGLE


class square(rectangle):
    def __init__(self, x=1):
        self.x = x

    def get_side(self):
        return self.x

    def set_side(self, x=1):  # POLYMORPHISM
        self.x = x

    def perimeter(self):
        return rectangle(self.x, self.x).perimeter()

    def area(self):
        return rectangle(self.x, self.x).area()

    def draw(self):
        rectangle(self.x, self.x).draw()


class circle(conics):
    def __init__(self, x=1):
        self.__r = x

    def parametric_form(self):
        print("rcos(x) + rsin(x)")

    def get_radius(self):
        return self.__r

    def set_radius(self, x=1):
        self.__r = x

    def circumference(self):
        return math.pi*self.__r*2

    def area(self):
        return math.pi*self.__r*self.__r

    def draw(self):
        turtle.clear()
        turtle.circle(self.__r)

# REQUIRE TO GIVE THE 2 DIAGONALS OF RHOMBUS TO DEFINE IT PROPERLY
# LATER THE SIDE CAN BE CALCULATED


class rhombus(square):
    def __init__(self, x=1, y=1):
        self.x = x
        self.y = y

    def get_side(self):
        return (self.x**2 + self.y**2)**(0.5)/2

    def set_diagonals(self, x=1, y=1):  # POLYMORPHISM
        self.x = x
        self.y = y

    def perimeter(self):
        return square(self.get_side()).perimeter()

    def area(self):
        return 0.5*self.x*self.y

    def draw(self):
        side = self.get_side()
        angle1 = math.acos(((side**2)*2 - self.x**2)/(2*side*side))
        angle1 = math.degrees(angle1)
        angle2 = (360 - 2*angle1)/2
        turtle.forward(side)
        turtle.right(angle1)
        turtle.forward(side)
        turtle.right(angle2)
        turtle.forward(side)
        turtle.right(angle1)
        turtle.forward(side)


class parallelogram(rectangle):
    def __init__(self, x=20, y=10):
        self.x = x
        self.y = y

    def get_side(self):
        return rectangle(self.x, self.y).get_side()

    def set_side(self, x=2, y=1):
        self.x = x
        self.y = y

    def perimeter(self):
        return rectangle(self.x, self.y).perimeter()

    def area(self):
        return rectangle(self.x, self.y).area()

    def draw(self):
        turtle.clear()
        turtle.forward(self.x)
        turtle.left(60)
        turtle.forward(self.y)
        turtle.left(120)
        turtle.forward(self.x)
        turtle.left(60)
        turtle.forward(self.y)
