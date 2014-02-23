class vehicle:
    def __init__(self,speed):
        self.speed=speed

    def drive(self,distance):
        print('need %f hours'%(distance/self.speed))

class bike(vehicle):
    pass

class car(vehicle):
    def __init__(self,speed,fuel):
        vehicle.__init__(self,speed)
        self.fuel=fuel

    def drive(self,distance):
        vehicle.drive(self,distance)
        print('need %f fuels'%(distance*self.fuel))

b=bike(15.0)
c=car(80.0,0.012)
b.drive(100.0)
c.drive(100.0)
