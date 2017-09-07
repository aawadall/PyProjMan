import datetime
from PyProjManCore.helpers import assign_type, calculate_dates_and_durations


class TimeElement:
    """
    Time Element, is a repeated unit used in the Task Object
    It can be actual time, estimated time,
    best case estimated time,
    worst case estimated time or anything else
    This piece of code was refactored in a separate class to avoid high number of methods in Task class
    """

    def __init__(self, start=None, end=None, duration=None):
        self._start = None
        self._end = None
        self._duration = None
        self._start = assign_type(start, datetime.date, datetime.datetime)
        self._end = assign_type(end, datetime.date, datetime.datetime)
        self._duration = assign_type(duration, datetime.timedelta, datetime.timedelta)
        _start, _end, _duration = calculate_dates_and_durations(self._start, self._end, self._duration)

    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, value):
        self._start = assign_type(value, datetime.datetime, datetime.date)
        self._start, self._end, self._duration = calculate_dates_and_durations(self._start,
                                                                               self._end,
                                                                               self._duration)

    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, value):
        self._end = assign_type(value, datetime.datetime, datetime.date)
        self._start, self._end, self._duration = calculate_dates_and_durations(self._start,
                                                                               self._end,
                                                                               self._duration)

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        self._duration = assign_type(value, datetime.timedelta, datetime.timedelta)
        self._start, self._end, self._duration = calculate_dates_and_durations(self._start,
                                                                               self._end,
                                                                               self._duration)

    def __eq__(self, other):
        if isinstance(other, TimeElement):
            return self._start == other.start and self._end == other.end and self._duration == other.duration
