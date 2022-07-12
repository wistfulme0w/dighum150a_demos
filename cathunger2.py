import random
if __name__ == "__main__":
    # This code sets up the variables we need to simulate a hungry cat.
    catHunger = random.randint(0, 10)
    bowlFull = random.choice([True, False])
    if not bowlFull:
        print("The cat's dish is empty. Are you currently getting food? y/n")
        gettingFood = input()

    # This code simulates a hungry cat.
    if catHunger < 5:
        print("The cat walks to the bowl.")
        if bowlFull == True:
            print("The cat gobbles down his food.")
        elif gettingFood == "y":
            print("The cat rubs your legs encouraginly.")
            print("The cat eats gobbles down his food.")
        else:
            print("MEOW")
            print("The cat spitefully scratches the furniture.")
    else:
        print("The cat is not hungry, so he scratches the furniture. ")
