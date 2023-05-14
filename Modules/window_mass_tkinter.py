import tkinter as tk
from PIL import ImageTk, Image

class Ui_Form(object):
    def setupUi(self, Acc):
        Acc.title("Mass explanation")
        Acc.geometry("600x172")

        self.centralwidget = tk.Frame(Acc)
        self.centralwidget.pack(fill="both", expand=True)

        self.image_label = tk.Label(self.centralwidget)
        self.image_label.pack(fill="both", expand=True)
        Acc.config(bg="white")

        self.image = ImageTk.PhotoImage(Image.open("explain/mass explanation.png"))
        self.image_label.config(image=self.image)

        self.retranslateUi(Acc)

    def retranslateUi(self, Acc):
        pass

class mass(tk.Tk):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.bind("<Configure>", self.on_resize)

    def on_resize(self, event):
        self.image = ImageTk.PhotoImage(Image.open("explain/mass explanation.png").resize((event.width, event.height)))
        self.ui.image_label.config(image=self.image)

# if __name__ == "__main__":
#     app = mass()
#     app.mainloop()
