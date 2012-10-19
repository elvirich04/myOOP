import tkinter
points=0
response=tkinter.messagebox.askyesno("Q.1","Answer: Yes")
if (response==True):
    points+=1
response=tkinter.messagebox.askyesno("Q.2","Answer: Yes")
if (response==True):
    points+=1
response=tkinter.messagebox.askyesno("Q.3","Answer: Yes")
if (response==True):
    points+=1
tkinter.messagebox.showinfo("Results","Total points is %i"%(points))
