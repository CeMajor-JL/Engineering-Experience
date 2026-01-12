class RollingAverage:
    def __init__(self, size: int):
        self.size = size
        self.values = []

    def add(self, value: float) -> float:
        self.values.append(value)
        if len(self.values) > self.size:
            self.values.pop(0)
        return sum(self.values) / len(self.values)


if __name__ == "__main__":
    avg = RollingAverage(5)

    data = [10, 20, 30, 40, 50, 60]
    for v in data:
        print(f"Added {v}, average = {avg.add(v):.2f}")