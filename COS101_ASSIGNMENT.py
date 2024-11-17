def a():
    print("Enter the displacement:")
    displacement = float(input())
    print("Enter the time taken:")
    time = float(input())
    print(f"The speed is {displacement / time} m/s")
def b():
    print("Enter the mass of the object:")
    mass = float(input())
    print("Enter the volume of the object:")
    volume = float(input())
    print(f"The density is {mass * volume}kg/cm3")

def c():
    print('Enter the distance:')
    distance = float(input())
    print('Enter the force:')
    force = float(input())
    print(f"The workdone is {distance * force} Joules")

def d():
    print('Enter the current of the circuit:')
    current = float(input())
    print('Enter the total resistance of the circuit:')
    resistance = float(input())
    print(f"The voltage of the entire circuit is {current * resistance} Volts.")

def e():
    print("Enter the mass of the object:")
    mass = float(input())
    print("Enter the acceleration of the object:")
    acceleration = float(input())
    print(f"The force of the object is {mass * acceleration} Newtons.")
print("This is a program designed to calculate Physics operations")
print("Choose an option from the menu below:")
print("A) Speed")
print("B) Density")
print("C) Work Done")
print("D) Voltage")
print("E) Force")
userInput = input().upper()
if userInput == "A":
    a()
elif userInput == "B":
    b()
elif userInput == "C":
    c()
elif userInput == "D":
    d()
elif userInput == "E":
    e()
else:
    print("Invalid input. Enter from an option A-E")
