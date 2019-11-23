import ui
import storage


def add_new_schedule(schedule):
    new_meeting = ui.get_input(['meeting title','duration in hours', 'start time'],'Schedule a new meeting')
    schedule.append(new_meeting)
    return schedule
