import tkinter as tk

window = tk.Tk()
window.title('Form')
window.geometry("600x800")
window.resizable(False, False)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=3)


first_name = tk.StringVar()
last_name = tk.StringVar()
gender = tk.StringVar(value='M')


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

radio04 = tk.Radiobutton(window, text='Other', variable=gender, value='E')
radio04.grid(row=6, column=1, sticky='w')


window.mainloop()
