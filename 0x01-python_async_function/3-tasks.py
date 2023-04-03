#!/usr/bin/env pyhton3
'''task 3 module.
'''

wait_random = __import__('0-basic_async_syntax').wait_random


import asyncio


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''creates an asynchronous task for wait_random
    '''
    return asyncio.create_task(wait_random(max_delay))
