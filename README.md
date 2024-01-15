# bbalg
[![Downloads](https://static.pepy.tech/personalized-badge/bbalg?period=total&units=none&left_color=grey&right_color=brightgreen&left_text=Downloads)](https://pepy.tech/project/bbalg) ![GitHub](https://img.shields.io/github/license/PINTO0309/bbalg?color=2BAF2B) [![Python](https://img.shields.io/badge/Python-3.10-2BAF2B)](https://img.shields.io/badge/Python-3.8-2BAF2B) [![PyPI](https://img.shields.io/pypi/v/bbalg?color=2BAF2B)](https://pypi.org/project/bbalg/)

Baba algorithm for robustly determining status changes of objects to be tracked.

```
pip install -U bbalg
```

```python
state_verdict(
  long_tracking_history: Deque[bool],
  short_tracking_history: Deque[bool]
) -> Tuple[bool, bool, bool]

    Baba algorithm for robustly determining status changes of objects to be tracked.
    
    Parameters
    ----------
    long_tracking_history: List[bool]
        History of N cases. Each element represents the past N state judgment results.
        e.g. N=10, [False, False, False, True, False, True, True, True, False, True]
    
    short_tracking_history: List[bool]
        History of M cases. Each element represents the past M state judgment results.
        e.g. M=4, [True, True, False, True]
    
    Returns
    ----------
    state_interval_judgment: bool
        Whether the object's state is currently ongoing.
        True as long as the condition is ongoing.
        True or False
    
    state_start_judgment: bool
        Whether the object has just changed to that state.
        True only if it is determined that the state has changed.
        True or False

    state_end_judgment: bool
        Whether the state of the object has just ended or not.
        It becomes true only at the moment it is over.
        True or False
```
### 1. State-in-Progress (whether or not the state is currently in progress, true for as long as the state lasts)

The sum of `N` histories is greater than or equal to `N/2` and the sum of the last `M` histories is greater than or equal to `M-1`

```python
from typing import Deque
from bbalg import state_verdict

state_interval_judgment, state_start_judgment, state_end_judgment = \
    state_verdict(
        long_tracking_history=\
          Deque([False, True, False, True, False, True, True, True, True, False], maxlen=10),
        short_tracking_history=\
          Deque([True, True, True, False], maxlen=4),
    )
print(f'state_interval_judgment: {state_interval_judgment}')
print(f'state_start_judgment: {state_start_judgment}')
print(f'state_end_judgment: {state_end_judgment}')
```
```
state_interval_judgment: True
state_start_judgment: False
state_end_judgment: False
```
### 2. State start judgment (whether the state has now been entered or not, it becomes true only at the moment of change)

Total of `N` histories = `N/2` and the sum of the last `M` histories is greater than or equal to `M-1`

```python
from typing import Deque
from bbalg import state_verdict

state_interval_judgment, state_start_judgment, state_end_judgment = \
    state_verdict(
        long_tracking_history=\
          Deque([False, False, False, True, False, True, True, True, False, True], maxlen=10),
        short_tracking_history=\
          Deque([True, True, False, True], maxlen=4),
    )
print(f'state_interval_judgment: {state_interval_judgment}')
print(f'state_start_judgment: {state_start_judgment}')
print(f'state_end_judgment: {state_end_judgment}')
```
```
state_interval_judgment: True
state_start_judgment: True
state_end_judgment: False
```
### 3. State end judgment (whether the state has just ended or not, it becomes true only at the moment it ends)

Sum of `N` histories = `N/2` and the sum of the last `M` histories is less than or equal to `1`

```python
from typing import Deque
from bbalg import state_verdict

state_interval_judgment, state_start_judgment, state_end_judgment = \
    state_verdict(
        long_tracking_history=\
          Deque([True, True, False, True, False, True, False, False, True, False], maxlen=10),
        short_tracking_history=\
          Deque([False, False, True, False], maxlen=4),
    )
print(f'state_interval_judgment: {state_interval_judgment}')
print(f'state_start_judgment: {state_start_judgment}')
print(f'state_end_judgment: {state_end_judgment}')
```
```
state_interval_judgment: False
state_start_judgment: False
state_end_judgment: True
```
