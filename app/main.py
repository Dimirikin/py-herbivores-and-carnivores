class Animal():
    alive: list["Animal"] = []

    def __init__(
            self,
            name: str,
            health: int = 100
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = False

        Animal.alive.append(self)

    def take_damage(self, damage: int) -> None:
        self.health -= damage
        if self.health <= 0:
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, other: "Herbivore") -> None:
        if (
            other in Animal.alive
            and isinstance(other, Herbivore)
            and not other.hidden
        ):
            other.take_damage(50)
