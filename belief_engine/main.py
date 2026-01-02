# main.py

from core.event_factory import EventFactory

if __name__ == "__main__":
    events = [
        EventFactory.create("object", "red", "damage", 0.9, 1),
        EventFactory.create("object", "red", "damage", 0.8, 2),
        EventFactory.create("object", "red", "safe", 0.7, 3),
        EventFactory.create("object", "blue", "safe", 0.9, 4),
    ]

    for e in events:
        print(e)
        print("Signature:", e.signature())
        print("-" * 40)
