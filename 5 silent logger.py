'''

Task 2: System Check

Based on the corrected code from Task 1,

enhance the program to also monitor memory usage and disk space, and provide alerts accordingly.
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