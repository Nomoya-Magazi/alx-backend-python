#!/usr/bin/env python3
'''task 0 module
'''
import asyncio
import random


async def async_generator():
    '''generates a sequence of 10 numbers
    '''
    for i in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
