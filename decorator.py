"""Decorator utilities for rate limiting and function behavior modification.
Copyright (C) 2024  SOMYA SARATHI SAMAL

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import time
from functools import wraps
from collections import deque

def rate_limit(calls: int, period: int):
    """
    A decorator to limit the number of function calls within a given time period.

    Args:
        calls (int): Maximum number of calls allowed.
        period (int): Time period in seconds for the rate limit.

    Returns:
        function: A wrapped function with rate limiting.
    """
    def decorator(func):
        call_times = deque()

        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal call_times
            current_time = time.time()
            
            # Remove calls older than the allowed period
            while call_times and current_time - call_times[0] > period:
                call_times.popleft()
            
            # Check if the limit is exceeded
            if len(call_times) >= calls:
                raise RuntimeError("Rate limit exceeded. Please wait before retrying.")
            
            # Add the current call time and execute the function
            call_times.append(current_time)
            return func(*args, **kwargs)
        
        return wrapper
    return decorator
