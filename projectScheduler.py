class Activity:

    def __init__(self, duration, name):
        self.name = name
        self.duration = duration

        self.float = 0
        self.early_start = 0
        self.late_start = 0
        self.early_finish = 0
        self.late_finish = 0

        self.next = None
        self.previous = None

    def __str__(self):
        # to show all the information in the __init__()
        sentence = "activity ".capitalize() + self.name.upper()\
            + ":" + "\n\tES: " + str(self.early_start) + "\t LS: " + str(self.late_finish)\
            + "\n\tEF: " + str(self.early_finish) + "\t LF: " + str(self.late_finish)\
            + "\n\tDuration: \t" + str(self.duration)\
            + "\n\tFloat: \t\t" + str(self.float) + "\n"
        return sentence

class LinkedList():

    def __init__(self):
        self.head = None

    def add_activity_to_end_of_list(self, duration_of_activity, name_of_activity):
        current_activity = self.head
        while current_activity.next is not None:
            current_activity = current_activity.next
        current_activity.next = Activity(
            duration_of_activity, name_of_activity)

    def add_at_start(self, duration_of_activity, name_of_activity):
        new_activity = Activity(4, "D")
        new_activity.next = self.head
        self.head = new_activity

    def print_list(self):
        activitylist = ""
        current_activity = self.head
        while current_activity.next is not None:
            activitylist += current_activity.name + "->"
            current_activity = current_activity.next
        activitylist += current_activity.name + "->x"
        print(activitylist)

    def print_schedule_information(self):
        current_activity = self.head
        while current_activity.next is not None:
            print(current_activity)
            current_activity = current_activity.next
        print(current_activity)


schedule = LinkedList()
schedule.head = Activity(5, "A")
schedule.add_activity_to_end_of_list(3, "B")
schedule.add_activity_to_end_of_list(5, "C")
schedule.add_at_start(4, "D")

schedule.print_list()
