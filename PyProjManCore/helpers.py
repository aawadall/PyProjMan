def assign_type(source, type1, type2):
    """Check class of source, if matches passed types, then assign destination the value of source"""
    if isinstance(source, type1) \
            or isinstance(source, type2):
        return source
    return None


def calculate_dates_and_durations(start=None, end=None, duration=None):
    """
    Calculates Start Date, End Date or Duration from the other two known's
    Rule is:
    If all Given Data is not none, then calculate end date from start and duration,
    if two are known, then calculate the third from them
    if less than two are known, then do nothing
    """
    if start is not None \
            and duration is not None:
        end = start + duration
    if start is not None \
            and end is not None:
        duration = end - start
    if end is not None \
            and duration is not None:
        start = end - duration
    return start, end, duration
