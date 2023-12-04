




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




class dog:
    def __init__(self, name,age,breed):
        self.name=name
        self.age=age
        self.breed=breed
    def __str__(self):
        return f'{self.name} is {self.age} old'
    def description(self,sound):
        return f'{self.name} says this {sound}'
    
mark=dog('mark', 23, 'hushpup')
miles=dog('miles', 34, 'jack russel terrier')
buddy=dog('buddy',45, 'dachsund')
jack=dog('jack',30, 'bulldog')
jim=dog('jim',30, 'bulldog')
print(mark.description('yuyuyu'))
print(mark.age)

class hushpup(dog):
    pass
class jackrussel(dog):
    pass

class dachsund(dog):
    pass
class bulldog(dog):
    pass

jim=hushpup('jim',30 , 'hush')
print(jim)
############################################################################################


class animal:
    species='canis familairis'
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f'{self.name} is {self.age} old'
    def speak(self,sound):
        return f'{self.name} says {sound}'
    
mouse=animal(name='mouse',age=20)
print(mouse)
second=mouse.speak('yuyu')
print(second)

class GoldenRetriever(animal):
    def speak(self, sound='bark'):
        return super().speak(sound)
    
    
mike=GoldenRetriever('mike',20)
print(mike.speak())
print(mike)