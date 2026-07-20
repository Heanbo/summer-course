from enum import Enum

class Throw(Enum):
    Rock = 0
    Paper = 1
    Scissors = 2

    def __str__(self) -> str:
        return self.name
    
    def __lt__(self, other):
        if other.value == len(Throw) - 1 and self.value == 0:
            return "win"
        elif other.value == 0 and self.value == len(Throw) - 1:
            return "loss"
        elif other.value == self.value:
            return "tie"
        elif other.value < self.value:
            return "win"
        else:
            return "loss"