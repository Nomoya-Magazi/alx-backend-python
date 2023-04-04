#!/usr/bin/env python3
'''task 2 module
'''

import asyncio
from typing import List
from time import perf_counter

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''executes async_comprehension 4 times
    and measures the total time executed
    '''
    start_time = perf_counter()
    await asyncio.gather(

            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension()
    )
    end_time = perf_counter()
    return end_time - start_time
