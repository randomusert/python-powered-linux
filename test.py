
def test():
    print("This script is runs the init script for the linux distro, it is used for testing purposes only on windows and should not be included in the final product")
    from userspace_v1.init import init
    init.init()

if __name__ == "__main__":
    test()