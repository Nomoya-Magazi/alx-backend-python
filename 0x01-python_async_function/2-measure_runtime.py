#!/usr/bin/env python3
'''task 2 module
'''

wait_n = __import__('1-concurrent_coroutines').wait_n

import time

def measure_time(n: int, max_delay: int) -> float:
    '''gives the avarage runtime of wait_n
    '''
    start_time = time.time()
    wait_n(n, max_delay)
    total_time = time.time() - start_time
    return total_time / n
