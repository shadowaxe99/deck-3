```python
from src.utils.eye_tracking_utils import EyeTracking
from src.interactive_elements.eye_tracking import EyeTrackingElement

class Slide12:
    def __init__(self, user):
        self.user = user
        self.title = "Thank You for Your Time"
        self.subtitle = "Let's Build a Brighter Future Together: #ElysiumFuture"
        self.eye_tracking = EyeTracking()

    def display_slide(self):
        print(f"Title: {self.title}")
        print(f"Subtitle: {self.subtitle}")

    def display_interactive_element(self):
        eye_tracking_element = EyeTrackingElement(self.user)
        eye_tracking_element.activate()

    def run_slide(self):
        self.display_slide()
        self.display_interactive_element()

if __name__ == "__main__":
    user = {"name": "John Doe", "country": "USA"}
    slide = Slide12(user)
    slide.run_slide()
```