```python
from src.utils.video_utils import play_demo_video
from src.utils.time_utils import get_current_time

class Slide3:
    def __init__(self, user):
        self.title = "Your 24/7 Digital Butler"
        self.bullet_points = [
            "Smart Home Management: Control up to 20 devices",
            "Financial Portfolio Optimization: Increase ROI by 15%"
        ]
        self.user = user

    def display_slide(self):
        print(f"Title: {self.title}")
        for point in self.bullet_points:
            print(f"- {point}")

    def display_interactive_element(self):
        print(f"Hello, {self.user.name}, it's {get_current_time()}")
        play_demo_video("demo_video.mp4", 45)

if __name__ == "__main__":
    from src.User import User
    user = User("John Doe", "USA")
    slide = Slide3(user)
    slide.display_slide()
    slide.display_interactive_element()
```