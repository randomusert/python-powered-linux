from userspace_v1.main.commands.BaseCommands import BaseCommands
import platform
import os

class VerCommand(BaseCommands):
    def __init__(self, args):
        self.args = args

    def execute(self):

        runningOs = platform.system()
        if(runningOs != "linux"):
            print("This program is designed to run on Linux. You are running on " + runningOs)
            print("Please switch to a Linux environment to use this program.")
            return


        print("TINOSLE Python 0.10-beta1")
        print("This is a work in progress, expect bugs and crashes")
        print("If you want to contribute, please check out the github repository")
        print(f"Kernel version: {os.uname().release}")
        print(f"Architecture: {platform.machine()}")
        print("Userland version: 0.1.0-beta1")