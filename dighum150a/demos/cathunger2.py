import random
if __name__ == "__main__":
    # This code sets up the variables we need to simulate a hungry cat.
    catHunger = random.randint(0, 10) #uses the randint function of the random library to generate a random int between 0 and 10.
    bowlFull = random.choice([True, False]) #uses the choice function to pick between different chocies in a list of them.
    if not bowlFull:
        print("The cat's dish is empty. Are you currently getting food? y/n")
        gettingFood = input()

    # This code simulates a hungry cat.
    if catHunger < 5: #There is a 50% chance of the cat being hungry.
        print("The cat walks to the bowl.")
        if bowlFull == True:
            print("The cat gobbles down his food.")
        elif gettingFood == "y":
            print("The cat rubs your legs encouragingly.")
            print("The cat  gobbles down his food.")
        else:
            print("MEOW")
            print("The cat spitefully scratches the furniture.")
    else:
        print("The cat is not hungry, so he scratches the furniture. ")
