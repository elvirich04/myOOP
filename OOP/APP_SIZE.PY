import tkinter
class Application(tkinter.Frame):
    def __init__ (self,master):
        tkinter.Frame.__init__(self,master)
        self.config(width=1000)
        self.config(height=200)
        self.config(bg="#9933CC")
        self.pack()
        self.CreateWidgets()
    def CreateWidgets(self):
        pass
root=tkinter.Tk()
app=Application(master=root)
app.mainloop()
root.destroy()
