

import time

current = time.strftime('%H:%M')
print(current)
minute = current[-2:]
hour = current[:2]
print(minute)
print(hour)