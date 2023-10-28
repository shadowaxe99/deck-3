```python
import json

def load_roadmap_data():
    with open('data/roadmap.json', 'r') as file:
        data = json.load(file)
    return data

def get_milestone(milestone_id):
    data = load_roadmap_data()
    for milestone in data['milestones']:
        if milestone['id'] == milestone_id:
            return milestone
    return None

def display_milestone(milestone_id):
    milestone = get_milestone(milestone_id)
    if milestone:
        print(f"Milestone: {milestone['title']}")
        print(f"Description: {milestone['description']}")
        print(f"Estimated Completion: {milestone['estimated_completion']}")
    else:
        print("Milestone not found.")

def display_roadmap():
    data = load_roadmap_data()
    for milestone in data['milestones']:
        print(f"Milestone: {milestone['title']}")
        print(f"Description: {milestone['description']}")
        print(f"Estimated Completion: {milestone['estimated_completion']}")
        print("\n")
```