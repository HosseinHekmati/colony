class MessageBus:
    def __init__(self):
        self.messages = []

    def send(self, sender, receiver, content):
        msg = {
            "from": sender,
            "to": receiver,
            "content": content
        }
        self.messages.append(msg)

    def fetch_all(self):
        msgs = self.messages[:]
        self.messages.clear()
        return msgs
