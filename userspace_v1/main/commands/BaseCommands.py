# Gives info what commands need to have to be implemented
class BaseCommands:
    def __init__(self, args):
        self.args = args

    def execute(self):
        raise NotImplementedError("This method should be overridden by subclasses")