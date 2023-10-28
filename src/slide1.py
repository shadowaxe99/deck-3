```python
from src.utils.animation_utils import create_3d_animation
from src.utils.time_utils import get_current_date

class Slide1:
    def __init__(self, user):
        self.title = "Elysium Innovations"
        self.subtitle = "Revolutionizing AI with a User-First Approach"
        self.date = get_current_date()
        self.user = user

    def display_slide(self):
        print(f"Title: {self.title}")
        print(f"Subtitle: {self.subtitle}")
        print(f"Date: {self.date}")

    def display_interactive_element(self):
        create_3d_animation("Elysium Innovations logo", 50)

    def run_slide(self):
        self.display_slide()
        self.display_interactive_element()
```