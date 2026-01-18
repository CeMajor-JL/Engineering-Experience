# core.py

class Toolkit:
    """Basic utility functions"""

    def clamp(self, value, min_value, max_value):
        """Clamp value between min_value and max_value"""
        return max(min_value, min(value, max_value))


if __name__ == "__main__":
    tools = Toolkit()
    print("Clamp 15 between 0 and 10:", tools.clamp(15, 0, 10))