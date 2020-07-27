class Vehicle:

    owner = None
    color = None
    
    def __init__(self, owner, color):
        self.owner = owner
        self.color = color

    def start(self):
        print("The vehicle is started")

    def stop(self):
        print("The vehicle is stopped")


class Car(Vehicle):

    engine_power = None
    number_of_wheels = None

    def __init__(self, engine_power, number_of_wheels, owner, color):
        super().__init__(owner, color)
        self.engine_power = engine_power
        self.number_of_wheels = number_of_wheels
    
    def start(self):
        print("Vroum Vroum !")

class Boat(Vehicle):

    has_rescue_boat = None
    has_sails = None
    
    def __init__(self, has_rescue_boat, has_sails, owner, color):
        super().__init__(owner, color)
        self.has_rescue_boat = has_rescue_boat
        self.has_sails = has_sails

    def start(self):
        print("Let's sail !")

    
a_vehicle = Vehicle(owner="Nathan", color="Blue")
a_car = Car(engine_power="V8", number_of_wheels=4, owner="Nathan", color="Blue")
a_boat = Boat(has_rescue_boat=True, has_sails=True, owner="Nathan", color="Blue")

a_vehicle.start()
a_car.start()
a_boat.start()

a_vehicle.stop()
a_car.stop()
a_boat.stop()
