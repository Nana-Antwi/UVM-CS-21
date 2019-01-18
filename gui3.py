#import
#main function
import tkinter
def main():
    root=Tk()

    root.title("Some GUI")
    root.geometry("400x700")
    #someothersting=""
    someotherstring=0
#enter Celcius
    L1=Label(root,text="Enter a Celcius temperature.")
    E1=Entry(root,textvariable=someotherstring)
    somebutton=Button(root, text="Total", command=convert(someotherstring))

    somebutton.pack()
    E1.pack()
    L1.pack()
    root.mainloop()#main loop


#convert Celcius to Fahrenheit
def convert(somestring):
    thestring=""
    thestring=somestring
    cel=0
    far=0
    cel=int(thestring)
    far=(9/5*(cel))+32
    print(far)
