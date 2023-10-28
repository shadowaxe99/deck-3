```python
import hologram_utils

class AIHologram:
    def __init__(self, team_members):
        self.team_members = team_members

    def generate_hologram(self, member):
        hologram = hologram_utils.create_hologram(member['image'])
        return hologram

    def play_elevator_pitch(self, member):
        hologram_utils.play_audio(member['audio'])

    def display_holograms(self):
        for member in self.team_members:
            hologram = self.generate_hologram(member)
            hologram_utils.display_hologram(hologram)
            self.play_elevator_pitch(member)
```