#!/usr/bin/python

from typing import Deque, Tuple

def state_verdict(
    long_tracking_history: Deque[bool],
    short_tracking_history: Deque[bool],
) -> Tuple[bool, bool, bool]:
    """Baba algorithm for robustly determining status changes of objects to be tracked.

    Parameters
    ----------
    long_tracking_history: List[bool]\n
        History of N cases. Each element represents the past N state judgment results.\n
        e.g. N=10, [False, True, False, True, True, True, True, True, True, False]\n
    short_tracking_history: List[bool]\n
        History of M cases. Each element represents the past M state judgment results.\n
        e.g. M=4, [True, True, False, True]

    Returns
    ----------
    state_interval_judgment: bool\n
        Whether the object's state is currently ongoing. True as long as the condition is ongoing. True or False\n
    state_start_judgment: bool\n
        Whether the object has just changed to that state. True only if it is determined that the state has changed. True or False\n
    state_end_judgment: bool\n
        Whether the state of the object has just ended or not. It becomes true only at the moment it is over. True or False
    """
    if not isinstance(long_tracking_history, Deque):
        raise TypeError('long_tracking_history is not Deque.')
    if not isinstance(short_tracking_history, Deque):
        raise TypeError('short_tracking_history is not Deque.')

    n: int = long_tracking_history.maxlen
    m: int = short_tracking_history.maxlen

    if n is None:
        raise ValueError('long_tracking_history.maxlen is None. Set long_tracking_history.maxlen to the maximum number of histories indicating N histories.')
    if m is None:
        raise ValueError('short_tracking_history.maxlen is None. Set long_tracking_history.maxlen to the maximum number of histories indicating N histories.')

    if len(long_tracking_history) < n:
        return False, False, False
    if len(short_tracking_history) < m:
        return False, False, False

    # 1. State-in-Progress (whether or not the state is currently in progress, true for as long as the state lasts)
    # The sum of N histories is greater than or equal to N/2 and the sum of the last M histories is greater than or equal to M-1
    state_interval_judgment: bool = sum(long_tracking_history) >= (n // 2) and sum(short_tracking_history) >= (m - 1)
    # 2. State start judgment (whether the state has now been entered or not, it becomes true only at the moment of change)
    # Total of N histories = N/2 and the sum of the last M histories is greater than or equal to M-1
    state_start_judgment: bool = sum(long_tracking_history) == (n // 2) and sum(short_tracking_history) >= (m - 1)
    # 3. State end judgment (whether the state has just ended or not, it becomes true only at the moment it ends)
    # Sum of N histories = N/2 and the sum of the last M histories is less than or equal to 1
    state_end_judgment: bool = sum(long_tracking_history) == (n // 2) and sum(short_tracking_history) <= 1

    return state_interval_judgment, state_start_judgment, state_end_judgment

if __name__ == '__main__':
    print(f'long_tracking_history = Deque([False, True, False, True, True, True, True, True, True, False], maxlen=10)')
    print(f'short_tracking_history = Deque([True, True, False, True], maxlen=4)')
    state_interval_judgment, state_start_judgment, state_end_judgment = \
        state_verdict(
            long_tracking_history=Deque([False, True, False, True, True, True, True, True, True, False], maxlen=10),
            short_tracking_history=Deque([True, True, False, True], maxlen=4),
        )
    print(f'state_interval_judgment: {state_interval_judgment}')
    print(f'state_start_judgment: {state_start_judgment}')
    print(f'state_end_judgment: {state_end_judgment}')
