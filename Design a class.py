# Base class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def device_info(self):
        return f"{self.brand} {self.model}"

# Derived class (inheritance)
class Smartphone(Device):
    def __init__(self, brand, model, os, storage):
        super().__init__(brand, model)  # Call parent constructor
        self.os = os
        self.storage = storage
    
    def call(self, number):
        return f"📱 Calling {number} from {self.device_info()}..."
    
    def install_app(self, app):
        return f"📲 Installing {app} on {self.device_info()} ({self.os})"

# Another derived class
class Tablet(Device):
    def __init__(self, brand, model, screen_size):
        super().__init__(brand, model)
        self.screen_size = screen_size
    
    def watch_movie(self, movie):
        return f"🎬 Watching '{movie}' on {self.device_info()} ({self.screen_size}-inch screen)"
phone1 = Smartphone("Samsung", "Galaxy S25", "Android", "256GB")
tablet1 = Tablet("Apple", "iPad Pro", 12.9)

print(phone1.call("0722891640"))
print(phone1.install_app("Instagram"))
print(tablet1.watch_movie("Black Panther"))
