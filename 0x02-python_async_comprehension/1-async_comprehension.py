#!/usr/bin/env python3
'''task 1 module
'''
from typing import List
from random import randint

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[int]:
    '''creates a list of 10 numbers
    '''
    result = [value async for value in async_generator()]
    return result
