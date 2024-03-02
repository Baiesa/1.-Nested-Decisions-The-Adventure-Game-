'''
5. The Silent Logger: System Monitor 🖥️

Objective:

To practice the use of the pass statement in a system monitoring context.

Task 1: Code Correction

You are provided with a Python script that is supposed to monitor system parameters,
 but it has some mistakes. Identify and fix them.

Buggy Code:

'''

import random

cpu_usage = random.randint(0, 100)
if cpu_usage > 90:
    print("High CPU usage!")
elif 80 <  cpu_usage < 90:
    pass
