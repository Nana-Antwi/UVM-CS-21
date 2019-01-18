#Nana Antwi
#CS 21
#assignment 11
#temps.py

#design a gui program that accepts celsius temperature and convert into fahrenheit

#import python library
import tkinter

#call class
class CelsiusConverterGUI:

	#define function
	def __init__(self):

		#create the main window
		self.main_window = tkinter.Tk()

		#create frames to group widgets 
		self.top_frame = tkinter.Frame()
		self.mid_frame = tkinter.Frame()
		self.button_frame = tkinter.Frame()

		#widgets and pack celsius
		self.prompt_label = tkinter.Label(self.top_frame, \
			text="Enter the Celsius temperature: ")
		self.cel_entry = tkinter.Entry(self.top_frame, \
			width=10)
		self.prompt_label.pack(side='left')
		self.cel_entry.pack(side='left')

		#widgets and pack for average
		self.result_label = tkinter.Label(self.mid_frame, \
			text="Converted to fahrenheit: ")
		self.value = tkinter.StringVar()
		self.fahrenheit_label = tkinter.Label(self.mid_frame,\
			textvariable=self.value)
		self.result_label.pack(side='left')
		self.fahrenheit_label.pack(side='left')

		#widgets and pack for button
		self.calc_button = tkinter.Button(self.button_frame, \
			text='Convert',\
			command=self.convert)
		self.quit_button = tkinter.Button(self.button_frame,\
			text='Quit',\
			command=self.main_window.destroy)
		self.calc_button.pack(side='left')
		self.quit_button.pack(side='left')

		#pack all buttons 
		self.top_frame.pack()
		self.mid_frame.pack()
		self.button_frame.pack()

		#enter the thinter loop
		tkinter.mainloop()

		#define convert function for calculations
	def convert(self):

		#varaiable to hold entry
		cel = float(self.cel_entry.get())


		#calcution of fahrenheit
		fah = (9/5) * cel + 32

		#update cel widget
		self.value.set(fah)

			#create instance for class
Celsius_conv = CelsiusConverterGUI()
