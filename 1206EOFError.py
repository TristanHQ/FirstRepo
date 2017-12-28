import sys
try:
    s=input("Your name:")
except EOFError:
    print("\nWhy di you do an EOFError on me?")
    sys.exit()
else:
    print("BYE!")
