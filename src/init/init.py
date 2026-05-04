from ..main import main

def init():
    print("Loading Linux 7.1-rc2 distro powered by python")
    print("This is a work in progress, expect bugs and crashes")
    print("If you want to contribute, please check out the github repository")
    while True:
        command = input()
        if command == "exit":
            break
        if command == "test":
            main.test()



if __name__ == "__main__":    
    init()