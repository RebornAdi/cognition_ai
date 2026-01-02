# core/event.py

class Event:
    """
    Represents a single experience observed by the system.
    This is raw input, not reasoning.
    """

    def __init__(self, entity, attribute, outcome, reliability, timestamp):
        self.entity = entity
        self.attribute = attribute
        self.outcome = outcome
        self.reliability = reliability
        self.timestamp = timestamp

    def __repr__(self):
        return (
            f"Event(entity={self.entity}, "
            f"attribute={self.attribute}, "
            f"outcome={self.outcome}, "
            f"reliability={self.reliability}, "
            f"timestamp={self.timestamp})"
        )
