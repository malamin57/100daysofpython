import tkinter as tk

window = tk.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

label_1 = tk.Label(text = 'is equal to', font =("Arial", 24, "bold"), )
label_1.grid(column=1, row= 2)

input = tk.Entry(width = 10 )
value = int(input)

def convert(a):
     km = a * 1.6 
     return km
     
lable_2 = tk.Label(text = "value", font =("Arial", 24, "bold") ) 
lable_2.grid(column=2,row=2)

button = tk.Button(text="calculate ", command=convert(value))
button.grid(column=2, row = 3 )

