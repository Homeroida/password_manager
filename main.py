from tkinter import *
from tkinter import messagebox
from random import *
import json

import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def random_passwords():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # random_password = []
    #
    # for letter in range(1, randint(3, 9)):
    #     random_password.append(letters[randint(0, 51)])
    #
    # for number in range(1, randint(3, 9)):
    #     random_password.append(numbers[randint(0, 9)])
    #
    # for symbol in range(1, randint(3, 9)):
    #     random_password.append(symbols[randint(0, 8)])
    #
    # shuffle(random_password)
    # new_random = ''.join(random_password)
    # entry_password.delete(0, END)
    # entry_password.insert(0, new_random)

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = ''.join(password_list)
    entry_password.delete(0, END)
    entry_password.insert(0, password)

    pyperclip.copy(password)

# ---------------------------- SEARCH BUTTON ------------------------------- #

def search():
    file_search = entry_website.get().capitalize()
    try:
        with open("data_file.json", mode="r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")

    else:
        if file_search in data:
            email = data[file_search]["email"]
            password = data[file_search]["password"]
            messagebox.showinfo(title=f"info {file_search}", message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {file_search} exists.")







# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    website = entry_website.get().capitalize()
    email = entry_username.get()
    password = entry_password.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data_file.json", mode="r") as data_file:
                # reading old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data_file.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data_file.json", mode="w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)

        finally:
            entry_website.delete(0, END)
            entry_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.configure(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

label_name = Label(text="Website:", padx=10)
label_name.grid(column=0, row=1)

label_username = Label(text="Email/Username:", padx=10)
label_username.grid(column=0, row=2)

label_password = Label(text="Password: ")
label_password.grid(column=0, row=3)

entry_website = Entry()
entry_website.place(width=180, height=22, x=114, y=200)

entry_username = Entry(width=50)
entry_username.grid(column=1, row=2, columnspan=2)

entry_password = Entry(width=23)
entry_password.place(width=180, height=22, x=114, y=249)

button_gen_pass = Button(text="Generate Password", command=random_passwords)
button_gen_pass.place(width=120, x=297, y=248)

button_add = Button(text="Add", width=42, command=add)
button_add.place(width=305, x=110, y=280)

button_search = Button(text="Search", command= search)
button_search.place(width=120, x=297, y=199)


window.mainloop()
