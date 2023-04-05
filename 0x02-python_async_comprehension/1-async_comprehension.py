#!/usr/bin/env python3
'''task 1 module
'''
from typing import List
from importlib import import_module as using


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''creates a list of 10 numbers
    '''
    result = [value async for value in async_generator()]
    return result
