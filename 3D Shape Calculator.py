#If and Else Statements 1.3 - Ex 23

#Rectangular Prism
prism_l = float(input("Rectangular Prism\nEnter the length: "))
prism_w = float(input("Enter the width: "))
prism_h = float(input("Enter the height: "))

prism_volume = prism_h*prism_l*prism_w

print("The volume is:", prism_volume)

#Sphere
sphere_radius = float(input("Sphere\nEnter the radius: "))
sphere_volume = (((sphere_radius*2)**3)*3.14159)/6
print("The volume is:", sphere_volume)

#Cube
cube_sides = float(input("Cube\nEnter the length of each side: "))
cube_volume = cube_sides**3
print("The voume is:", cube_volume)
