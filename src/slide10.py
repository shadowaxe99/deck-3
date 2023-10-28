```python
from src.utils.hologram_utils import generate_hologram
from src.interactive_elements.ai_hologram import AIHologram

class Slide10:
    def __init__(self, user):
        self.user = user
        self.title = "Meet the Innovators"
        self.bullet_points = [
            "CEO - 20 years in AI",
            "CTO - 15 patents"
        ]
        self.holograms = [
            AIHologram("CEO", "20 years in AI", 30),
            AIHologram("CTO", "15 patents", 30)
        ]

    def display_slide(self):
        print(f"Title: {self.title}")
        for point in self.bullet_points:
            print(f"- {point}")

    def display_interactive_element(self):
        for hologram in self.holograms:
            hologram_data = generate_hologram(hologram)
            print(f"Displaying hologram for {hologram_data['name']}")

if __name__ == "__main__":
    slide = Slide10("John Doe")
    slide.display_slide()
    slide.display_interactive_element()
```