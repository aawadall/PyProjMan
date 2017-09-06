import uuid

# Building Block
from PyProjMan import TimeElement


class Task:
    """Building block of a project plan"""
    type = "Task Element"

    def __init__(self, name=None):
        # Actual Task Metrics
        self._actual = None

        # Planned Task Metrics
        self._planned = None

        self._pct_complete = 0.0  # Percentage Completed

        self._dependants = []
        self._name = name
        self._prerequisites = []
        self._id = uuid.uuid4()

    # Task methods

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

            self._prerequisites.append(value)
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
            self._dependants.append(value)
            value.append_prerequisite(self)
        return self._dependants

    # Planned
    # Starting
    @property
    def planned(self):
        """Task planned timings"""
        return self._planned

    @planned.setter
    def planned(self, value):
        self._planned = TimeElement.assign_type(value, TimeElement, TimeElement)

    @property
    def actual(self):
        """Task actual start date/time"""
        return self._actual

    @actual.setter
    def actual(self, value):
        self._actual = TimeElement.assign_type(value, TimeElement, TimeElement)

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
        """.format(self.planned.start, self.planned.end, self.planned.duration,
                   self.actual.start, self.actual.end, self.actual.duration))

        # List Prerequisite Tasks
        print("Prerequisite Tasks")
        for prereq in self.prerequisites:
            print("{} - {}".format(prereq.id, prereq.name))
        # List Dependant Tasks
        print("Dependant Tasks")
        for dependant in self.dependants:
            print("{} - {}".format(dependant.id, dependant.name))
