```python
from src.utils.roadmap_utils import displayInteractiveRoadmap

class Slide8:
    def __init__(self, user):
        self.title = "A Compelling Vision for the Future"
        self.bullets = [
            "Our Vision for 2030: Reach 10 million users",
            "Seamless Integration of AI into Daily Life: 500+ services",
            "A People-Led AI Revolution: 2 million user-contributions"
        ]
        self.user = user

    def display(self):
        print(f"Title: {self.title}")
        for bullet in self.bullets:
            print(f"- {bullet}")

    def interactive_element(self):
        milestones = [
            "2024: 2 million users",
            "2025: 300+ services",
            "2026: 1 million user-contributions",
            "2027: 5 million users",
            "2030: 10 million users"
        ]
        displayInteractiveRoadmap(milestones)

def main(user):
    slide = Slide8(user)
    slide.display()
    slide.interactive_element()

if __name__ == "__main__":
    user = {"name": "John Doe", "country": "USA"}
    main(user)
```