import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"


class Vector:
    def __init__(self, start: Point, end: Point):
        self.x = end.x - start.x
        self.y = end.y - start.y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def add_vector(self, other):
        return Vector(Point(0, 0), Point(self.x + other.x, self.y + other.y))


# Ввод координат точек
print("Введите координаты 4 точек:")
x1, y1 = map(float, input("Точка A (x y): ").split())
x2, y2 = map(float, input("Точка B (x y): ").split())
x3, y3 = map(float, input("Точка C (x y): ").split())
x4, y4 = map(float, input("Точка D (x y): ").split())

# Создание объектов точек
A = Point(x1, y1)
B = Point(x2, y2)
C = Point(x3, y3)
D = Point(x4, y4)

# Создание векторов
V1 = Vector(A, B)
V2 = Vector(C, D)

# Сложение векторов
V3 = V1.add_vector(V2)

# Вывод результатов
print(f"Вектор AB: {V1}")
print(f"Вектор CD: {V2}")
print(f"Сумма векторов AB + CD: {V3}")
