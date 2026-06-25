import tkinter as tk 
from tkinter import messagebox
from translator import translate_auto

class Logic:       
    def translate_text(self,text):
        return translate_auto(text)
        
        


class UI:
    def __init__(self) -> None:
        self.root=tk.Tk()
        self.root.title("AI Translation Bot")
        self.root.geometry("500x500")
        self.root.resizable(False,False)
        self.create_widgets()
        self.logic=Logic()
        self.run()

    def create_widgets(self):
        #CLIENT WIDGETS
        title=tk.Label(self.root,text="🤳WELCOME AI Translation Bot",font=("Tahoma",20)).pack()
        client_lbl=tk.Label(self.root,text="YOU:").pack(anchor="w",padx=10,pady=5)
        self.client_ent=tk.Text(self.root,width=80,height=8)
        self.client_ent.pack(padx=10,pady=5)

        # BOT WIDGETS
        bot_lbl=tk.Label(self.root,text="BOT:").pack(anchor="w",padx=10,pady=5)
        self.bot_ent=tk.Text(self.root,width=80,height=8)
        self.bot_ent.pack(padx=10,pady=5)

        #translate button 
        translation_btn=tk.Button(self.root,text="Translate",command=self.translate_btn_func)
        translation_btn.pack(padx=10,pady=5)

    def type_writer(self,text,index=0):
        if index<len(text):
            self.bot_ent.insert("end",text[index])
            self.bot_ent.see("end")

            self.root.after(30,lambda:self.type_writer(text,index+1))

        
    def translate_btn_func(self):
        
        text=self.client_ent.get("1.0",tk.END)

        result=self.logic.translate_text(text)

        self.bot_ent.delete("1.0",tk.END)

        self.type_writer(result)

        
    def run(self):
        self.root.mainloop()
        


if __name__=="__main__":
    UI()

