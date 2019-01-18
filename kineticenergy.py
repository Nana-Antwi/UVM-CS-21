#Nana Antwi
#CS 21
#Assignment 7
#kineticenergy.py

#design a program that asccept mass and velocity as inputs and returns the kinetic energy

#declare varaibles
mass= 0.0
velocity = 0.0
KE = 0.0

#define function
def main():

	#exception statements
	try:


		#declare constants in the function
		kinetic_energy_multiplyer = 1/2

		#user prompt statments
		mass = float(input('Enter objects mass in kilograms: '))
		velocity = float(input('Enter objects velocity in meters:'))

		#computation of main function for results 
		kinetic_energy = result_ke(kinetic_energy_multiplyer, mass, velocity)
		print('kinetic energy :', format(kinetic_energy, '.2f'))


	except ValueError:
		print('Invalid entry! enter number greater than zero')
    except:
    	
                
        print('Program Error re-run')

	#define second function
def results_ke(kinetic_energy_multiplyer, mass, velocity):
	kinetic_energy = kinetic_energy_multiplyer * ((mass) * ((velocity)**2))
	return kinetic_energy

#recall function
main()

	
 

