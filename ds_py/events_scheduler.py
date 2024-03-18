"""
Event Scheduler: Implement an Event class 
with attributes for event details and a 
Scheduler class to manage and organize events by date.

"""

class Event:
    def __init__(self, name, date, description):
        self.name = name
        self.date = date
        self.description = description