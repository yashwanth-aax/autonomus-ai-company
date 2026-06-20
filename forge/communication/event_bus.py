# forge/communication/event_bus.py

class EventBus:

    def __init__(self, registry):

        self.registry = registry

        self.history = []

    def publish(self, message):

        receiver = self.registry.get(
            message.receiver
        )

        self.history.append(message)

        if receiver:

            receiver.receive_message(
                message
            )

        else:

            print(
                f"[EventBus] "
                f"Agent "
                f"{message.receiver} "
                f"not found."
            )

    def get_history(self):

        return self.history