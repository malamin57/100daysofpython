from tkinter import * 
from tkinter import messagebox
from  random import choice, randint, shuffle
import pyperclip 
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_list = []

    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


   
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
            website: {
                    "email": email,
                    "password": password
            }
    }

    
    if len(website) == 0 or len(email) == 0 or len(password) == 0 :
        messagebox.showinfo(title="Opps", message=" Enter a value")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are details entered: \nEmail: {email}"
                                  f"\Password: {password} \n Is it ok to save?")
        try:
            with open("data.json", "r") as data_file:
                #reading old data 
                data = json.load(data_file)
                #updateing old data with new data
               # data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
             
        else:
            with open("data.json", "w") as data_file:
                #saving updated data
                json.dump(new_data, data_file, indent=4)
        finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
      


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height= 200, width=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_lable = Label(text='Website')
website_lable.grid(row=1)
email_label = Label(text='Email/username')
email_label.grid(row=2)
password_label = Label(text="password")
password_label.grid(row=3)

#entries 
website_entry = Entry(width = 35)
website_entry.grid(row = 1, column = 1, columnspan=2)
website_value = website_entry.get()
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, 'example@gmail.com')
password_entry = Entry(width=21)
password_entry.grid(row=3, column= 1)

#Button
generate_password_button = Button(text = 'Generate Password', command = generate_password)
generate_password_button.grid(row= 3 , column = 2)
add_button = Radiobutton(text = "Add", command = save)
add_button.grid(row=4, column=1)

#file 

print(website_value)
'''
data_file =open('data.txt', 'w')
data_file(password_entry)
data_file.close()
'''

window.mainloop()





