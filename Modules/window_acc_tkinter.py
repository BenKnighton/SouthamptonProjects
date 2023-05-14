import tkinter as tk
from PIL import ImageTk, Image


class Ui_Acc(object):
    def setupUi(self, Acc):
        Acc.geometry('600x172')
        Acc.resizable(False, False)
        Acc.title("Acceleration explanation")

        self.image_label = tk.Label(Acc)
        self.image_label.grid(row=0, column=0)

        self.image = ImageTk.PhotoImage(Image.open("explain/acc explanation.png"))
        self.image_label.config(image=self.image)

    def retranslateUi(self, Acc):
        pass


class Acc(tk.Tk):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Acc()
        self.ui.setupUi(self)

        self.bind("<Configure>", self.resize_image)

    def resize_image(self, event):
        resized = self.ui.image.resize((event.width, event.height))
        self.ui.image = ImageTk.PhotoImage(resized)
        self.ui.image_label.config(image=self.ui.image)


# if __name__ == "__main__":
#     Acc = Acc()
#     Acc.mainloop()
