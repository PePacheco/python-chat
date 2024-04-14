class Msgfiltered:
    def __init__(self):
        self.param1 = None
        self.param2 = None
        self.param3 = None

    def process_message(self, message):
        parts = message.split(" ", 2)

        if len(parts) >= 2:
            self.param1 = parts[0]
            self.param2 = parts[1]

        if len(parts) == 3:
            self.param3 = parts[2]

        return self
