```python
import matplotlib.pyplot as plt

def displayInteractiveRoadmap(milestones):
    fig, ax = plt.subplots()

    # Create a list of colors for each milestone
    colors = ['b', 'g', 'r', 'c', 'm']

    for i, milestone in enumerate(milestones):
        ax.broken_barh([(milestone['start'], milestone['duration'])], (i*10, 9), facecolors=colors[i])

        # Add a text annotation for each milestone
        ax.text(milestone['start'] + milestone['duration']/2, i*10 + 5, milestone['name'],
                horizontalalignment='center', verticalalignment='center', fontsize=10, color='white')

    # Set the y-axis labels to be the milestone names
    ax.set_yticks([i*10 + 5 for i in range(len(milestones))])
    ax.set_yticklabels([milestone['name'] for milestone in milestones])

    ax.set_xlabel('Years')
    ax.set_title('Interactive Roadmap')

    plt.show()

milestones = [
    {'name': 'Milestone 1', 'start': 2023, 'duration': 2},
    {'name': 'Milestone 2', 'start': 2025, 'duration': 2},
    {'name': 'Milestone 3', 'start': 2027, 'duration': 2},
    {'name': 'Milestone 4', 'start': 2029, 'duration': 2},
    {'name': 'Milestone 5', 'start': 2031, 'duration': 2},
]

displayInteractiveRoadmap(milestones)
```