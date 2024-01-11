from entity import Entity


# кристал для восстановления здоровья черепашки
class HealthCrystal(Entity):
    def __init__(self):
        super().__init__("health_cristal", sprite="health_crystal.png")
