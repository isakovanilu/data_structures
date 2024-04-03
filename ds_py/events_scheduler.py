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
        if len(self.events) < 0:
            print('There is no events')
            return
        for event in self.events:
            if event.name == name:
                self.events.remove(event)
                break
        else:
            print("Event not found.")
            
    def display_events(self):
        if len(self.events) < 0:
            print('There is no events')
            return
        for event in self.events: 
            print(event)
         
         
scheduler = Scheduler()
scheduler.add_event(Event("Meeting with nilu", "2023-02-22", "10:00 AM", "11:00 AM"))
scheduler.add_event(Event("Lunch with nilu", "2023-02-22", "12:00 PM", "1:00 PM"))
scheduler.display_events()
scheduler.remove_event("Meeting with nilu")
scheduler.display_events()        