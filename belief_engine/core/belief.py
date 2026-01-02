# core/belief.py

class Belief:
    """
    Represents a belief held by the system.
    Beliefs are hypotheses with confidence, not facts.
    """

    def __init__(self, statement, confidence=0.5):
        self.statement = statement
        self.confidence = float(confidence)

        # Evidence tracking
        self.support_events = []
        self.contradict_events = []

        # History of belief evolution
        self.history = []

        # Initial state log
        self._log_history(
            action="created",
            confidence=self.confidence,
            note="Initial belief formation"
        )

    def add_support(self, event):
        """Register supporting evidence (no confidence update yet)."""
        self.support_events.append(event)
        self._log_history(
            action="support_added",
            confidence=self.confidence,
            note=f"Support from event {event.signature()}"
        )

    def add_contradiction(self, event):
        """Register contradicting evidence (no confidence update yet)."""
        self.contradict_events.append(event)
        self._log_history(
            action="contradiction_added",
            confidence=self.confidence,
            note=f"Contradiction from event {event.signature()}"
        )

    def update(self, event, is_support):
        """
        Temporary placeholder update.
        Real confidence logic comes Day 4.
        """
        if is_support:
            self.add_support(event)
        else:
            self.add_contradiction(event)

    def decay(self):
        """
        Placeholder for belief decay.
        Implemented Day 5.
        """
        self._log_history(
            action="decay_called",
            confidence=self.confidence,
            note="Decay placeholder"
        )

    def explain(self):
        """
        Human-readable explanation (basic version).
        """
        return (
            f"I believe '{self.statement}' with confidence {round(self.confidence, 2)}.\n"
            f"Supporting events: {len(self.support_events)}\n"
            f"Contradicting events: {len(self.contradict_events)}"
        )

    def _log_history(self, action, confidence, note):
        self.history.append({
            "action": action,
            "confidence": round(confidence, 4),
            "note": note
        })

    def __repr__(self):
        return (
            f"Belief(statement='{self.statement}', "
            f"confidence={round(self.confidence, 2)}, "
            f"support={len(self.support_events)}, "
            f"contradictions={len(self.contradict_events)})"
        )
