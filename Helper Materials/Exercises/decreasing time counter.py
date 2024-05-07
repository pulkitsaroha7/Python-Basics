import time

seconds = 20  # Starting number of seconds

while seconds > 0:
    print(seconds)
    time.sleep(1)  # Wait for 1 second
    seconds -= 1  # Decrease the number of seconds by 1

print("Time's up!")
