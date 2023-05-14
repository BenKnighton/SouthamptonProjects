# from PyQt5 import QtCore, QtGui, QtWidgets


# class Ui_Angle(object):
#     def setupUi(self, Angle):
#         Angle.setObjectName("Angle")
#         Angle.resize(400, 300)
#         self.image_label = QtWidgets.QLabel(Angle)
#         self.image_label.setGeometry(QtCore.QRect(0, 0, Angle.width(), Angle.height()))
#         self.image_label.setScaledContents(True)
#         self.image_label.setObjectName("image_label")
#         self.image = QtGui.QPixmap("explain/angle explanation.png")
#         self.image_label.setPixmap(self.image.scaled(Angle.size()))

#         self.retranslateUi(Angle)
#         QtCore.QMetaObject.connectSlotsByName(Angle)

#     def retranslateUi(self, Angle):
#         _translate = QtCore.QCoreApplication.translate
#         Angle.setWindowTitle(_translate("Angle", "Form"))
        
#         Angle.resizeEvent = lambda event: self.image_label.setPixmap(self.image.scaled(Angle.size()))

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Angle = QtWidgets.QWidget()
#     ui = Ui_Angle()
#     ui.setupUi(Angle)
#     Angle.show()
#     sys.exit(app.exec_())




from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Angle(object):
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

        self.image = QtGui.QPixmap("explain/angle explanation.png")
        self.image_label.setPixmap(self.image)

        self.retranslateUi(Acc)
        QtCore.QMetaObject.connectSlotsByName(Acc)

    def retranslateUi(self, Acc):
        _translate = QtCore.QCoreApplication.translate
        Acc.setWindowTitle(_translate("Acc", "Angle explanation"))

class Acc(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Angle()
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
