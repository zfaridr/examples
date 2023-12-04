class A:
    x = 3
    y = 2

    def __init__(self, f):
        self.f = f

    def add(self, a, b):
        return a + b

    def multiply(self, c, d):
        return c * d

    @classmethod
    def divide(x, y) -> float:
        return x / y

    @classmethod
    def sub(cls):
        return cls(3)

instance = A(2)

multiply = classmethod(A.multiply)

print(instance.add(3, 4))
print(A.multiply(A, 2, 3))
print(A.multiply(A, A.x, A.y))
print(A.sub().__dict__)
