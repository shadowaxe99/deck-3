```python
from src.utils.animation_utils import displayInteractiveElement
from src.utils.time_utils import current_time

class Slide4:
    def __init__(self, user_name):
        self.title = "Connect, Collaborate, Control"
        self.bullet_points = ["Discover 200+ AI Capabilities", "User-Developer Bridge: Connect with 500+ developers"]
        self.interactive_element = "Clickable icons that show 5 mini-demos or infographics."
        self.user_name = user_name

    def displaySlide(self):
        print(f"Title: {self.title}")
        print("Bullet Points:")
        for point in self.bullet_points:
            print(f"- {point}")
        print(f"Interactive Element: {self.interactive_element}")

    def displayInteractiveElement(self):
        displayInteractiveElement(self.interactive_element)

    def welcomeMessage(self):
        print(f"Hello, {self.user_name}, it's {current_time()}")

if __name__ == "__main__":
    slide = Slide4("John Doe")
    slide.displaySlide()
    slide.displayInteractiveElement()
    slide.welcomeMessage()
```