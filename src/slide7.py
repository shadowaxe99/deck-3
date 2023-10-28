```python
from src.utils.voice_utils import activate_voice_command
from src.interactive_elements.voice_activated_testimonials import VoiceActivatedTestimonials

class Slide7:
    def __init__(self, user):
        self.title = "AI for Everyone, Everywhere"
        self.bullets = [
            "Affordable: Plans start at $9.99/month",
            "Accessible: Available in 50 countries"
        ]
        self.user = user
        self.interactive_element = VoiceActivatedTestimonials(user)

    def display_slide(self):
        print(f"Title: {self.title}")
        for bullet in self.bullets:
            print(f"- {bullet}")
        self.display_interactive_element()

    def display_interactive_element(self):
        print("Say 'Tell me more' to activate 3 reviews.")
        command = input("Your command: ")
        if command.lower() == "tell me more":
            self.interactive_element.activate_testimonials()
        else:
            print("Invalid command. Please say 'Tell me more'.")

if __name__ == "__main__":
    user = {"name": "John Doe", "country": "USA"}
    slide = Slide7(user)
    slide.display_slide()
```