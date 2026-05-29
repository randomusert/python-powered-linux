from userspace_v1.main.commands import BaseCommands

class VerCommand(BaseCommands):
    def __init__(self, args):
        self.args = args

    def execute(self):
        print("TINOSLE Python 0.10-beta1")
        print("This is a work in progress, expect bugs and crashes")
        print("If you want to contribute, please check out the github repository")
        print("Kernel version: 7.1-rc5")
        print("Architecture: x86_64")
        print("Userland version: 0.1.0-beta1")