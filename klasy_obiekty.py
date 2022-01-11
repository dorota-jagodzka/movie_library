class Car:

   def __init__(self, make, model_name, top_speed, color):
       self.make = make
       self.model_name = model_name
       self.top_speed = top_speed
       self.color = color

       # Variables
       self.current_speed = 0

   def accelerate(self, step=10):
       self.current_speed += step

   def decelerate(self, step=10):
       self.current_speed -= step

car = Car(make="Ford", model_name="Mustang", top_speed=250, color="Red")
car.current_speed

print(car)
print(car.current_speed)

car.accelerate()
car.current_speed

print(car.current_speed)

car.accelerate(20)
car.current_speed

print(car.current_speed)

