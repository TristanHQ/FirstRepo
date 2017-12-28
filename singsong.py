def happy():
    print("Happy birthday to you!")

def sing(name):
    happy()
    happy()
    print("Happy birthday,dear",name + ".")
    happy()

def main():
    sing("Mike")
    print()
    sing("Lily")
    print()
    sing("Tom")

main()