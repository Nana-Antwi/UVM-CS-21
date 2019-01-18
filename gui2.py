#Nana Antwi
#CS 21 
#assignment 11
#mpg.py

#Design a gui program that calculates mpg from user input.

#import from python library
import tkinter

#call class
class MPG:

    #define init function
    def __init__(self):
        # create main window
        self.main_window = tkinter.Tk()

        # create four frames for varibles
        self.gallons_frame = tkinter.Frame(self.main_window)
        self.miles_frame = tkinter.Frame(self.main_window)
        self.milespergallon_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        #widgets and pack for gallons
        self.gallons_label = tkinter.Label(self.gallons_frame, \
                                       text='Enter the amount of gallons used: ')
        self.gallons_entry = tkinter.Entry(self.gallons_frame, \
                                       width=10)
        self.gallons_label.pack(side='left')
        self.gallons_entry.pack(side='left')

        #widgets and pack for miles
        self.miles_label = tkinter.Label(self.miles_frame, \
                                           text='Enter the number of miles: ')
        self.miles_entry = tkinter.Entry(self.miles_frame, \
                                           width=10)
        self.miles_label.pack(side='left')
        self.miles_entry.pack(side='left')

        #widgets and pack for the results display
        self.result_label = tkinter.Label(self.milespergallon_frame, \
                                       text='Miles per gallon is:')
        self.mpg = tkinter.StringVar() 
        self.mpg_label = tkinter.Label(self.milespergallon_frame, \
                                       textvariable=self.mpg)
        self.result_label.pack(side='left')
        self.mpg_label.pack(side='left')

        #widgets and pack for button
        self.calc_button = tkinter.Button(self.button_frame, \
                                          text='Calculate MPG', \
                                          command=self.calc_mpg)
        self.quit_button = tkinter.Button(self.button_frame, \
                                          text='Quit', \
                                          command=self.main_window.destroy)
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        #pack frames containign all widgets
        self.gallons_frame.pack()
        self.miles_frame.pack()
        self.milespergallon_frame.pack()
        self.button_frame.pack()

    #define calculation function 
    def calc_mpg(self):

        #assing varaibles to get input 
        self.gallons = float(self.gallons_entry.get())
        self.miles = float(self.miles_entry.get())

        #calculate  MPG
        self.miles_per_gallon = self.miles / self.gallons

        #update results to variable display
        self.mpg.set(self.miles_per_gallon)

carmpg = MPG()