import tkinter as tk 

#Calculator
Calculator = tk.Tk()
Calculator.title('Calculator')
Calculator.geometry('500x300')

#Label
label = tk.Label(text='Calculator')
label.pack()

#Entry
entry1 = tk.Entry()
entry1.pack()
entry2 = tk.Entry()
entry2.pack()

#commands
def jam():
    label.configure(text = int(entry1.get()) + int(entry2.get()))

def tafrigh():
    label.configure(text = int(entry1.get()) - int(entry2.get()))
def zarb():
    label.configure(text = int(entry1.get()) * int(entry2.get()))
def taghsim():
    label.configure(text = int(entry1.get()) / int(entry2.get()))

#Buttons 
b1 = tk.Button(width = 20, text = '+', command = jam, bg = 'blue')
b1.pack()

b2 = tk.Button(width = 20, text = '-', command = tafrigh)
b2.pack()

b3 = tk.Button(width = 20, text = 'x', command = zarb)
b3.pack()

b4 = tk.Button(width = 20, text = '/', command = taghsim)
b4.pack()

Calculator.mainloop()