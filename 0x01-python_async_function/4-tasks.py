#!/usr/bin/env python3
'''task 4 Module.
'''

from typing import List
import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''executes task_wait_random n times.
    '''
    tasks = [await(task_wait_random(max_delay)) for _ in range(n)]
    results = sorted(tasks)
    return (results)
