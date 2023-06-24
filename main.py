from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    passwordn = ''.join(password_list)
    pass_text.insert(0, passwordn)
    pyperclip.copy(passwordn)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = web_text.get()
    email=email_text.get()
    pasword = pass_text.get()

    if len(web)==0 or len(pasword)==0:
        messagebox.showinfo(title='oops', message='Please donot left any blank')

    else:
        ok = messagebox.askokcancel(title='Titile', message=f'your website: {web}\n'
                                                            f'your email: {email}\n'
                                                            f'your password: {pasword} \n'
                                                            f'is it ok?')
        if ok:
            with open('file.txt', 'a') as file:
                file.write(f"{web} | {email} | {pasword} \n")
                web_text.delete(0, END)
                pass_text.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #



window = Tk()
window.title('Password genereator')
window.config(pady=50,padx=50)

canvas = Canvas(width=200,height=200)
imag = PhotoImage(file='logo.png')
canvas.create_image(100,100, image = imag )
canvas.grid(column=1,row=0)



web_lable = Label(text='Website')
web_lable.grid(column=0,row=1)
email_lable = Label(text='Email/Username')
email_lable.grid(column=0,row=2)
pass_lable = Label(text='Password')
pass_lable.grid(column=0,row=3)


web_text = Entry(width=35)
web_text.grid(row=1,column=1,columnspan=2)
web_text.focus()
email_text = Entry(width=35)
email_text.grid(row=2,column=1,columnspan=2)
email_text.insert(0,'usha@gmail.com')
pass_text = Entry(width=21)
pass_text.grid(row=3,column=1)


gen_lable = Button(text='Generate password', command=generate_password)
gen_lable.grid(row=3,column=2)
add = Button(text='Add',width=35,command=save)
add.grid(row=4,column=1,columnspan=2)





window.mainloop()