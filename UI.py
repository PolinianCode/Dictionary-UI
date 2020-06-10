import tkinter
import json
from difflib import get_close_matches
from tkinter import *
from tkinter import messagebox


data = json.load(open("data.json","r"))
output = ""
class GUI:
    def __init__(self, master):    #Виджеты и данные об окне
        self.master = master
        master.title("Dictionary")
        master.geometry("800x600")
        #master.resizable(0,0)

        self.show_me_img = PhotoImage(file='Button.png')
        global word
        global text


        self.label = Label(master, text="Enter the word",pady = 30, anchor = CENTER)
        self.label.config(font=("Morganite", 30))
        self.label.pack()

        self.e1 = Entry(width = 30,relief=FLAT, font='Zelek' )
        self.e1.pack()

        self.how_to_use_btn = Label(master, text="How to use?", font=("Arial", 8), fg="Purple", cursor = "hand2")
        self.how_to_use_btn.bind("<Enter>",self.hover_on_text)
        self.how_to_use_btn.bind("<Leave>",self.dehover_on_text)
        self.how_to_use_btn.bind("<Button-1>", self.how_msg)
        self.how_to_use_btn.pack(pady = 10)



        self.enter_btn = Button(master, text="Show me",  relief = SUNKEN, cursor = "hand2", width = 185, height = 50, image = self.show_me_img, border = 0, command = self.on_click_main_btn)
        self.enter_btn.pack(pady = 20, side = TOP)

        self.label_result = Text(master,width = 75, height = 15, state=DISABLED)
        self.label_result.pack(padx = 10)

    def show_res(self, p):      #Вывод результата в Label_Result
        if type(p) == list:
            for item in p:
                self.label_result.configure(state=NORMAL)
                self.label_result.insert(END, "*" + item + "\n")
                self.label_result.configure(state=DISABLED)
        
            

    def on_click_main_btn(self):        #Проверка ввода
        self.label_result.configure(state=NORMAL)
        self.label_result.delete(1.0, END)
        self.label_result.configure(state=DISABLED)
        word = self.e1.get()
        global output
        if word in data:
            output = self.find_word(word)
            self.show_res(output)
        elif word.title() in data:
            output = self.find_word(word.title())
            self.show_res(output)
        elif word.upper() in data:
            output = self.find_word(word.upper())
            self.show_res(output)
        elif word.lower() in data:
            output = self.find_word(word.lower())
            self.show_res(output)
        elif len(get_close_matches(word, data.keys())) > 0:
            replace_text = "Did you mean %s?" % get_close_matches(word, data.keys())[0]
            MsgBox = messagebox.askquestion(title="Mistake", message=replace_text)
            if MsgBox == 'yes':
                output = data[get_close_matches(word, data.keys())[0]]
                self.show_res(output)
            else:
               self.label_result.configure(text = "The word doens exist")
        else:
            self.label_result.configure(text = "The word doens exist.Please check the word one more time!")

        

    def find_word(self, word):
        return data[word]

    def how_msg(self, event):
        messagebox.showinfo(title = "Guide", message = '''1)Enter the word into the field(in ENG) 
2)Press the button 
3)Ready)''')

    def hover_on_text(self, event):
        self.how_to_use_btn.configure(font="Arial 8 underline")

    def dehover_on_text(self, event):
        self.how_to_use_btn.configure(font="Arial 8")



root = Tk()
window = GUI(root)
root.mainloop()


