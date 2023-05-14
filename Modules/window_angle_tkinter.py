


import tkinter as tk
from PIL import Image, ImageTk


class Ui_Angle(object):
    def setupUi(self, Acc):
        Acc.title("Angle explanation")
        Acc.geometry("600x172")

        self.centralwidget = tk.Frame(Acc)
        self.centralwidget.pack(fill=tk.BOTH, expand=True)
        self.centralwidget.columnconfigure(0, weight=1)

        self.image_label = tk.Label(self.centralwidget)
        self.image_label.pack(fill=tk.BOTH, expand=True)
        Acc.config(menu=self.centralwidget)

        self.image = ImageTk.PhotoImage(Image.open("explain/angle explanation.png"))
        self.image_label.config(image=self.image)

        self.retranslateUi(Acc)

    def retranslateUi(self, Acc):
        pass


class Angle(tk.Tk):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Angle()
        self.ui.setupUi(self)

    def on_resize(self, event):
        image = Image.open("explain/angle explanation.png")
        width, height = event.width, event.height
        ratio = min(width / image.width, height / image.height)
        new_size = (int(image.width * ratio), int(image.height * ratio))
        self.image = ImageTk.PhotoImage(image.resize(new_size))
        self.ui.image_label.config(image=self.image)


# if __name__ == "__main__":
#     angle = Angle()
#     angle.bind("<Configure>", angle.on_resize)
#     angle.mainloop()
