import tkinter as tk

window = tk.Tk()
window.title('Form')
window.geometry("600x800")
window.resizable(False, False)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=3)


first_name = tk.StringVar()


label01 = tk.Label(window, text="Register", font='Verdana 16 bold')
label01.grid(row=0, column=0, sticky='we', columnspan=2)

label02 = tk.Label(window, text='First name')
label02.grid(row=1, column=0)

entry01 = tk.Entry(window, textvariable=first_name)
entry01.grid(row=1, column=1, sticky='ew')


window.mainloop()
