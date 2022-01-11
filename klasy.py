# class Car:
#    def __init__(self, make, model_name, top_speed, color):
#        self.make = make
#        self.model_name = model_name
#        self.top_speed = top_speed
#        self.color = color

#     # def __str__(self):
#     #     return f'{self.color} {self.make} {self.model_name}'
   

# mustang = Car(make="Ford", model_name="Mustang", color="Yellow", top_speed=250)
# print(mustang.make)

# car_one = Car(make="Ford", model_name="Mustang", top_speed=250, color="Red")
# car_two = Car(make="Ford", model_name="Mustang", top_speed=250, color="Red")
# car_one == car_two

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


def make_a():
  print("A")

def make_b():
  print("B")

def make_c():
  print("C")

def problem():
  print("no valid option defined")

options = { 0: make_a, 1: make_b, 2: make_c }
option = int(input())
options.get(option, problem)()
