import tkinter as tk
from PIL import Image, ImageTk

class Ui_Mu:
    def setupUi(self, Acc):
        Acc.title("Coefficiant of friction explanation")
        Acc.geometry("600x172")

        self.centralwidget = tk.Frame(Acc)
        self.centralwidget.pack(fill=tk.BOTH, expand=1)
        self.image_label = tk.Label(self.centralwidget)
        self.image_label.pack(fill=tk.BOTH, expand=1)
        Acc.config(bg='white')
        self.image = ImageTk.PhotoImage(Image.open("explain/mu explanation.png"))
        self.image_label.config(image=self.image)

        self.retranslateUi(Acc)

    def retranslateUi(self, Acc):
        pass

class Mu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Mu()
        self.ui.setupUi(self)

# if __name__ == "__main__":
#     app = Acc()
#     app.mainloop()
