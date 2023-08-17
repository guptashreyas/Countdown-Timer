import time


def countdown_timer(sec):
    while sec > 0:
        print(f"Time remaining: {sec} seconds")
        time.sleep(1)
        sec -= 1
    print("Time's up!")


# Get the input from the user
try:
    sec = int(input("Enter the number of seconds to countdown: "))
    countdown_timer(sec)
except ValueError:
    print("Invalid input. Please enter a valid number of seconds.")
