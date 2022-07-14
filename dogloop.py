import random
# simulates a dog chasing its tail. On each loop, there is a 10% chance of catching the tail
# and a 20% chance of seeing a squirrel.
if __name__ == "__main__":
    # variable setup
    caughtTail = False
    while(caughtTail == False):
        print("Chasing Tail")
        if random.randint(0, 10) < 2:
            print("SQUIRREL!")
            break
        if random.randint(0, 10) < 1:
            print("The tail has been caught.")
            caughtTail = True
