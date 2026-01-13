def basic_stats(numbers):
    if not numbers:
        return None

    total = sum(numbers)
    count = len(numbers)
    average = total / count
    minimum = min(numbers)
    maximum = max(numbers)

    return {
        "count": count,
        "sum": total,
        "average": average,
        "min": minimum,
        "max": maximum
    }

if __name__ == "__main__":
    data = [4, 8, 15, 16, 23, 42]
    stats = basic_stats(data)

    for key, value in stats.items():
        print(f"{key}: {value}")