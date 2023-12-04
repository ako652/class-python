




class employees:
    def __init__(self, name,age) :
        self.name=name
        self.age=age
     
    def description(self):
        return f'my name is {self.name} and i am {self.age} old'
    def noise(self,sound):
        return f'my name is {self.name} i can hear {sound} properly '
john=employees('john',30,)
print(john.name)
print(john.noise('sound'))
print(john.description())



class car:
    def __init__(self, color,mileage):
        self.color=color
        self.mileage=mileage
    def __str__(self) :
        return f'the {self.color} car has {self.mileage} miles'
    
blue_car=car(color='blue',mileage=20000)
red_car=car(color='red',mileage= 30000)

for car in (blue_car, red_car):
    print(car)

