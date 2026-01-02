# core/event.py

class Event:
    """
    Represents a single experience observed by the system.
    This is raw input, not reasoning.
    """

    def __init__(
        self,
        entity,
        attribute,
        outcome,
        reliability,
        timestamp,
        context=None
    ):
        self.entity = entity              # e.g., "object"
        self.attribute = attribute        # e.g., "red"
        self.outcome = outcome            # e.g., "damage"
        self.reliability = float(reliability)  # [0,1]
        self.timestamp = timestamp        # logical time
        self.context = context or {}      # optional metadata

    def signature(self):
        """
        Abstract identity of the event (used later for pattern detection)
        """
        return (self.entity, self.attribute, self.outcome)

    def __repr__(self):
        return (
            f"Event(entity={self.entity}, "
            f"attribute={self.attribute}, "
            f"outcome={self.outcome}, "
            f"reliability={self.reliability}, "
            f"timestamp={self.timestamp}, "
            f"context={self.context})"
        )
