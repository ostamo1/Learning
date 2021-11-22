#learning classes syntax and usage within python

class Bike:
    def __init__(self,colour,frame_masterial):
        self.colour = colour
        self.frame_material = frame_masterial
    def brake(self):
        print("braking!")
    



red_bike = Bike('Red','Carbon fiber')
blue_bike = Bike('Blue','Steel')


print(red_bike.colour)
print(red_bike.frame_material)

print(blue_bike.colour)
print(blue_bike.frame_material)

red_bike.brake()


