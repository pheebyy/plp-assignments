class Animal:
    def move(self):
        raise NotImplementedError("Subclass must implement this method")

class Dog(Animal):
    def move(self):
        return "🐕 Running on four legs"

class Bird(Animal):
    def move(self):
        return "🐦 Flying in the sky"

class Fish(Animal):
    def move(self):
        return "🐟 Swimming in water"

# Vehicles
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclass must implement this method")

class Car(Vehicle):
    def move(self):
        return "🚗 Driving on the road"

class Plane(Vehicle):
    def move(self):
        return "✈️ Flying in the air"

class Boat(Vehicle):
    def move(self):
        return "⛴️ Sailing on water"

# Animals
animals = [Dog(), Bird(), Fish()]
for animal in animals:
    print(animal.move())

# Vehicles
vehicles = [Car(), Plane(), Boat()]
for vehicle in vehicles:
    print(vehicle.move())
