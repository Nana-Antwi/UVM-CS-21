#import from library
import tkinter


#varaibles
v =""
 
class Application(Frame):
 
    def __init__(self,master):
 
        Frame. __init__(self,master)
        self.grid()
        self.create_widgets()
 
    def create_widgets(self):
 
        v = IntVar()
 
        self.button1 = Radiobutton(self,
                             text="Convert To Fahrenheit.",
                             variable=v,value=1,
                             ).grid(row=0,column=0,sticky=W)
        self.button2 = Radiobutton(self,
                             text="Convert To Celcius.",
                             variable=v,value=2,
                             ).grid(row=1,column=0,sticky=W)
 
        self.text = Entry(self,
                          ).grid(row=2,column=0,sticky=W)
 
        self.finish_button = Button(self,
                                    text="Calculate.",command=self.calculate,
                                    ).grid(row=3,column=0,sticky=W)
    def calculate(self):
 
        if v == 1:
            temp = float(self.text.get())
            message = (9/5)*(temp)+(32)
        else:
            temp = float(self.text.get())
            message = (5/9)*(temp)-(160/9)
        
        self.text.delete(0.0,END)
        self.text.insert(0.0,message)
        
        
                    
 
        
root = Tk()
root.title("Temp Converter.")
root.geometry("300x200")
 
app = Application(root)
root.mainloop()
 