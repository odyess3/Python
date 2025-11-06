class User:
    

    def __init__(self):
        print("new user is made...")

user1 = User()
user1.id = "001"
user1.username = "ody"

print(user1.username)



class Car:
    def __init__(self, seats, car_id):
        self.seats = seats
        self.id = car_id
        self.wheels = 4



car1 = Car("5", "2334")

print(car1.wheels)


class MoterBike:
    def __init__(self, name):
        self.wheels = 2
        self.speed = 0
        self.name = name
    
    def racemode(self, speed):
       self.speed += speed


moter1 = MoterBike("yazzer")

moter1.racemode(20)

print(moter1.speed)