from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Acc(object):
    def setupUi(self, Acc):
        Acc.setObjectName("Acc")
        Acc.resize(600, 172)

        self.centralwidget = QtWidgets.QWidget(Acc)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.image_label = QtWidgets.QLabel(self.centralwidget)
        self.image_label.setScaledContents(True)
        self.image_label.setObjectName("image_label")
        self.gridLayout.addWidget(self.image_label, 0, 0, 1, 1)
        Acc.setCentralWidget(self.centralwidget)

        self.image = QtGui.QPixmap("explain/acc explanation.png")
        self.image_label.setPixmap(self.image)

        self.retranslateUi(Acc)
        QtCore.QMetaObject.connectSlotsByName(Acc)

    def retranslateUi(self, Acc):
        _translate = QtCore.QCoreApplication.translate
        Acc.setWindowTitle(_translate("Acc", "Accelaration explanation"))

class Acc(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Acc()
        self.ui.setupUi(self)

    def resizeEvent(self, event):
        scaled_pixmap = self.ui.image.scaled(
            self.ui.image_label.size(), QtCore.Qt.KeepAspectRatio, 
            QtCore.Qt.SmoothTransformation)
        self.ui.image_label.setPixmap(scaled_pixmap)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Acc = Acc()
    Acc.show()
    sys.exit(app.exec_())
