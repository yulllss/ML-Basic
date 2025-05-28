"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""
class LowFuelError(Exception):
    """Недостаточно топлива для запуска"""
    pass


class NotEnoughFuel(Exception):
    """Недостаточно топлива для преодоления дистанции"""
    pass


class CargoOverload(Exception):
    """Превышена максимальная грузоподъемность"""
    pass