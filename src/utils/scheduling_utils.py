```python
import datetime
from dateutil.relativedelta import relativedelta

def get_next_two_weeks_dates():
    today = datetime.date.today()
    two_weeks_later = today + relativedelta(weeks=2)
    date_range = [today + datetime.timedelta(days=x) for x in range((two_weeks_later-today).days + 1)]
    return date_range

def schedule_meeting(user_name, meeting_date):
    if meeting_date not in get_next_two_weeks_dates():
        return f"Sorry {user_name}, the selected date is not within the next two weeks. Please choose another date."
    else:
        # Assuming a database or some storage to save the scheduled meetings
        # save_meeting_to_db(user_name, meeting_date)
        return f"Meeting scheduled successfully for {user_name} on {meeting_date}."
```