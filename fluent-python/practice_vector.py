#! /usr/bin/env python

import numpy as np


class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Vector({str(self.x)}, {str(self.y)})'

    def __repr__(self):
        return f'{Vector.__name__}({self.x!r}, {self.y!r})'

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __abs__(self):
        return np.sqrt(self.x**2 + self.y**2)

    def __bool__(self):
        return bool(abs(self))

    def __mul__(self, const):
        return Vector(const * self.x, const * self.y)


if __name__ == "__main__":
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    print(f'v1: {v1}')
    print(f'repr(v1): {repr(v1)}')
    print(f'v2: {v2}')
    print(f'v1 + v2: {v1 + v2}')
    w1 = v1 + v2
    v3 = Vector(5, 6)
    print(f'v3: {v3}')
    w2 = w1 + v3
    print(f'w2: {w2}')
    print(f'abs(w2): {abs(w2)}')
    print(f'w2 * 9: {w2 * 9}')
    v4 = Vector()
    print(f'bool(v4): {bool(v4)}')
    print(f'bool(w2): {bool(w2)}')
