class Car:

    def __init__(self ):
        self.color = None
        self.motor = None

    def run(self):
        print(f"Une voiture {self.color} roule. Elle a un moteur {self.motor}.")


class CarFactory:

    def create_tesla() -> Car :
        car = Car()
        car.color ="Blanc"
        car.motor = "Electric"
        return car

    def create_police_car() -> Car :
        car = Car()
        car.motor = "Diesel"
        car.color= "Bleu"
        return car

    
# Execution
police_car = CarFactory.create_police_car()
police_car.run()

tesla = CarFactory.create_tesla()
tesla.run()