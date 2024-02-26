class Dog(object):

  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def add_age(self, num):
    self.age += num

doggo = Dog('Cutie', 5)

print(doggo.name) 
print(doggo.age)

doggo.add_age(4)
print(doggo.age)