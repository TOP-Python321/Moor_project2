from abc import ABC, abstractmethod

from creature import Creature


class Action(ABC):
    name: str

    def __init__(self, origin: Creature, timer: int = 0):
        self.origin = origin
        self.timer = timer

    @abstractmethod
    def action(self):
        pass