import tkinter as tk
import gpt2
import make_hard_prompt
import sys
import model_coefont
import softalk

class ModelWindow:
    root = None
    canvas = None
    img = []
    image_count = 0
    voice_main_key = 0
    voice_sub_key = 1
    wait_character_time = 200
    balloon_dict = {}
    marisa_dict = {}
    reimu_dict = {}

    def make_window(self, width, height):
        self.softalk = softalk.SofTalk()
        self.root=tk.Tk()
        self.root.config(bg="snow")
        self.root.attributes("-transparentcolor", "snow")
        self.root.overrideredirect(1)
        
        self.adjust_window(width, height, 40)
        self.add_canvas(width, height)
        #self.canvas.bind("<Expose>", self.load_gpt2)
    
    def adjust_window(self, width, height, taskbar_height):
        w = self.root.winfo_screenwidth()
        h = self.root.winfo_screenheight()
        self.root.geometry(
            str(width) + 'x' + str(height) + '+' + 
            str(w - width) + '+' + 
            str(h - height - taskbar_height)
            )


    def add_canvas(self, width, height):
        self.canvas = tk.Canvas(
            master=self.root, 
            background="snow", 
            width=width, 
            height=height, 
            bd=0, 
            highlightthickness=0, 
            relief=tk.FLAT
            )
        self.canvas.place(x=0, y=0)
        self.canvas.bind("<Button-1>", self.btn_clicked)

    def display_exit_button(self, pos_x, pos_y):
        self.btn = tk.Button(self.root, text='終了')
        self.btn.place(x=pos_x, y=pos_y)
        self.btn.bind("<Button-1>", self.btn_exit)

    def btn_exit(self, e):
        print("exit")
        sys.exit()

    def btn_clicked(self, e):
        print("clicked")
        tag = make_hard_prompt.MakeHardPrompt().get_tag()
        self.display_message(tag + "についての話です", 370, 410)
        self.root.after(100, self.load_gpt2, tag)


    def add_image(self, image_path, width, height):
        self.img.append(
            tk.PhotoImage(file=image_path, width=width, height=height)
        )
        return len(self.img) - 1

    #imgが描画されるタイミングはmainloopが呼ばれた時。なのでimgを保持しておく必要がある。よってglobal
    def display_image(self, image_no, pos_x, pos_y, tag):
        self.canvas.create_image(
            pos_x, 
            pos_y, 
            image=self.img[image_no], 
            tag=tag,
            anchor=tk.NW
        ) 
        return {'image_no':image_no, 'pos_x':pos_x, 'pos_y':pos_y, 'tag':tag,}

    def change_image(self, image_no, pos_x, pos_y, tag):
        self.canvas.delete(tag)
        return self.display_image(image_no, pos_x, pos_y, tag)

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


    def set_balloon_dict(self, balloon_left_no, balloon_right_no, balloon_dict):
        balloon_dict['balloon_left_no'] = balloon_left_no
        balloon_dict['balloon_right_no'] = balloon_right_no
        self.balloon_dict = balloon_dict

    def set_marisa_dict(self, marisa_0, marisa_1, marisa_dict):
        marisa_dict['image0'] = marisa_0
        marisa_dict['image1'] = marisa_1
        marisa_dict['increase'] = -1
        self.marisa_dict = marisa_dict

    def set_reimu_dict(self, reimu_0, reimu_1, reimu_dict):
        reimu_dict['image0'] = reimu_0
        reimu_dict['image1'] = reimu_1
        reimu_dict['increase'] = -1
        self.reimu_dict = reimu_dict

    def animation(self, image_dict, count):
        image_no = 0
        if count % 2 == 0:
            image_no = image_dict['image0']
        else:
            image_no = image_dict['image1']
        self.change_image(
            image_no,
            image_dict['pos_x'], 
            image_dict['pos_y'],
            image_dict['tag'])
        count -= 1
        if count > 0:
            self.root.after(self.wait_character_time, self.animation, image_dict, count)

    def fuwa_fuwa_animation(self):
        if self.reimu_dict['pos_y'] == 195:
            self.reimu_dict["increase"] = 1
            self.marisa_dict["increase"] = 1
        elif self.reimu_dict['pos_y'] == 205:
            self.reimu_dict["increase"] = -1
            self.marisa_dict["increase"] = -1
        self.canvas.move(self.reimu_dict['tag'], 0, self.reimu_dict["increase"])
        self.canvas.move(self.marisa_dict['tag'], 0, self.marisa_dict["increase"])
        self.reimu_dict['pos_y'] += self.reimu_dict["increase"]
        self.marisa_dict['pos_y'] += self.marisa_dict["increase"]
        self.root.after(120, self.fuwa_fuwa_animation)

    def load_gpt2(self, tag):
        prefix = make_hard_prompt.MakeHardPrompt().get_hard_prompt(tag)
        #print(prefix)
        gpt = gpt2.GetSentence()
        response = gpt.get_sentence(prefix)
        self.message = gpt.get_message(response[0])
        #self.message = gpt.add_yukkuri(self.message)
        self.len_message = 0
        print(self.message)
        self.message_controller()

    def message_controller(self):
        text = self.message[self.len_message]
        self.display_message(text, 370, 410)

        if self.len_message % 2 == 1:
            self.change_image(
                self.balloon_dict['balloon_left_no'],
                self.balloon_dict['pos_x'], 
                self.balloon_dict['pos_y'],
                self.balloon_dict['tag'])
            self.animation(self.marisa_dict, len(text))
            self.root.after(100, self.play_voice, text, self.voice_sub_key)
        else:
            self.change_image(
                self.balloon_dict['balloon_right_no'],
                self.balloon_dict['pos_x'], 
                self.balloon_dict['pos_y'],
                self.balloon_dict['tag'])
            self.animation(self.reimu_dict, len(text))
            self.root.after(100, self.play_voice, text, self.voice_main_key)
        self.len_message += 1
        if self.len_message < len(self.message):
            self.root.after(self.wait_character_time * len(text), self.message_controller)

    def play_voice(self, text, key):
        self.softalk.play(key, text)

