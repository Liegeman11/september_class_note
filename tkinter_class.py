from tkinter import *

window=Tk()
window.title('My First Tkinter App')
window.geometry("850x600")
icon=PhotoImage(file='C:\SeptemberCohort\Images\download (1).png')
window.iconphoto(TRUE,icon)
window.config(background="green")
label=Label(window,text='Hello World!',font=('aerial', 20, 'bold'), fg='red', bg='black')
# label.pack()
# label.place(x=0, y=50)
def click():
    label.pack()
button = Button(window,text=('Click Me!'))
button.config(activebackground="#FFF000")
button.config(activeforeground="#ff0000")
# button.config(image=image)
button.place(x=0,y=10)
window.mainloop()