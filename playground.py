class Car:

    owner = None
    number_of_wheels = None
    engine = None
    brand = None
    number_of_seats = None

    def __init__(self, owner, number_of_wheels, engine, brand, number_of_seats):
        self.owner = owner
        self.number_of_wheels = number_of_wheels
        self.engine = engine
        self.brand = brand
        self.number_of_seats = number_of_seats

    def start(self):
        print(f"{self.owner}'s car : Vroum vroum")

    def break_speed(self):
        print(f"{self.owner}'s car : I'm decreasing my speed")

    def stop(self):
        print(f"{self.owner}'s car : car engine stopped")

    def __str__(self):
        description_string = f"{self.owner}'s car has {self.number_of_wheels} wheel(s) and {self.number_of_seats} seats. It's a {self.brand} with a {self.engine} engine"
        return description_string
        

# -------------------------------------------------------------------

my_car = Car(owner = "Nathan", number_of_wheels=4, number_of_seats=2, brand="BMW", engine=116)
print(my_car)
my_car.start()
my_car.break_speed()
my_car.stop()

mom_car = Car(owner = "Mummy", number_of_wheels=4, number_of_seats=4, brand="Aston", engine="V8")
print(mom_car)
mom_car.start()
mom_car.break_speed()
mom_car.stop()