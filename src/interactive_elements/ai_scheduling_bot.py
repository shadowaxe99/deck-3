```python
import datetime
from dateutil.relativedelta import relativedelta

class AISchedulingBot:
    def __init__(self, user):
        self.user = user
        self.meeting_slots = self.generate_meeting_slots()

    def generate_meeting_slots(self):
        current_date = datetime.datetime.now()
        meeting_slots = []
        for i in range(14):
            slot_date = current_date + relativedelta(days=i)
            for hour in range(9, 18):
                slot_time = datetime.time(hour=hour)
                slot_datetime = datetime.datetime.combine(slot_date, slot_time)
                meeting_slots.append(slot_datetime)
        return meeting_slots

    def schedule_meeting(self, requested_slot):
        if requested_slot in self.meeting_slots:
            self.meeting_slots.remove(requested_slot)
            return True
        else:
            return False

    def get_available_slots(self):
        return self.meeting_slots
```