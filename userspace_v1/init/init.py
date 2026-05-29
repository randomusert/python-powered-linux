import time

from userspace_v1.main import main
from userspace_v1.main.commands import dir

def init():
    print("Loading Linux 7.1-rc5 distro powered by python")

    time.sleep(2)

    print("Load complete")
    while True:
        print("> ", end="")
        command = input()

        if command == "exit":
            break

        if command == "test":
            main.test.execute(main.test, "DEV")
        
        if command == "dir":
            dir.DirCommand().execute()
        
        if command == "help":
            print("Available commands:")
            print("exit - Exit the program")
            print("test - Run the test command")
            print("dir - List files in the current directory")
            print("help - Show this help message")
            print("ver - Show version information(Not working currently)")

        if command == "ver":
            from userspace_v1.main.commands import ver
            ver.VerCommand().execute()
        



if __name__ == "__main__":    
    init()