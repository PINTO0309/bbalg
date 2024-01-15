# bbalg
Baba algorithm for robustly determining status changes of objects to be tracked.

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
        e.g. N=10, [False, True, False, True, True, True, True, True, True, False]
    
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

```python
from typing import Deque
from bbalg import state_verdict

state_interval_judgment, state_start_judgment, state_end_judgment = \
    state_verdict(
        long_tracking_history=Deque([False, True, False, True, True, True, True, True, True, False], maxlen=10),
        short_tracking_history=Deque([True, True, False, True], maxlen=4),
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
