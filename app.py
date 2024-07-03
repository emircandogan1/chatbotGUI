from tkinter import *
from chat import get_response, bot_name # chat is class that i create for chat-bot


BG_GRAY = "#D3D3D3"      
BG_COLOR = "#FFFFFF"     
TEXT_COLOR = "#2C3E50"  
ENTRY_BG = "#F1F1F1"     
BUTTON_BG = "#3498DB"    
BUTTON_TEXT_COLOR = "#FFFFFF" 
FONT = ("Helvetica", 12)
FONT_BOLD = ("Helvetica", 12, "bold")
FONT_HEADER = ("Helvetica", 14, "bold")

class ChatApplication:
    def __init__(self):
        self.window = Tk()
        self._setup_main_window()

    def run(self):
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title('Emiren Chatbot')
        self.window.resizable(width=False, height=False)
        self.window.configure(width=700, height=550, bg=BG_COLOR)

        head_label = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR,
                           text="Hoşgeldiniz", font=FONT_HEADER, pady=10)
        head_label.place(relwidth=1)

        line = Label(self.window, bg=BG_GRAY)
        line.place(relwidth=1, rely=0.07, relheight=0.012)

        self.text_widget = Text(self.window, bg=BG_COLOR, fg=TEXT_COLOR,
                                font=FONT, padx=5, pady=5, wrap=WORD, state=DISABLED)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)

        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)

        bottom_label = Label(self.window, bg=BG_GRAY, height=80)
        bottom_label.place(relwidth=1, rely=0.825)

        self.msg_entry = Entry(bottom_label, bg=ENTRY_BG, fg=TEXT_COLOR, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

        send_button = Button(bottom_label, text="Gönder", font=FONT_BOLD, bg=BUTTON_BG,
                             fg=BUTTON_TEXT_COLOR, command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)

    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "Sen")

    def _insert_message(self, msg, sender):
        if not msg:
            return 
        
        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)

        response = get_response(msg)
        msg2 = f"{bot_name}: {response}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)
        self.text_widget.see(END)

if __name__ == "__main__":
    app = ChatApplication()
    app.run()
