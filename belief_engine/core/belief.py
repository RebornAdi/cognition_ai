# core/belief.py

class Belief:
    """
    Represents a belief held by the system.
    Beliefs are hypotheses with confidence, not facts.
    """

    def __init__(self, statement, confidence=0.5):
        self.statement = statement
        self.confidence = confidence

        # Evidence tracking
        self.support_count = 0
        self.contradict_count = 0

        # History of belief changes (for explainability)
        self.history = []

    def update(self, event):
        """
        Update belief based on a new event.
        Logic will be implemented later.
        """
        pass

    def decay(self):
        """
        Apply time-based forgetting.
        Logic will be implemented later.
        """
        pass

    def explain(self):
        """
        Return a human-readable explanation of this belief.
        """
        pass

    def __repr__(self):
        return (
            f"Belief(statement='{self.statement}', "
            f"confidence={round(self.confidence, 2)})"
        )
