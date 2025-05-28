"""
Создайте класс `Car`, наследник `Vehicle`
"""
from homework_05.base import Vehicle
from homework_05.engine import Engine

class Car(Vehicle):
    def __init__(self, engine):
        super().__init__(weight, fuel, fuel_consumption)
        self.engine: Engine = None

    def set_engine(self, engine: Engine):
        self.engine = engine