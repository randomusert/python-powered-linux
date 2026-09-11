# exec command

import subprocess
import os

from .BaseCommands import BaseCommands

class ExecCommand(BaseCommands):
    def __init__(self, args):
        self.args = args

    def execute(self):
        if not self.args:
            print("Error: No command provided.")
            return

        command = self.args[0]
        command_args = self.args[1:]

        try:
            result = subprocess.run([command] + command_args, check=True, text=True, capture_output=True)
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Error executing command '{command}': {e.stderr}")
        except FileNotFoundError:
            print(f"Command '{command}' not found.")