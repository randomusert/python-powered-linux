import os

class DirCommand:
    def __init__(self, path='.'):
        self.path = path

    def execute(self):
        try:
            files = os.listdir(self.path)
            for file in files:
                print(file)
        except FileNotFoundError:
            print(f"Directory '{self.path}' not found.")
        except PermissionError:
            print(f"Permission denied for directory '{self.path}'.")