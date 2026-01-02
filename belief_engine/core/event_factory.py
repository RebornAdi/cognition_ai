# core/event_factory.py

from core.event import Event

class EventFactory:
    """
    Responsible for creating clean, consistent events.
    """

    @staticmethod
    def create(entity, attribute, outcome, reliability, timestamp, context=None):
        return Event(
            entity=entity,
            attribute=attribute,
            outcome=outcome,
            reliability=reliability,
            timestamp=timestamp,
            context=context
        )
