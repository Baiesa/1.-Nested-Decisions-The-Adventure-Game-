'''
Task 3: Alert System

If any of the system parameters exceed a certain threshold, print an alert message.
 However, if the system parameter is within a "gray zone",
use the pass statement to silently log this without alerting the user.

'''
import random

cpu_usage = random.randint(0, 100)
memory_usage = random.randint(0, 100)
disk_space = random.randint(0, 100)

if cpu_usage > 90:
    print("High CPU usage!")
elif 80 < cpu_usage < 90:
    pass

if memory_usage > 90:
    print("High memory usage!")
elif 80 < memory_usage < 90:
    pass

if disk_space > 90:
    print("Low disk space!")
elif 80 < disk_space < 90:
    pass