from Util.commands import Commands

cmds = Commands()

class Msgfiltered:
    def __init__(self):
        self.param1 = None
        self.param2 = None
        self.param3 = None

    def process_message(self, message):
        self.param1 = None
        self.param2 = None
        self.param3 = None

        msg = message.split(" ", 1)
        self.param1 = msg[0]
        
        if self.param1 != cmds.REG:
            msg = msg[1].split(" ", 1)
            self.param2 = msg[0]
            self.param3 = msg[1]
            return self
        print(f'{msg[1]}')
        self.param2 = msg[1]
        print(self.param1, self.param2, self.param3)

        return self
