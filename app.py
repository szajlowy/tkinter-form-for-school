import tkinter as tk

window = tk.Tk()
window.title('Form')
window.geometry("600x800")
window.resizable(False, False)


label01 = tk.Label(window, text="Register", font='Verdana 16 bold')
label01.grid(row=0, column=0, sticky='ew')
window.grid_columnconfigure(0, weight=1)


window.mainloop()
