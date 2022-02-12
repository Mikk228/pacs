import time

final = True
open = False
points = 0

start_time = time.time()

while True:
    if time.time() - start_time > 5:
        open = True
        start_time = time.time()
    if points >= 2560:
        final = True
    if final == True:
        final = False
        # рестарт
