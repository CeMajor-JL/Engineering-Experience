class Toolkit:
    def clamp(self, value, min_value, max_value):
        return max(min_value, min(value, max_value))

    def lerp(self, a, b, t):
        return a + (b - a) * t

    def swap(self, a, b):
        return b, a

    def factorial(self, n):
        if n <= 1:
            return 1
        return n * self.factorial(n - 1)

    def fibonacci(self, n):
        if n <= 1:
            return n
        return self.fibonacci(n - 1) + self.fibonacci(n - 2)


if __name__ == "__main__":
    tools = Toolkit()
    print("Clamp 15 between 0 and 10:", tools.clamp(15, 0, 10))
    print("Lerp from 0 to 100 at t=0.25:", tools.lerp(0, 100, 0.25))
    x, y = tools.swap(5, 10)
    print("Swap 5 and 10:", x, y)
    print("Factorial 5:", tools.factorial(5))
    print("Fibonacci 7:", tools.fibonacci(7))