class Car:

    owner = None
    number_of_wheels = None
    engine = None
    brand = None
    number_of_seats = None
    _engine_oil = "Oil ABC"
    __engine_candle = "Candle CDF"

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

    def _compressing_oil(self):
        print("Compressing the oil")
    
    def __lighting_up(self):
        print("BOUM")
    
    def accessing_private_attribute(self):
        return self.__engine_candle
    
    def accessing_private_method(self):
        return self.__lighting_up()

    def __str__(self):
        description_string = f"{self.owner}'s car has {self.number_of_wheels} wheel(s) and {self.number_of_seats} seats. It's a {self.brand} with a {self.engine} engine"
        return description_string
        

# -------------------------------------------------------------------

my_car = Car(owner = "Nathan", number_of_wheels=4, number_of_seats=2, brand="BMW", engine=116)

# -------------------------------------------------------------------

print("\n\n"+"="*15+"Convention protected"+"="*15)
print(f"Convention protected attribute : {my_car._engine_oil}")
print(f"Convention protected method :")
my_car._compressing_oil()

# -------------------------------------------------------------------

print("\n\n"+"="*15+"Protected"+"="*15)
try :
    print(f"Private attribute : {my_car.__engine_candle}")
except Exception as e:
    print(f"Error catched ! : {e}")

try :
    my_car.__lighting_up()
except Exception as e:
    print(f"Error catched ! : {e}")

# -------------------------------------------------------------------

print("\n\n"+"="*15+"Getters"+"="*15)
print(my_car.accessing_private_attribute())
my_car.accessing_private_method()
