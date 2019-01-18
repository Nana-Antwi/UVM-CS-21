#GUI
#assignment 11

#Design a program that calculates mpg from user input.

#import dictionary
import tkinter


class MPG:

#define main function
	def __init__(self):


		#create main window 
		self.main_window = tkinter.Tk()

		#create frames 
		self.milespergallon_frame = tkinter.Frame(self.main_window)
		self.miles_frame = tkinter.Frame(self.main_window)
		self.gallons_frame = tkinter.Frame(self.main_window)
		self.button_frame = tkinter.Frame(self.main_window)


		#create widgets for variables 
		#widget and pack for miles 
		self.miles_label = tkinter.Label(self.miles_frame, \
		 text="Enter the number of miles travelled: ")
		self.miles_entry = tkinter.Entry(self.miles_frame, \
			width = 10)
		self.miles_label.pack(side='left')
		self.miles_entry.pack(side='left')


		#widget and pack for gallons
		self.gallons_label = tkinter.Label(self.gallons_frame, \
			text="Enter the amount of gallons used: ")
		self.gallons_entry = tkinter.Entry(self.gallons_frame, \
			width= 10)
		self.gallons_label.pack(side='left')
		self.gallons_entry.pack(side='left')

		#widget and pack for avarage
		self.result_label = tkinter.Label(self.milespergallon_frame, \
			text="Miles per gallon is:")
		self.milespergallon = tkinter.StringVar()
		self.milespergallon_label = tkinter.Label(self.milespergallon_frame, \
			textvariable=self.milespergallon)
		self.result_label.pack(side='left')
		self.milespergallon_label.pack(side='left')

		#widget and pack for button
		self.calc_button = tkinter.Button(self.button_frame, \
			text="Calculate MPG", \
			command=self.calc_milespergallon)
		self.quit_button = tkinter.Button(self.button_frame, \
			text="Quit", \
			command=self.main_window.destroy)
		self.calc_button.pack(side='left')
		self.quit_button.pack(side='left')


		#pack frames containing widgets 
		self.milespergallon_frame.pack()
		self.miles_frame.pack()
		self.gallons_frame.pack()
		self.button_frame.pack()


		#mpg calculation function 
		def calc_milespergallon(self):

			#user prompt input
			self.gallons = float(self.gallons_entry.get())
			self.miles = float(self.miles_entry.get())

			#mpg calculation
			self.mpg = (self.miles / self.gallons)

			#widget update
			self.milespergallon.set(self.mpg)

#re call main function
carmpg = MPG()


