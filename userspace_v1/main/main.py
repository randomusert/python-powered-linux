class test:
    def __init__(self, env="DEV"):
        self.env = env

    def execute(self, env):
        if env == "DEV":
            print("this is a test class")
        else:
            print("This environment is not supported. Please put the argument to DEV to run the test command.")