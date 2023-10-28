```python
from src.utils.ar_utils import displayARPopup
from src.interactive_elements.ar_popup import ARPopup

class Slide5:
    def __init__(self, user):
        self.title = "Security & User Control"
        self.bullets = [
            "Your Data, Your Control",
            "Blockchain Security: 256-bit encryption",
            "Decentralized Platform: 10,000 nodes"
        ]
        self.user = user
        self.ar_popup = ARPopup("Secure Vault", "256-bit Encryption")

    def display(self):
        print(f"Title: {self.title}")
        for bullet in self.bullets:
            print(f"- {bullet}")

    def display_interactive_element(self):
        displayARPopup(self.ar_popup)

    def run(self):
        self.display()
        self.display_interactive_element()
```