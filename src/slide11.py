```python
from src.utils.scheduling_utils import schedule_meeting
from src.interactive_elements.ai_scheduling_bot import AISchedulingBot

class Slide11:
    def __init__(self, user):
        self.title = "Ready to Join Us?"
        self.bullet_points = [
            "Schedule a Meeting: Availability for next 2 weeks",
            "Download Our Whitepaper: 30 pages of in-depth analysis"
        ]
        self.user = user
        self.ai_scheduling_bot = AISchedulingBot(user)

    def display_slide(self):
        print(self.title)
        for point in self.bullet_points:
            print(f"- {point}")

    def display_interactive_element(self):
        self.ai_scheduling_bot.display()

    def schedule_meeting(self):
        return schedule_meeting(self.user)

slide11 = Slide11(user)
slide11.display_slide()
slide11.display_interactive_element()
meeting_time = slide11.schedule_meeting()
print(f"Meeting scheduled at {meeting_time}")
```