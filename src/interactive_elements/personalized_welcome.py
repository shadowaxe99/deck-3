```python
from datetime import datetime
from src.utils.time_utils import get_current_time

def personalized_welcome(user_name):
    current_time = get_current_time()
    welcome_message = f"Hello, {user_name}, it's {current_time}"
    return welcome_message
```