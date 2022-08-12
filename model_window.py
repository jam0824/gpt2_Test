import tkinter as tk
import gpt2
import make_hard_prompt
import sys
import model_coefont

class ModelWindow:
    root = None
    canvas = None
    img = []
    image_count = 0
    voice_main_key = 'c28adf78-d67d-4588-a9a5-970a76ca6b07'
    voice_sub_key = 'f95d6c31-4ffa-4222-a261-7c8ed7213441'

    def make_window(self, width, height):
        self.coefont = model_coefont.ModelCoeFont()
        self.width = width
        self.height = height
        self.root=tk.Tk()
        self.root.config(bg="snow")
        self.root.attributes("-transparentcolor", "snow")
        self.root.overrideredirect(1)
        w = self.root.winfo_screenwidth()
        h = self.root.winfo_screenheight()
        self.root.geometry(
            str(self.width) + 'x' + str(self.height) + '+' + 
            str(w - width) + '+' + 
            str(h-height -40)
            )

        self.canvas = tk.Canvas(
            master=self.root, 
            background="snow", 
            width=width, 
            height=width, 
            bd=0, 
            highlightthickness=0, 
            relief=tk.FLAT
            )
        self.canvas.place(x=0, y=0)
        self.canvas.bind("<Button-1>", self.btn_clicked)
        #self.canvas.bind("<Expose>", self.load_gpt2)

        

    def display_exit_button(self, pos_x, pos_y):
        self.btn = tk.Button(self.root, text='終了')
        self.btn.place(x=pos_x, y=pos_y)
        self.btn.bind("<Button-1>", self.btn_exit)

    def btn_exit(self, e):
        print("exit")
        sys.exit()



    #imgが描画されるタイミングはmainloopが呼ばれた時。なのでimgを保持しておく必要がある。よってglobal
    def display_image(self, image_path, width, height, pos_x, pos_y):
        self.img.append(
            tk.PhotoImage(file=image_path, width=width, height=height)
        )
        self.canvas.create_image(
            pos_x, 
            pos_y, 
            image=self.img[self.image_count], 
            anchor=tk.NW
        ) 
        self.image_count += 1


    def btn_clicked(self, e):
        print("clicked")
        tag = make_hard_prompt.MakeHardPrompt().get_tag()
        self.display_message(tag + "についての話です", 240, 260)
        self.root.after(100, self.load_gpt2, tag)

    
    def display_message(self, text, pos_x, pos_y):
        label=tk.Label(
            master=self.root,
            text=text,
            foreground="black",
            background="#F5EFEB",
            wraplength=280, 
            justify=tk.LEFT,
            width=40,
            height=4,
            anchor=tk.NW
            )
        label.place(x=pos_x,y=pos_y)



    def display_window(self):
        self.root.mainloop()

    def load_gpt2(self, tag):
        prefix = make_hard_prompt.MakeHardPrompt().get_hard_prompt(tag)
        #print(prefix)
        gpt = gpt2.GetSentence()
        response = gpt.get_sentence(prefix)
        self.message = gpt.get_message(response[0])
        self.len_message = 0
        print(self.message)
        self.message_controller()

    def message_controller(self):
        if self.len_message % 2 == 0:
            text = self.message[self.len_message]
            self.display_message(text, 200, 520)
            self.root.after(100, self.play_voice, text, self.voice_sub_key)
        else:
            text = self.message[self.len_message]
            self.display_message(text, 240, 260)
            self.root.after(100, self.play_voice, text, self.voice_main_key)
        self.len_message += 1
        if self.len_message < len(self.message):
            self.root.after(5000, self.message_controller)

    def play_voice(self, text, key):
        self.coefont.play(text, key)

