def vibe_check(day_energy: int) -> str:
    if day_energy >= 80:
        return "wow"
    elif day_energy >= 50:
        return "meh"
    else:
        return "tilt"


# daily vibe
if __name__ == "__main__":
    energy = 73
    print(vibe_check(energy))