```python
from src.utils.chart_utils import generate_3d_pie_chart
from src.interactive_elements.interactive_budget_chart import InteractiveBudgetChart

class Slide9:
    def __init__(self, user):
        self.title = "Be a Part of the Revolution"
        self.bullet_points = [
            "Investment Opportunities: $50M in Series A",
            "Strategic Partnerships: 20+ industry leaders"
        ]
        self.user = user
        self.interactive_element = InteractiveBudgetChart()

    def display_slide(self):
        print(f"Title: {self.title}")
        for point in self.bullet_points:
            print(f"- {point}")

    def display_interactive_element(self):
        investment_data = {
            "Series A": 50,
            "Strategic Partnerships": 20
        }
        chart = generate_3d_pie_chart(investment_data)
        self.interactive_element.display(chart)

    def interact(self):
        self.display_slide()
        self.display_interactive_element()
```