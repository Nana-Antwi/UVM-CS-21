#Nana Antwi
#CS 21
#Assignment 7
#kinetic.py

#design a program accepts mass and velocity as inputs and returns the kinetic energy


#declare variables 
mass = 0.0
velocity = 0.0
KE = 0.0
    
# define main function
def main():
    #exception loop statments
    try:

        #declare varaible constants
        ke_multiplyer = 1/2

        #user prompt input statements
        mass = float(input("Enter objects mass in kilograms: "))
        velocity = float(input("Enter object's velocity in meters: "))

        #computation for kinetic energy
        kinetic_energy = calc_kinetic_energy(ke_multiplyer, mass, velocity)
        print("The object has: ",format(kinetic_energy,'.2f'))
    except ValueError:
        print("Invalid entry, try again!")
    except:
        print("Program error re run")
        
#re validation of function and display results
def calc_kinetic_energy(ke_multiplyer, mass, velocity):
    kinetic_energy = ke_multiplyer * ((mass * velocity)**2)
    return kinetic_energy

#recall main function
main()
