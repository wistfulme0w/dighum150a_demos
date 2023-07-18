import random
# simulates a dog chasing its tail. On each loop, there is a 10% chance of catching the tail
# and a 20% chance of seeing a squirrel.

# variable setup
caughtTail = False
while(caughtTail == False):
    print("Chasing Tail")
    seesquirrel = random.randint(0,10)
    catchtail = random.randint(0,10)
    if seesquirrel < 2:
        print("SQUIRREL!")
        break
    if catchtail < 1:
        print("The tail has been caught.")
        caughtTail = True
