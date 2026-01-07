def vibe_meter(energy):
    level = 0

    while energy > 0:
        print(f"Vibe level {level} | Energy left: {energy}")
        energy -= 1
        level += 1

    return "Energy depleted. Sleep arc unlocked."

# test run
result = vibe_meter(5)
print(result)