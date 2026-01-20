class Toolkit:
    """Basic utility functions"""

    def clamp(self, value, min_value, max_value):
        return max(min_value, min(value, max_value))

    def lerp(self, a, b, t):
        """Linear interpolation between a and b with t (0-1)"""
        return a + (b - a) * t


if __name__ == "__main__":
    tools = Toolkit()
    print("Clamp 15 between 0 and 10:", tools.clamp(15, 0, 10))
    print("Lerp from 0 to 100 at t=0.25:", tools.lerp(0, 100, 0.25))