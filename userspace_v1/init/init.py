from userspace_v1.main import main
from userspace_v1.main.commands import dir

def init():
    print("Loading Linux 7.1-rc5 distro powered by python")
    print("This is a work in progress, expect bugs and crashes")
    print("If you want to contribute, please check out the github repository")
    while True:
        print(">")
        command = input()
        if command == "exit":
            break
        if command == "test":
            main.test.execute(main.test, "PROD")
        if command == "dir":
            dir.DirCommand().execute()
        if command == "help":
            print("Available commands:")
            print("exit - Exit the program")
            print("test - Run the test command")
            print("dir - List files in the current directory")
            print("help - Show this help message")
        



if __name__ == "__main__":    
    init()