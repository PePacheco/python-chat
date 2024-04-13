class Msgfiltered:
    def __init__(self):
        self.primary_command = None
        self.second_command  = None
        self.message_content = None

    def process_message(self, sender_id, message):
        parts = message.split(" ", 2)

        if len(parts) >= 2:
            self.primary_command = parts[0]
            self.second_command  = parts[1]

        if len(parts) == 3:
            self.message_content = parts[2]
        