from userspace_v1.main.commands.BaseCommands import BaseCommands
import platform
import os
import io

class MkdirCommand(BaseCommands):
    def __init__(self, args):
        self.args = args

    def execute(self):
        if not self.args:
            print("Error: No directory name provided.")
            return

        dir_name = self.args[0]

        try:
            os.makedirs(dir_name, exist_ok=True)
            print(f"Directory '{dir_name}' created successfully.")
        except Exception as e:
            if (e == FileExistsError):
                print(f"Error: Directory '{dir_name}' already exists.")
            elif (e == PermissionError):
                print(f"Error: Permission denied to create directory '{dir_name}'.")
            else:
                print(f"Unknown error occured during directory creation: {e}")