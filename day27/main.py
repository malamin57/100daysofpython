import tkinter as tk

window = tk.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

#Lable 



my_lable = tk.Label(text = 'click me', font =("Arial", 24, "bold"), )
#my_lable.pack()
my_lable['text'] = "New Text"
my_lable.config(text='New Text')
my_lable.grid(column=5,row =2 )

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_lable.config(text = "Button Got Clicked")


button = tk.Button(text="click me ", command=button_clicked)
button.grid(column= 7, row = 3)


input = tk.Entry(width= 10 )

print(input.get())





window.mainloop()