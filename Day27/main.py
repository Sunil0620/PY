import tkinter as tk

root = tk.Tk()
root.title("My First GUI Program")
root.minsize(500, 300)

# Label
my_label = tk.Label(text="i am labor",font=("Arial",23,"bold"))
my_label.pack(side="bottom")





tk.mainloop()
