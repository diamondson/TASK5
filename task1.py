class Airplane():
    def __init__(self,make,model,year,max_speed):
        self.make = make
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.odometer = 0
        self.is_flying = False
    
    def describe(self):
        print(f"make: {self.make.upper()}")
        print(f"model: {str(self.model)}")
        print(f"year: {str(self.year)}")
        print(f"max_speed: {str(self.max_speed)}")

    def take_off(self):
        self.is_flying = True

    def fly(self, miles):
        self.odometer += miles

    def land(self):
        self.is_flying = False

my_plane = Airplane("boing", 737, 2019, 793)

my_plane.describe()

print(my_plane.is_flying)

my_plane.take_off()
print(my_plane.is_flying)

print(my_plane.odometer)
my_plane.fly(1230)
print(my_plane.odometer)

my_plane.land()

print(my_plane.is_flying)
