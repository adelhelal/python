from models.mammal import Mammal

class Person(Mammal):
    def __init__(self, name) -> None:
        self.name = name

    def walk(self):
        return f"{self.name} walks"

    def run(self, speed):
        return f"{self.name} runs at {speed}km/h"
