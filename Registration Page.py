import tkinter
from tkinter import messagebox, CENTER

window =tkinter.Tk()
window.title("Registration Page")
window.geometry("400x600")

tkinter.Label(window, text="Enter the details\n").pack()
tkinter.Label(window, text="Name of the Student").pack()
tkinter.Entry(window).pack()

tkinter.Label(window, text="\nEmail Id").pack()
tkinter.Entry(window).pack()

tkinter.Label(window, text="\nPasswords").pack()
tkinter.Entry(window).pack()

tkinter.Label(window, text="\nSection").pack()
tkinter.Entry(window).pack()

tkinter.Label(window, text="\nPhone Number").pack()
tkinter.Entry(window).pack()

def regbutton():
    messagebox.showinfo('Message box','Registration successful')
btn = tkinter.Button(window, text="Submit",bg="green",fg="black",command=regbutton)
btn.pack(side='right')

tkinter.Label(window, text="\nGender").pack()
var = tkinter.Invar()
R1 = tkinter.Radiobutton(window, text="Male",variable=var, value=0,)
R1.pack(anchor.CENTER)
R1 = tkinter.Radiobutton(window, text="Female",variable=var, value=1,)
R1.pack(anchor.CENTER)

window.mainloop()