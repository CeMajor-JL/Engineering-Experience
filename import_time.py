import time

def focus_timer(minutes: int):
    seconds = minutes * 60
    print(f" Focus started for {minutes} minutes")

    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        print(f"\r {mins:02d}:{secs:02d}", end="")
        time.sleep(1)
        seconds -= 1

    print("\n Focus session complete. Take a break.")

if __name__ == "__main__":
    try:
        mins = int(input("Enter focus time (minutes): "))
        focus_timer(mins)
    except ValueError:
        print(" Please enter a valid number")