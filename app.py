import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Form')
window.geometry("600x800")
window.resizable(False, False)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=3)


first_name = tk.StringVar()
last_name = tk.StringVar()
gender = tk.StringVar(value='M')
age = tk.IntVar
province = tk.StringVar()
check = tk.IntVar()


label01 = tk.Label(window, text="Register", font='Verdana 16 bold')
label01.grid(row=0, column=0, sticky='we', columnspan=2)

label02 = tk.Label(window, text='First name:')
label02.grid(row=1, column=0)

entry01 = tk.Entry(window, textvariable=first_name)
entry01.grid(row=1, column=1, sticky='ew', padx=(0, 10))

label03 = tk.Label(window, text='Last name:')
label03.grid(row=2, column=0)

entry02 = tk.Entry(window, textvariable=last_name)
entry02.grid(row=2, column=1, sticky='ew', padx=(0, 10))

label04 = tk.Label(window, text='Gender:')
label04.grid(row=3, column=0)

radio01 = tk.Radiobutton(window, text='Male', variable=gender, value='M')
radio01.grid(row=3, column=1, sticky='w')

radio02 = tk.Radiobutton(window, text='Female', variable=gender, value='F')
radio02.grid(row=4, column=1, sticky='w')

radio03 = tk.Radiobutton(window, text='Attack helicopter', variable=gender, value='A')
radio03.grid(row=5, column=1, sticky='w')

radio04 = tk.Radiobutton(window, text='Other', variable=gender, value='O')
radio04.grid(row=6, column=1, sticky='w')

label04 = tk.Label(window, text='Age:')
label04.grid(row=7, column=0)

scale01 = tk.Scale(window, from_=0, to=120, orient=tk.HORIZONTAL, variable=age)
scale01.grid(row=7, column=1, sticky='ew')

label05 = tk.Label(window, text='Province:')
label05.grid(row=8, column=0)

combobox01 = ttk.Combobox(window, textvariable=province)
combobox01['values'] = ('dolnośląskie', 'kujawsko-pomorskie', 'lubelskie', 'lubuskie', 'łódzkie', 'małopolskie', 'mazowieckie', 'opolskie', 'podkarpackie', 'podlaskie', 'pomorskie', 'śląskie', 'świętokrzyskie', 'warmińsko-mazurskie', 'wielkopolskie', 'zachodniopomorskie')
combobox01.grid(row=8, column=1, sticky='ew')

c01 = tk.Checkbutton(window, text='Accept the Terms of Service', variable=check)
c01.grid(row=9, column=0, columnspan=2)

btn01 = tk.Button(text='Submit')
btn01.grid(row=10, column=0, columnspan=2)

up = tk.PhotoImage(file='up.png')
label06 = tk.Label(
    master = window,
    image = up,
    width = 512,
    height = 512
)
label06.grid(row=11, column=0, columnspan=2)


window.mainloop()
