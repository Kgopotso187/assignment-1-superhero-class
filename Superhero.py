# Base Class
class Superhero:
    def __init__(self, name, power, health):
        self.name = name
        self.power = power
        self.health = health

    def attack(self, target):
        print(f"{self.name} attacks {target} using {self.power}!")

    def heal(self, amount):
        self.health += amount
        print(f"{self.name} heals for {amount} points. Health is now {self.health}.")

    def display_stats(self):
        print(f"Name: {self.name}\nPower: {self.power}\nHealth: {self.health}")


# Subclass with Inheritance and Polymorphism
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, health, flight_speed):
        super().__init__(name, power, health)  # Call the parent constructor
        self.flight_speed = flight_speed

    def fly(self):
        print(f"{self.name} soars through the sky at {self.flight_speed} km/h!")

    # Overriding the attack method to show polymorphism
    def attack(self, target):
        print(f"{self.name} swoops down from the sky and attacks {target} using {self.power}!")


# Testing the classes
hero1 = Superhero("Shadow Ninja", "Invisibility Strike", 100)
hero2 = FlyingSuperhero("Sky Blaze", "Flame Wings", 120, 300)

hero1.display_stats()
hero1.attack("Dr. Evil")
hero1.heal(20)

print("\n---\n")

hero2.display_stats()
hero2.fly()
hero2.attack("Ice Queen")  # Polymorphic behavior
