import random
#generates a random number and feeds the cat if its hunry
catHunger = random.randint(0,10)
if catHunger <5:
    print("Cat is eating")
else:
    print("The cat is not hungry and is scratching the furniture.")