import tkinter
root=tkinter.Tk()

tkinter.messagebox.showinfo("title","message",icon=tkinter.messagebox.QUESTION)
#icon=(either of the four below)
#tkinter.messagebox.ERROR
#tkinter.messagebox.INFO
#tkinter.messagebox.WARNING
#tkinter.messagebox.QUESTION
root.mainloop()
root.destroy()
