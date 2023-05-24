from rich.console import Console 
from rich.panel import Panel 
console = Console()

class Vehicle1():
    #Here is where the attributes start
    colour = 'White'
    speed = 80 
    windows = 'up'
    name = 'volvo'
    #This is to print the title with art 
    def __init__(self):
        console.print(
            Panel.fit(" --  Arturo's program  --  ", style = "bold purple", subtitle="By Arturo Montiel")
        )
    #This is to lower ythe windows in the car
    def lower_windows(self):
        print('Lowering windows on all doors')
        print('Windows down')
    # This is to raise the windows 
    def raise_windows(self):
        print('Raising windows on all doors')
        print('Windows up')
    #Acccelrate by taking the information of speed and storing it so all the methods can use that info
    def accelerate (self):
        self.speed = self.speed + 15 
        print(f"Your courrent velocity is {self.speed} mph")
        
    # Breakes and saves the information of the speed so the different methods may use it
    def break_speed(self):
        self.speed = self.speed - 15 
        print(f"Your courrent velocity is {self.speed} mph")
        return self.speed
        
#We create the object and give it special attributes based on the attribute of the class
car1 = Vehicle1()
car1.colour = 'red'
car1.speed = 100
car1.windows = 'up'
car1.name = 'Arturo Movil'
#Print the new attributes of the car
print(f"The car {car1.name} is ready to leave")
print(f"{car1.name} is color {car1.colour}")
print(f"The {car1.name} speed is {car1.speed}")
print (f"{car1.name} windows are {car1.windows}")


#Define the variable that will run the while loop
keep_running = "y"  
#Initialize the while loop 
while keep_running == "y":
    #Get the input from the user 
    print("What do you want to do with your car?")
    decision = input("(A)ccelerate ; (B)reake ; (L)ower windows ; (R)aise windows ; (Enter) not play anymore : ")
    #Create an if statement based on the input from the user and using the methods from the class.
    if decision == "L": 
        car1.lower_windows()

    elif decision == "R":
        car1.raise_windows()

    elif decision == "A":
        car1.accelerate()

    elif decision == "B":
        car1.break_speed()
    
    elif decision == "":
        break
    
   