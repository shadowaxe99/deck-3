```python
from src.utils.time_utils import get_current_time
from src.interactive_elements.personalized_welcome import generate_welcome_message

class Slide2:
    def __init__(self, user):
        self.title = "Elysium Innovations"
        self.subtitle = "Revolutionizing AI with a User-First Approach"
        self.date = "October 2023"
        self.user = user

    def display_slide(self):
        print(f"Title: {self.title}")
        print(f"Subtitle: {self.subtitle}")
        print(f"Date: {self.date}")

    def display_interactive_element(self):
        current_time = get_current_time()
        welcome_message = generate_welcome_message(self.user, current_time)
        print(welcome_message)
```