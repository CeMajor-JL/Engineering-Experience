studied = input("Did you study today? (yes/no): ") == "yes"
worked_out = input("Did you work out today? (yes/no): ") == "yes"
productive = studied and worked_out
lazy_day = not productive
print("productive", productive)
print("lazy_day:", lazy_day)