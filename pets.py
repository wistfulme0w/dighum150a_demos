import random

class Pet():
    def __init__(self, name=""):
        self.name = name
        self.sex = random.choice(["Male", "Female"])
        self.coat_color = "black"
        self.eye_color = "yellow"

    def _say(self, message=""):
        print(f"{self.name} says: {message}")

    def makeNoise(self):
        raise NotImplementedError


class Dog(Pet):
    def __init__(self, name="Fido"):
        super().__init__(name)

    def makeNoise(self):
        self._say("BORK")
 

class Cat(Pet):
    def __init__(self, name="Cat"):
        super().__init__(name)

    def makeNoise(self):
        self._say("Meow")

    def purr(self):
        self._say("Purrrrrrrr")