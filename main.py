import tkinter as tk
from time import strftime
def update_time():
    clock=strftime("%H:%M:%S")
    clock_label.config(text=clock)
    clock_label.after(1000,update_time)
root=tk.Tk()
root.title("TahaTavana")
root.geometry('300x150')
clock_label=tk.Label(root,font=('aviny',50,'bold'),fg='red')
clock_label.pack(fill="both",expand=True)
update_time()
root.mainloop()
