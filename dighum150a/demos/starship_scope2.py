friends = ["Spock","Kirk","McCoy","Scotty","Sulu","Uhuru"]
planets = []
def enterStarwarsDimension(friends):
    friends.extend(["Chewie","Luke","Leah","Han","R2D2","C3PO"])
    global planets 
    planets.extend(["Endor","Tatooine","Hoth"])
    enterDrWhoDimension(friends)
    return friends

def enterDrWhoDimension(friends):
    friends.extend(["Sarah-Jane","The Doctor","K-9","Leela"])
    global planets
    planets.extend(["Earth","Gallifrey"])
    #in python, I can access local variables outside of the block in which they were declared. 
    #This is not true in every language.
    enterDuneDimension(friends)
    return friends

def enterDuneDimension(friends):
    friends.extend( ["Lady Jessica","Alia","Paul Atreides"])
    global planets
    planets.extend(["Dune","Caladan","Gedes Prime"])
    enterVoidDimension(friends)
    return friends

def enterVoidDimension(friends):
    friends.extend([])
    return friends


friends = enterStarwarsDimension(friends)
print(f"In the global scope, my friends are: {friends}")
print(planets)