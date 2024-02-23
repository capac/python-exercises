from math import hypot


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __radd__(self, other):
        return self.__add__(other)

    def __str__(self):
        return "Vector({:s}, {:s})".format(str(self.x), str(self.y))

    def prod(self, other):
        return self.x * other.x + self.y * other.y

    def __mul__(self, scalar):
        x = scalar * self.x
        y = scalar * self.y
        return Vector(x, y)

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))


if __name__ == "__main__":
    vec1 = Vector(4, 3)
    vec2 = Vector(2, 6)
    vec3 = Vector(0, 0)
    print("vec1 =", vec1)
    print("vec2 =", vec2)
    print("vec1 + vec2 =", vec1 + vec2)
    print("vec2 + vec1 =", vec2 + vec1)
    print("vec1.prod(vec2) =", vec1.prod(vec2))
    print("vec2.prod(vec1) =", vec2.prod(vec1))
    print("9*vec1 =", 9 * vec1)
    print("vec1*9 =", vec1 * 9)
    print("abs(vec1) =", abs(vec1))
    print("Is abs(vec2) > 0 ?", bool(vec2))
    print("Is abs(vec3) > 0 ?", bool(vec3))
