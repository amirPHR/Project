import os 
import tkinter as tk 

app = tk.Tk()
app.geometry('500x300')
app.title('Shutdown system')

#Label 
label = tk.Label(text = 'Do you want Shutdown your system? ')
label.pack()

#Function 
def system_yes():
    label.configure(os.system('shutdown /s /t 0'))

def system_no():
    label.configure(print('Your system not shut down'))

#Button 
b1 = tk.Button(text = 'Yes' , width = 15 , command = system_yes)
b1.pack()

b2 = tk.Button(text = 'No' , width = 15 , command = system_no)
b2.pack()


app.mainloop()