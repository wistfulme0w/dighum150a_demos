friends = ["Spock","Kirk","McCoy","Scotty","Sulu","Uhuru"]

def enterStarwarsDimension():
    friends = ["Chewie","Luke","Leah","Han","R2D2","C3PO"]
    planets = ["Endor","Tatooine","Hoth"]
    print(f"In the Starwars dimension, my friends are:{friends}")
    enterDrWhoDimension()

def enterDrWhoDimension():
    friends = ["Sarah-Jane","The Doctor","K-9","Leela"]
    planets = ["Earth","Gallifrey"]
    print(f"In the Dr. Who dimension, the planets are {planets}, and my friends are:")
    for friend in friends:
        a = friend
        print(a)
    #in python, I can access local variables outside of the block in which they were declared. 
    #This is not true in every language.
    print(a)
    enterDuneDimension()

def enterDuneDimension():
    friends = ["Lady Jessica","Alia","Paul Atreides"]
    planets = ["Dune","Caladan","Gedes Prime"]
    print(f"My friends in the Dune Dimension are {friends} ")
    enterVoidDimension()

def enterVoidDimension():
    friends = []
    print(f" In the void dimension, my friends are: {friends}")


enterStarwarsDimension()
print(f"In the global scope, my friends are: {friends}")