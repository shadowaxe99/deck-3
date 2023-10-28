```python
from src.slide1 import Slide1
from src.slide2 import Slide2
from src.slide3 import Slide3
from src.slide4 import Slide4
from src.slide5 import Slide5
from src.slide6 import Slide6
from src.slide7 import Slide7
from src.slide8 import Slide8
from src.slide9 import Slide9
from src.slide10 import Slide10
from src.slide11 import Slide11
from src.slide12 import Slide12

class Main:
    def __init__(self, user_name, user_country):
        self.user_name = user_name
        self.user_country = user_country
        self.current_time = None

    def update_time(self):
        from src.utils.time_utils import get_current_time
        self.current_time = get_current_time()

    def display_pitch_deck(self):
        self.update_time()

        Slide1(self.user_name, self.current_time).display()
        Slide2(self.user_name, self.current_time).display()
        Slide3(self.user_name, self.current_time).display()
        Slide4(self.user_name, self.current_time).display()
        Slide5(self.user_name, self.current_time).display()
        Slide6(self.user_name, self.current_time).display()
        Slide7(self.user_name, self.current_time).display()
        Slide8(self.user_name, self.current_time).display()
        Slide9(self.user_name, self.current_time).display()
        Slide10(self.user_name, self.current_time).display()
        Slide11(self.user_name, self.current_time).display()
        Slide12(self.user_name, self.current_time).display()

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    user_country = input("Enter your country: ")
    Main(user_name, user_country).display_pitch_deck()
```