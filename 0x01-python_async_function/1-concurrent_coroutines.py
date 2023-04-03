#!/usr/bin/env python3

'''task 1 module
'''

wait_random = __import__('0-basic_async_syntax').wait_random

from typing import List
import asyncio


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''executes wait_random n times.
    '''
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    return sorted(results)

