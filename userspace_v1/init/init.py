import time

from userspace_v1.main import main
from userspace_v1.main.commands import dir

def init():
    print("Loading Linux 7.3-rc2 distro powered by python")

    time.sleep(2)
    command_parts = input().split()
    command = command_parts[0]
    args = command_parts[1:]

    print("Load complete")
    while True:
        print("> ", end="")
        command_parts = input().split()

        if not command_parts:
            continue

        command = command_parts[0]
        args = command_parts[1:]

        if command == "exit":
            break

        if command == "test":
            main.test.execute(main.test, "DEV")

        if command == "dir":
            path = args[0] if args else "."
            dir.DirCommand(path).execute()

        if command == "help":
            print("Available commands:")
            print("exit - Exit the program")
            print("test - Run the test command")
            print("dir [path] - List files in a directory")
            print("help - Show this help message")
            print("ver - Show version information")

        if command == "ver":
            from userspace_v1.main.commands import ver
            ver.VerCommand(args).execute()
        else:
            print(f"Unknown command: {command}. Type 'help' for a list of commands.")



if __name__ == "__main__":    
    init()