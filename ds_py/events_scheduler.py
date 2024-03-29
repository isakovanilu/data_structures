"""
Event Scheduler: Implement an Event class 
with attributes for event details and a 
Scheduler class to manage and organize events by date.

"""

class Event:
    def __init__(self, name, date, start_time, end_time):
        self.name = name
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        
    def __str__(self):
        return f"{self.name} on {self.date} from {self.start_time} to {self.end_time}"
       
class Scheduler:
    def __init__(self):
        self.events = []
        
    def add_event(self, event):
        self.events.append(event)
        self.events.sort(key=lambda x: x.date)
    
    def remove_event(self, name):
        for event in self.events:
            if event.name == name:
                self.events.remove(event)
                break
        else:
            print("Event not found.")
         