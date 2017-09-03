import uuid
import datetime

class Task:
    type = "Task Element"

    def __init__(self):
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
        self._name = None
        self._prerequisites = []
        self._id = uuid.uuid4()

    # Task methods
    # TODO: Define a set of date/duration calculation methods
    #       Such that:
    # Changing duration, will automatically calculate end date
    # Changing End date, will automatically calculate duration

    @staticmethod
    def calculate_date_from_duration(date, duration):
        try:
            return date + duration
        except TypeError:
            return  None

    @staticmethod
    def calculate_duration_from_date(date1, date2):
        try:
            return date2 - date1
        except TypeError:
            return None

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

    def append(self, value):
        """Append to prerequisites array"""
        self._prerequisites = self._prerequisites + [value]
        return self._prerequisites

    def extend(self, value):
        """Extends prerequisites """
        return self._prerequisites.extend(value)

    # Dependants
    @property
    def dependants(self):
        """Tasks depending on current task... aka children"""
        return self._dependants

    @dependants.setter
    def dependants(self, value):
        self._dependants = value

    def append(self, value):
        self._dependants = self._dependants + [value]
        return self._dependants

    def extend(self, value):
        return self._dependants.extend(value)

    # Planned
    # Starting
    @property
    def planned_start(self):
        """Task planned start date/time"""
        return self._planned_start

    @planned_start.setter
    def planned_start(self, value):
        self._planned_start = value

    # Ending
    @property
    def planned_end(self):
        """Task planned end date/time"""
        return self._planned_end

    @planned_end.setter
    def planned_end(self, value):
        self._planned_end = value

    # Duration
    @property
    def planned_duration(self):
        """Planned task duration"""
        return self._planned_duration

    @planned_duration.setter
    def planned_duration(self, value):
        self._planned_duration = value

    # Actual
    # Starting
    @property
    def actual_start(self):
        """Task actual start date/time"""
        return self._actual_start

    @actual_start.setter
    def actual_start(self, value):
        self._actual_start = value

    # Ending
    @property
    def actual_end(self):
        """Task actual end date/time"""
        return self._actual_end

    @actual_end.setter
    def actual_end(self, value):
        self._actual_end = value

    # Duration
    @property
    def actual_duration(self):
        """Actual task duration"""
        return self._actual_duration

    @actual_duration.setter
    def actual_duration(self, value):
        self._actual_duration = value

    # Status
    @property
    def completed(self):
        """Percentage Completed of this task, real number ranging from 0 to 1"""
        return self._pct_complete

    @completed.setter
    def completed(self, value):
        self._pct_complete = value
