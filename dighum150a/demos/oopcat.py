import random


class Cat:
    claws = True

    def __init__(self, name="Cat"):
        # this method is an init method. When called, it sets up all the initial instance attribute values
        # for an object. Every time we make a new cat, this will run.
        self.name = name  # this is an instance attribute
        self.hunger = 10
        self.boredom = 10
        self.sex = random.choice(["Male", "Female"])
        eye_colors = ["blue", "green", "yellow", "orange"]
        coat_colors = ["brown", "white", "Siamese", "Gray Tabby",
                       "Orange and Black Tabby", "Gray", "Black", "Black and white spotted", "Tuxedo"]
        if self.sex == "Male":
            coat_colors.append("Orange")
        else:
            coat_colors.append("Calico")
        self.coat_color = random.choice(coat_colors)
        self.eye_color = random.choice(eye_colors)

    def __str__(self):
        return f"{self.name} is a {self.sex} {self.coat_color} cat with {self.eye_color} eyes."

    def meow(self):
        print("<<Meow>>")


if __name__ == "__main__":
    # make some cats!
    list_o_cats = []
    for i in range(0, 10):
        list_o_cats.append(Cat())

    for cat in list_o_cats:
        print(cat)
