import tkinter as tk

def btn_clicked(e):
	print("clicked")

root=tk.Tk()
root.config(bg="snow")
root.attributes("-transparentcolor", "snow")
#root.wm_attributes("-transparentcolor", "snow")
#root.overrideredirect(1)
#root.attributes("-alpha",0.5)#
#ttk.Style().configure("TP.TFrame", background="snow")
#f=ttk.Frame(master=root,style="TP.TFrame",width=800,height=600, relief=tkinter.FLAT)
#f.pack()

w = root.winfo_screenwidth()
h = root.winfo_screenheight()
root.geometry('800x600+' + str(w -800) + '+' + str(h-670))



canvas = tk.Canvas(master=root, background="snow", width=800, height=600, bd=0, highlightthickness=0, relief=tk.FLAT)
canvas.place(x=0, y=0)
canvas.bind("<Button-1>", btn_clicked)
img = tk.PhotoImage(file="surface0000.png", width=300, height=400)
canvas.create_image(500, 200, image=img, anchor=tk.NW)
img2 = tk.PhotoImage(file="surface0010.png", width=300, height=400)
canvas.create_image(100, 320, image=img2, anchor=tk.NW)

label=tk.Label(master=root,text="薄くならないで…",foreground="black",background="snow")
label.place(x=150,y=150)


root.mainloop()