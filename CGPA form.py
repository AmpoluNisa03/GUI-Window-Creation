import tkinter
from tkinter import messagebox, CENTER

window =tkinter.Tk()
window.title("CGPA Form for 2nd years")
window.geometry("400x600")

tkinter.Label(window, text="Enter the details\n").pack()
tkinter.Label(window, text="Name of the Student").pack()
tkinter.Entry(window).pack()

tkinter.Label(window, text="\nEmail Id").pack()
tkinter.Entry(window).pack()

tkinter.Label(window, text="\nBranch").pack()
tkinter.Entry(window).pack()

tkinter.Label(window, text="\nSection").pack()
tkinter.Entry(window).pack()

tkinter.Label(window, text="\nSEM3 GPA").pack()
tkinter.Entry(window).pack()

tkinter.Label(window, text="\nAverage CGPA(SEM1+SEM2+SEM3)").pack()
tkinter.Entry(window).pack()

def regbutton():
    messagebox.showinfo('Message box','Submission successful')
btn = tkinter.Button(window, text="Submit",bg="blue",fg="white",command=regbutton)
btn.pack(side='bottom')

window.mainloop()
