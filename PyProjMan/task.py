import uuid
import datetime
# Building Block
class Task:
    """Building block of a project plan"""
    type = "Task Element"

    def __init__(self,name=None):
        # Actual Task Metrics
        self._actual_start = None  # Start Date/Time
        self._actual_end = None  # End Date/Time
        self._actual_duration = None  # Duration

        # Planned Task Metrics
        self._planned_duration = None  # Duration
        self._planned_start = None  # Start Date/Time
        self._planned_end = None  # End Date/Time

        self._pct_complete = 0.0  # Percentage Completed

        self._dependants = []
        self._name = name
        self._prerequisites = []
        self._id = uuid.uuid4()

    # Task methods

    @staticmethod
    def calculate_end_date(date1, duration):
        try:
            return date1 + duration
        except TypeError:
            return  None

    @staticmethod
    def calculate_duration_from_date(date1, date2):
        try:
            if date2 > date1:
                return date2 - date1
            return None
        except TypeError:
            return None

    @staticmethod
    def calculate_start_date(date2, duration):
        try:
            return date2 - duration
        except TypeError:
            return  None

    # Tasks should have
    # ID, Read only property generated at construction
    @property
    def id(self):
        """Unique Task ID
        :rtype: UUID
        """
        return self._id

    # Name
    @property
    def name(self):
        """Task Name"""
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    # Predecessors
    @property
    def prerequisites(self):
        """Task predecessors ... aka predecessors"""
        return self._prerequisites

    @prerequisites.setter
    def prerequisites(self, value):
        """One transaction setting"""
        self._prerequisites = value

    def append_prerequisite(self, value):
        """Append to prerequisites array"""
        if value not in self._prerequisites:

            self._prerequisites = self._prerequisites + [value]
            value.append_dependant(self)
        return self._prerequisites



    # Dependants
    @property
    def dependants(self):
        """Tasks depending on current task... aka children"""
        return self._dependants

    @dependants.setter
    def dependants(self, value):
        self._dependants = value

    def append_dependant(self, value):
        if value not in self._dependants:
            self._dependants = self._dependants + [value]
            value.append_prerequisite(self)
        return self._dependants


    # Planned
    # Starting
    @property
    def planned_start(self):
        """Task planned start date/time"""
        return self._planned_start

    @planned_start.setter
    def planned_start(self, value):
        self._planned_start = value
        # Calculate Rest of components from this and a known one
        if self._planned_duration is not None:
            self._planned_end = Task.calculate_end_date(date1= self._planned_start, duration= self.planned_duration)
        elif self._planned_end is not None:
            self._planned_duration = Task.calculate_duration_from_date(date1= self.planned_start,date2= self.planned_end)

    # Ending
    @property
    def planned_end(self):
        """Task planned end date/time"""
        return self._planned_end

    @planned_end.setter
    def planned_end(self, value):
        self._planned_end = value
        # Calculate Rest of components from this and a known one
        if self._planned_duration is not None:
            self._planned_start = Task.calculate_start_date(date2= self._planned_end ,duration= self.planned_duration)
        elif self._planned_start is not None:
            self._planned_duration = Task.calculate_duration_from_date(date1= self.planned_start,date2= self.planned_end)

    # Duration
    @property
    def planned_duration(self):
        """Planned task duration"""
        return self._planned_duration

    @planned_duration.setter
    def planned_duration(self, value):
        self._planned_duration = value

        # Calculate Rest of components from this and a known one
        if self._planned_start is not None:
            self.planned_end = Task.calculate_end_date(date1= self._planned_start ,duration=self._planned_duration)
        elif self._planned_end is not None:
            self.planned_start = Task.calculate_start_date(date2= self._planned_end,duration=  self._planned_duration)

    # Actual
    # Starting
    @property
    def actual_start(self):
        """Task actual start date/time"""
        return self._actual_start

    @actual_start.setter
    def actual_start(self, value):
        self._actual_start = value
        # Calculate Rest of components from this and a known one
        if self._actual_duration is not None:
            self.actual_end = Task.calculate_end_date(self._actual_start , self.actual_duration)
        elif self._actual_end is not None:
            self.actual_duration = Task.calculate_duration_from_date(self.actual_start, self.actual_end)

    # Ending
    @property
    def actual_end(self):
        """Task actual end date/time"""
        return self._actual_end

    @actual_end.setter
    def actual_end(self, value):
        self._actual_end = value
        # Calculate Rest of components from this and a known one
        if self._actual_start is not None:
            self._actual_duration = Task.calculate_duration_from_date(self._actual_start , self.actual_end)
        elif self._actual_duration is not None:
            self._actual_start = Task.calculate_start_date(self.actual_end, self.actual_duration)

    # Duration
    @property
    def actual_duration(self):
        """Actual task duration"""
        return self._actual_duration

    @actual_duration.setter
    def actual_duration(self, value):
        self._actual_duration = value
        # Calculate Rest of components from this and a known one
        if self._actual_start is not None:
            self.actual_end = Task.calculate_end_date(self._actual_start , self.actual_duration)
        elif self._actual_end is not None:
            self.actual_start = Task.calculate_start_date(self.actual_end, self.actual_duration)

    # Status
    @property
    def completed(self):
        """Percentage Completed of this task, real number ranging from 0 to 1"""
        return self._pct_complete

    @completed.setter
    def completed(self, value):
        self._pct_complete = value

    def report(self):
        """Report Current Task Statistics"""
        # List Task ID, Name
        print("{} : {}".format(self.id, self.name))
        # List Task Status
        print("{} % Completed ".format(self.completed*100))
        #  List Planned/Actual Time Metrics
        print("""
Planned:    
    Start   : {}  
    End     : {}  
    Duration: {}
Actual:     
    Start   : {}
    End     : {}
    Duration: {}
        """.format(self.planned_start, self.planned_end, self.planned_duration,
                   self.actual_start, self.actual_end, self.actual_duration))

        # List Prerequisite Tasks
        print("Prerequisite Tasks")
        for prereq in self.prerequisites:
            print("{} - {}".format(prereq.id, prereq.name))
        # List Dependant Tasks
        print("Dependant Tasks")
        for dependant in self.dependants:
            print("{} - {}".format(dependant.id, dependant.name))

    def project_stats(self):
        """Reports overall project statistics starting from current node"""
        # Overall Start, Overall End, Overall Duration, Overall Completed
        # List Prerequisites
        # Task Name, Start, End, Completed
        # List Dependants
        # Task Name, Start, End, Completed


    def crawl_up(self):
        """Search all parent tasks"""
        parents = []
        if self._prerequisites.__len__()  != 0:
            for prerequisite in self._prerequisites:
                parents.extend(prerequisite.crawl_up())

        return list(set(parents))

    def crawl_down(self):
        """Search all children tasks"""
        children = []
        if self._dependants.__len__()  != 0:
            for child in self._dependants:
                children.extend(child.crawl_down())
        return list(set(children))