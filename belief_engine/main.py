# main.py

from core.event_factory import EventFactory
from core.belief import Belief

if __name__ == "__main__":
    belief = Belief("Red objects are dangerous", confidence=0.6)

    e1 = EventFactory.create("object", "red", "damage", 0.9, 1)
    e2 = EventFactory.create("object", "red", "safe", 0.8, 2)

    belief.update(e1, is_support=True)
    belief.update(e2, is_support=False)

    print(belief)
    print()
    print(belief.explain())
    print()
    print("HISTORY LOG:")
    for h in belief.history:
        print(h)
