from abc import ABC, abstractmethod

from creature import Creature, Satiety


class Action(ABC):
    name: str

    def __init__(self, timer: int = None, origin: Creature = None):
        self.origin = origin
        self.timer = timer

    @abstractmethod
    def action(self):
        pass


class Feed(Action):
    def __init__(self,
                 amount: int,
                 timer: int = None,
                 origin: Creature = None
                 ):
        super().__init__(timer, origin)
        self.amount = amount

    def action(self):
        self.origin.params[Satiety] += self.amount
