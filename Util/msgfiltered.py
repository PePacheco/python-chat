from Util.commands import Commands

cmds = Commands()

class Msgfiltered:
    def __init__(self):
        self.param1 = None
        self.param2 = None
        self.param3 = None

    def process_message(self, message):
<<<<<<< HEAD
        parts = message.split(" ", 2)

        if len(parts) >= 2:
            self.param1 = parts[0]
            self.param2 = parts[1]

        if len(parts) == 3:
            self.param3 = parts[2]
=======

        msg = message.split(" ", 1)
        self.param1 = msg[0]
        print(self.param1)

        if self.param1 != cmds.ALL and self.param1 != cmds.REG:
            msg = msg[1].split(" ", 1)
            self.param2 = msg[0]
            self.param3 = msg[1]
            print("Cagou")
            return self
        print(f'{msg[1]}')
        self.param2 = msg[1]
>>>>>>> origin/Pedrao

        return self
