
#if unable to install, look at instructions here: https://github.com/BenKnighton/SouthamptonProjects.git

from PyQt5 import QtCore, QtGui, QtWidgets
from math import radians
from math import sqrt
from math import cos
from math import sin

from Modules.window_mass import Ui_Form
from Modules.window_angle import Ui_Angle

from Modules.window_mu import Ui_Mu
from Modules.window_acc import Ui_Acc


def merge(list1, list2):
    merged_list = tuple(zip(list1, list2))
    return merged_list

def pos(lst):
    return [x for x in lst if x > 0] or None

#v=u+at
def v_uat(u:float, a:float, t:float) -> float:
	try:
		u = float(u)
		a = float(a)
		t = float(t)
		return float(u + (a*t))
	except ValueError:
		return "input error"

def u_vat(v:float, a:float, t:float) -> float:
	try:
		v = float(v)
		a = float(a)
		t = float(t)
		return float(v - (a * t))
	except ValueError:
		return "input error"

def t_uva(u:float, v:float, a:float) -> float:
	try:
		u = float(u)
		v = float(v)
		a = float(a)
		return float((v - u)/ a)
	except ValueError:
		return "input error"
	except ZeroDivisionError:
		return "Div/0"

def a_uvt(u:float, v:float, t:float) -> float:
	try:
		u = float(u)
		v = float(v)
		t = float(t)
		return float((v - u)/ t)
	except ValueError:
		return "input error"
	except ZeroDivisionError:
		return "Div/0"

#s=ut+0.5at^2
def s_uat(u:float, a:float, t:float) -> float:
	try:
		u = float(u)
		a = float(a)
		t = float(t)
		return float((u*t) + (0.5 * a * t**2))
	except ValueError:
		return "input error"

def u_sat(s:float, a:float, t:float) -> float:
	try:
		s = float(s)
		a = float(a)
		t = float(t)
		return float((s-(0.5 * a * t**2))/t)
	except ValueError:
		return "input error"
	except ZeroDivisionError:
		return "Div/0"

def a_sut(s:float, u:float, t:float) -> float:
	try:
		s = float(s)
		u = float(u)
		t = float(t)
		return float((2 * (s - u*t))/t**2)
	except ValueError:
		return "input error"
	except ZeroDivisionError:
		return "Div/0"

def t_sua(s:float, u:float, a:float) -> float:
	try:
		s = float(s)
		u = float(u)
		a = float(a)
		#Disregard the - version of the +- part as t must be positive
		return [float((-u + sqrt(u**2 - 2*a*-s))/a), float((-u - sqrt(u**2 - 2*a*-s))/a)]                                    #ARGH +/- problems!!!!!
	except ValueError:
		return "input error"
	except ZeroDivisionError:
		return "Div/0"

#s=vt-0.5at^2
def s_vat(v:float, a:float, t:float) -> float:
	try:
		v = float(v)
		a = float(a)
		t = float(t)
		return float((v*t) - (0.5 * a * t**2))
	except ValueError:
		return "input error"

def v_sat(s:float, a:float, t:float) -> float:
	try:
		s = float(s)
		a = float(a)
		t = float(t)
		return float((s+(0.5 * a * t**2))/t)
	except ValueError:
		return "input error"

def a_svt(s:float, v:float, t:float) -> float:
	try:
		s = float(s)
		v = float(v)
		t = float(t)
		return float((2 * ((v*t) - s))/ t**2)
	except ValueError:
		return "input error"
	except ZeroDivisionError:
		return "Div/0"

def t_sva(s:float, v:float, a:float) -> float:
	try:
		s = float(s)
		v = float(v)
		a = float(a)
		#Disregard the + version of the +- part to get correct answer for t
		return float((v - sqrt(v**2 - 2*a*s))/a)
	except ValueError:
		return "input error"
	except ZeroDivisionError:
		return "Div/0"

#v^2=u^2+2as
def v_sua(s:float, u:float, a:float) -> float:
	try:
		s = float(s)
		u = float(u)
		a = float(a)
		return float(sqrt(u**2 + 2 * a * s))
	except ValueError:
		return "input error"

def u_sva(s:float, v:float, a:float) -> float:
	try:
		s = float(s)
		v = float(v)
		a = float(a)
		return float(sqrt(v**2 - 2 * a *s))
	except ValueError:
		return "input error"

def a_suv(s:float, u:float, v:float) -> float:
	try:
		s = float(s)
		u = float(u)
		v = float(v)
		return float((v**2 - u**2)/ (2 * s))
	except ValueError:
		return "input error"
	except ZeroDivisionError:
		return "Div/0"

def s_uva(u:float, v:float, a:float) -> float:
	try:
		u = float(u)
		v = float(v)
		a = float(a)
		return float((v**2 - u**2)/ (2 * a))
	except ValueError:
		return "input error"
	except ZeroDivisionError:
		return "Div/0"

#s=t(u+v)/2
def s_uvt(u:float, v:float, t:float) -> float:
	try:
		u = float(u)
		v = float(v)
		t = float(t)
		return float(((u + v)/ 2) * t)
	except ValueError:
		return "input error"

def u_svt(s:float, v:float, t:float) -> float:
	try:
		s = float(s)
		v = float(v)
		t = float(t)
		return float(((2 * s)/ t) - v)
	except ValueError:
		return "input error"
	except ZeroDivisionError:
		return "Div/0"

def v_sut(s:float, u:float, t:float) -> float:
	try:
		s = float(s)
		u = float(u)
		t = float(t)
		return float(((2 * s)/ t) - u)
	except ValueError:
		return "input error"
	except ZeroDivisionError:
		return "Div/0"

def t_suv(s:float, u:float, v:float) -> float:
	try:
		s = float(s)
		u = float(u)
		v = float(v)
		return float((2 * s)/ (u + v))
	except ValueError:
		return "input error"
	except ZeroDivisionError:
		return "Div/0"


def Suvat_calculator(s, u, v, a, t):
    print("input", s, u, v, a, t)
    print(type(s))
    dis, ini, fin, acc, time = 0, 0, 0, 0, 0

    if s == "":
        print("yes")
        if v == "":
            fin = v_uat(u, a, t)
        if u == "":
            ini = u_vat(v, a, t)
        if t == "":
            print("yes")
            time = t_uva(u, v, a)
        if a == "":
            acc = a_uvt(u, v, t)

    if u == "":
        if s == "":
            dis = s_vat(v, a, t)
        if v == "":
            fin = v_sat(s,  a, t)
        if a == "":
            acc = a_svt(s, v, t)
        if t == "":
            time = t_sva(s,  v, a)

    if v == "":
        if s == "":
            dis = s_uat(u, a, t)
        if u == "":
            ini = u_sat(s, a, t)
        if a == "":
            acc = a_sut(s, u, t)
        if t == "":
            time = t_sua(s, u, a)

    if a == "":
        if s == "":
            dis = s_uvt(u, v, t)
        if u == "":
            ini = u_svt(s, v, t)
        if v == "":
            fin = v_sut(s, u, t)
        if t == "":
            time = t_suv(s, u, v)

    if t == "":
        if v == "":
            fin = v_sua(s, u, a)
        if u == "":
            ini = u_sva(s, v, a)
        if a == "":
            acc = a_suv(s, u, v)
        if s == "":
            dis = s_uva(u, v, a)

    print("suvat result", dis, ini, fin, acc, time)

    try:
        if len(time) == 2:
            time = pos(time)[0]
    except TypeError:
        pass

    return (dis, ini, fin, acc, time)



def convert_mass(value, type_):
    value = float(value)
    if type_ == "mg":
        value = value / 1000000
    if type_ == "g":
        value = value / 1000
    if type_ == "kg":
        value = value
    if type_ == "oz":
        value = value / 35.27396584
    if type_ == "lb":
        value = value / 2.204622476
    if type_ == "tonne":
        value = value * 1000

	
    return value


def convert_distance(value, type_):
    value = float(value)
    if type_ == "mm":
        value = value / 1000
    if type_ == "cm":
        value = value / 100
    if type_ == "m":
        value = value
    if type_ == "km":
        value = value * 1000
    if type_ == "inch":
        value = value / 39.37007874
    if type_ == "yard":
        value = value / 1.093613298
    if type_ == "ft":
        value = value / 3.280839895
    if type_ == "mile":
        value = value / 0.000621371
		
    return value


def convert_time(value, type_):
    value = float(value)
    if type_ == "ms":
        value = value / 1000
    if type_ == "s":
        value = value 
    if type_ == "min":
        value = value * 60
    if type_ == "hour":
        value = value * 3600
    return value


def convert_speed(value, type_):
    value = float(value)
    if type_ == "cm/s":
        value = value / 100
    if type_ == "m/s":
        value = value / 1
    if type_ == "km/h":
        value = value / 3.6
    if type_ == "mile/h":
        value = value / 2.236936
    if type_ == "ft/s":
        value = value / 3.2808	
    return value



class Ui_Mass(object):

    def openMassWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Form()
        self.ui.setupUi (self.window)
        self.window.show()

    def openAngleWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Angle()
        self.ui.setupUi (self.window)
        self.window.show()


    def openMuWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Mu()
        self.ui.setupUi (self.window)
        self.window.show()


    def openAccWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Acc()
        self.ui.setupUi (self.window)
        self.window.show()





    def setupUi(self, Mass):
        Mass.setObjectName("Mass")
        Mass.setFixedSize(912, 708)
        font = QtGui.QFont()
        font.setFamily("Arial")
        Mass.setFont(font)
        self.Mass_label = QtWidgets.QLabel(Mass)
        self.Mass_label.setGeometry(QtCore.QRect(30, 450, 58, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Mass_label.setFont(font)
        self.Mass_label.setStyleSheet("color: rgb(0, 0, 0);")
        self.Mass_label.setObjectName("Mass_label")
        self.Mass_lineEdit = QtWidgets.QLineEdit(Mass)
        self.Mass_lineEdit.setGeometry(QtCore.QRect(130, 450, 113, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Mass_lineEdit.setFont(font)
        self.Mass_lineEdit.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.Mass_lineEdit.setObjectName("Mass_lineEdit")
        self.Angle_label = QtWidgets.QLabel(Mass)
        self.Angle_label.setGeometry(QtCore.QRect(30, 490, 58, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Angle_label.setFont(font)
        self.Angle_label.setStyleSheet("color: rgb(0, 0, 0);")
        self.Angle_label.setObjectName("Angle_label")
        self.Angle_lineEdit = QtWidgets.QLineEdit(Mass)
        self.Angle_lineEdit.setGeometry(QtCore.QRect(130, 490, 113, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Angle_lineEdit.setFont(font)
        self.Angle_lineEdit.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.Angle_lineEdit.setObjectName("Angle_lineEdit")
        self.Object_material_label = QtWidgets.QLabel(Mass)
        self.Object_material_label.setGeometry(QtCore.QRect(150, 550, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Object_material_label.setFont(font)
        self.Object_material_label.setStyleSheet("color: rgb(0, 0, 0);")
        self.Object_material_label.setObjectName("Object_material_label")
        self.Slope_material_label = QtWidgets.QLabel(Mass)
        self.Slope_material_label.setGeometry(QtCore.QRect(150, 590, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Slope_material_label.setFont(font)
        self.Slope_material_label.setStyleSheet("color: rgb(0, 0, 0);")
        self.Slope_material_label.setObjectName("Slope_material_label")
        self.Mu_label = QtWidgets.QLabel(Mass)
        self.Mu_label.setGeometry(QtCore.QRect(30, 630, 161, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Mu_label.setFont(font)
        self.Mu_label.setStyleSheet("color: rgb(0, 0, 0);")
        self.Mu_label.setObjectName("Mu_label")
        self.mass_comboBox = QtWidgets.QComboBox(Mass)
        self.mass_comboBox.setGeometry(QtCore.QRect(250, 450, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.mass_comboBox.setFont(font)
        self.mass_comboBox.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.mass_comboBox.setObjectName("mass_comboBox")
        self.angle_comboBox = QtWidgets.QComboBox(Mass)
        self.angle_comboBox.setGeometry(QtCore.QRect(250, 490, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.angle_comboBox.setFont(font)
        self.angle_comboBox.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.angle_comboBox.setObjectName("angle_comboBox")
        self.Object_comboBox = QtWidgets.QComboBox(Mass)
        self.Object_comboBox.setGeometry(QtCore.QRect(250, 550, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Object_comboBox.setFont(font)
        self.Object_comboBox.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.Object_comboBox.setObjectName("Object_comboBox")
        self.Slope_comboBox = QtWidgets.QComboBox(Mass)
        self.Slope_comboBox.setGeometry(QtCore.QRect(250, 590, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Slope_comboBox.setFont(font)
        self.Slope_comboBox.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.Slope_comboBox.setObjectName("Slope_comboBox")
        self.Mu_lineEdit = QtWidgets.QLineEdit(Mass)
        self.Mu_lineEdit.setGeometry(QtCore.QRect(210, 630, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Mu_lineEdit.setFont(font)
        self.Mu_lineEdit.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.Mu_lineEdit.setObjectName("Mu_lineEdit")
        self.angle_Slider = QtWidgets.QSlider(Mass)
        self.angle_Slider.setGeometry(QtCore.QRect(30, 520, 301, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.angle_Slider.setFont(font)
        self.angle_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.angle_Slider.setObjectName("angle_Slider")
        self.Distance_label = QtWidgets.QLabel(Mass)
        self.Distance_label.setGeometry(QtCore.QRect(560, 490, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Distance_label.setFont(font)
        self.Distance_label.setStyleSheet("color: rgb(0, 0, 0);")
        self.Distance_label.setObjectName("Distance_label")
        self.comboBox_distance = QtWidgets.QComboBox(Mass)
        self.comboBox_distance.setGeometry(QtCore.QRect(800, 490, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.comboBox_distance.setFont(font)
        self.comboBox_distance.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.comboBox_distance.setObjectName("comboBox_distance")
        self.Distance_lineEdit = QtWidgets.QLineEdit(Mass)
        self.Distance_lineEdit.setGeometry(QtCore.QRect(680, 490, 113, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Distance_lineEdit.setFont(font)
        self.Distance_lineEdit.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.Distance_lineEdit.setObjectName("Distance_lineEdit")
        self.Time_lineEdit = QtWidgets.QLineEdit(Mass)
        self.Time_lineEdit.setGeometry(QtCore.QRect(680, 610, 113, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Time_lineEdit.setFont(font)
        self.Time_lineEdit.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.Time_lineEdit.setObjectName("Time_lineEdit")
        self.Time_label = QtWidgets.QLabel(Mass)
        self.Time_label.setGeometry(QtCore.QRect(560, 610, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Time_label.setFont(font)
        self.Time_label.setStyleSheet("color: rgb(0, 0, 0);")
        self.Time_label.setObjectName("Time_label")
        self.comboBox_time = QtWidgets.QComboBox(Mass)
        self.comboBox_time.setGeometry(QtCore.QRect(800, 610, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.comboBox_time.setFont(font)
        self.comboBox_time.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.comboBox_time.setObjectName("comboBox_time")
        self.u_lineEdit = QtWidgets.QLineEdit(Mass)
        self.u_lineEdit.setGeometry(QtCore.QRect(680, 530, 113, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.u_lineEdit.setFont(font)
        self.u_lineEdit.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.u_lineEdit.setObjectName("u_lineEdit")
        self.v_label = QtWidgets.QLabel(Mass)
        self.v_label.setGeometry(QtCore.QRect(560, 570, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.v_label.setFont(font)
        self.v_label.setStyleSheet("color: rgb(0, 0, 0);")
        self.v_label.setObjectName("v_label")
        self.u_label = QtWidgets.QLabel(Mass)
        self.u_label.setGeometry(QtCore.QRect(560, 530, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.u_label.setFont(font)
        self.u_label.setStyleSheet("color: rgb(0, 0, 0);")
        self.u_label.setObjectName("u_label")
        self.comboBox_initial_v = QtWidgets.QComboBox(Mass)
        self.comboBox_initial_v.setGeometry(QtCore.QRect(800, 530, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.comboBox_initial_v.setFont(font)
        self.comboBox_initial_v.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.comboBox_initial_v.setObjectName("comboBox_initial_v")
        self.v_lineEdit = QtWidgets.QLineEdit(Mass)
        self.v_lineEdit.setGeometry(QtCore.QRect(680, 570, 113, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.v_lineEdit.setFont(font)
        self.v_lineEdit.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.v_lineEdit.setObjectName("v_lineEdit")
        self.comboBox_final_v = QtWidgets.QComboBox(Mass)
        self.comboBox_final_v.setGeometry(QtCore.QRect(800, 570, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.comboBox_final_v.setFont(font)
        self.comboBox_final_v.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.comboBox_final_v.setObjectName("comboBox_final_v")
        self.Additiona_features_label = QtWidgets.QLabel(Mass)
        self.Additiona_features_label.setGeometry(QtCore.QRect(560, 430, 311, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Additiona_features_label.setFont(font)
        self.Additiona_features_label.setStyleSheet("color: rgb(0, 0, 0);")
        self.Additiona_features_label.setObjectName("Additiona_features_label")
        self.Features_label = QtWidgets.QLabel(Mass)
        self.Features_label.setGeometry(QtCore.QRect(30, 430, 301, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Features_label.setFont(font)
        self.Features_label.setStyleSheet("color: rgb(0, 0, 0);")
        self.Features_label.setObjectName("Features_label")
        self.mass_pushButton = QtWidgets.QPushButton(Mass)
        self.mass_pushButton.setGeometry(QtCore.QRect(210, 10, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.mass_pushButton.setFont(font)
        self.mass_pushButton.setStyleSheet("background-color:   rgb(255, 108, 105);\n"
"border-radius: 5px;\n"
"color: rgb(0, 0, 0);")
        self.mass_pushButton.setObjectName("mass_pushButton")
        self.Angle_pushButton = QtWidgets.QPushButton(Mass)
        self.Angle_pushButton.setGeometry(QtCore.QRect(300, 10, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Angle_pushButton.setFont(font)
        self.Angle_pushButton.setStyleSheet("background-color:   rgb(255, 108, 105);\n"
"border-radius: 5px;\n"
"color: rgb(0, 0, 0);")
        self.Angle_pushButton.setObjectName("Angle_pushButton")
        self.Mu_pushButton = QtWidgets.QPushButton(Mass)
        self.Mu_pushButton.setGeometry(QtCore.QRect(390, 10, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Mu_pushButton.setFont(font)
        self.Mu_pushButton.setStyleSheet("background-color:   rgb(255, 108, 105);\n"
"border-radius: 5px;\n"
"color: rgb(0, 0, 0);")
        self.Mu_pushButton.setObjectName("Mu_pushButton")
        self.Accelaration_pushButton = QtWidgets.QPushButton(Mass)
        self.Accelaration_pushButton.setGeometry(QtCore.QRect(570, 10, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Accelaration_pushButton.setFont(font)
        self.Accelaration_pushButton.setStyleSheet("background-color:   rgb(255, 108, 105);\n"
"border-radius: 5px;\n"
"color: rgb(0, 0, 0);")
        self.Accelaration_pushButton.setObjectName("Accelaration_pushButton")
        self.Answers_scrollArea = QtWidgets.QScrollArea(Mass)
        self.Answers_scrollArea.setGeometry(QtCore.QRect(710, 40, 191, 363))
        self.Answers_scrollArea.setStyleSheet("background-color: rgb(242, 244, 237);\n"
"color: rgb(0, 0, 0);")
        self.Answers_scrollArea.setWidgetResizable(True)
        self.Answers_scrollArea.setObjectName("Answers_scrollArea")
        # self.scrollAreaWidgetContents = QtWidgets.QWidget()
        # self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 189, 361))
        # self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        # self.Answers_scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.Compute_down = QtWidgets.QPushButton(Mass)
        self.Compute_down.setGeometry(QtCore.QRect(30, 660, 151, 32))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Compute_down.setFont(font)
        self.Compute_down.setStyleSheet("background-color:   rgb(233, 128, 255);\n"
"\n"
"border-radius: 8px;\n"
"color: rgb(0, 0, 0);")
        self.Compute_down.setObjectName("Compute_down")
        self.Compute_additional_down = QtWidgets.QPushButton(Mass)
        self.Compute_additional_down.setGeometry(QtCore.QRect(560, 640, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Compute_additional_down.setFont(font)
        self.Compute_additional_down.setStyleSheet("background-color:   rgb(99, 219, 255);\n"
"border-radius: 8px;\n"
"color: rgb(0, 0, 0);")
        self.Compute_additional_down.setObjectName("Compute_additional_down")
        self.Compute_up = QtWidgets.QPushButton(Mass)
        self.Compute_up.setGeometry(QtCore.QRect(190, 660, 151, 32))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Compute_up.setFont(font)
        self.Compute_up.setStyleSheet("background-color:   rgb(129, 222, 145);\n"
"border-radius: 8px;\n"
"color: rgb(0, 0, 0);")
        self.Compute_up.setObjectName("Compute_up")
        self.Compute_additional_up = QtWidgets.QPushButton(Mass)
        self.Compute_additional_up.setGeometry(QtCore.QRect(730, 640, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Compute_additional_up.setFont(font)
        self.Compute_additional_up.setStyleSheet("background-color:   rgb(255, 184, 62);\n"
"border :1px solid  rgb(255, 184, 62);\n"
"border-radius: 8px;\n"
"color: rgb(0, 0, 0);")
        self.Compute_additional_up.setObjectName("Compute_additional_up")
        self.mgcos_theta = QtWidgets.QLabel(Mass)
        self.mgcos_theta.setGeometry(QtCore.QRect(590, 310, 82, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.mgcos_theta.setFont(font)
        self.mgcos_theta.setStyleSheet("color: rgb(0, 0, 0);")
        self.mgcos_theta.setObjectName("mgcos_theta")
        self.Reaction_force = QtWidgets.QLabel(Mass)
        self.Reaction_force.setGeometry(QtCore.QRect(360, 50, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.Reaction_force.setFont(font)
        self.Reaction_force.setStyleSheet("color: rgb(0, 0, 0);")
        self.Reaction_force.setObjectName("Reaction_force")
        self.material = QtWidgets.QLabel(Mass)
        self.material.setGeometry(QtCore.QRect(340, 120, 181, 141))
        self.material.setText("")
        self.material.setPixmap(QtGui.QPixmap("Downloads/rubber.jpg"))
        self.material.setScaledContents(True)
        self.material.setObjectName("material")
        self.diagram = QtWidgets.QLabel(Mass)
        self.diagram.setGeometry(QtCore.QRect(10, 40, 691, 363))
        self.diagram.setText("")
        self.diagram.setPixmap(QtGui.QPixmap("Downloads/final_design.png"))
        self.diagram.setScaledContents(True)
        self.diagram.setObjectName("diagram")
        self.weight = QtWidgets.QLabel(Mass)
        self.weight.setGeometry(QtCore.QRect(340, 330, 88, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.weight.setFont(font)
        self.weight.setStyleSheet("color: rgb(0, 0, 0);")
        self.weight.setObjectName("weight")
        self.mgsin_theta = QtWidgets.QLabel(Mass)
        self.mgsin_theta.setGeometry(QtCore.QRect(200, 230, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.mgsin_theta.setFont(font)
        self.mgsin_theta.setStyleSheet("color: rgb(0, 0, 0);")
        self.mgsin_theta.setObjectName("mgsin_theta")
        self.theta = QtWidgets.QLabel(Mass)
        self.theta.setGeometry(QtCore.QRect(130, 360, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.theta.setFont(font)
        self.theta.setStyleSheet("color: rgb(0, 0, 0);")
        self.theta.setObjectName("theta")
        self.acc_answer = QtWidgets.QLabel(Mass)
        self.acc_answer.setGeometry(QtCore.QRect(150, 110, 82, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.acc_answer.setFont(font)
        self.acc_answer.setStyleSheet("color: rgb(0, 0, 0);\n"
"")
        self.acc_answer.setObjectName("acc_answer")
        self.frictional_force = QtWidgets.QLabel(Mass)
        self.frictional_force.setGeometry(QtCore.QRect(550, 100, 82, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.frictional_force.setFont(font)
        self.frictional_force.setStyleSheet("color: rgb(0, 0, 0);")
        self.frictional_force.setObjectName("frictional_force")
        self.Suvat_ans_label = QtWidgets.QLabel(Mass)
        self.Suvat_ans_label.setGeometry(QtCore.QRect(710, 10, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.Suvat_ans_label.setFont(font)
        self.Suvat_ans_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Suvat_ans_label.setObjectName("Suvat_ans_label")
        self.title_label = QtWidgets.QLabel(Mass)
        self.title_label.setGeometry(QtCore.QRect(10, 10, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.title_label.setFont(font)
        self.title_label.setObjectName("title_label")
        self.Background_1 = QtWidgets.QLabel(Mass)
        self.Background_1.setGeometry(QtCore.QRect(10, 420, 351, 281))
        self.Background_1.setStyleSheet("background-color:   rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"color: rgb(0, 0, 0);")
        self.Background_1.setText("")
        self.Background_1.setObjectName("Background_1")
        self.Background_2 = QtWidgets.QLabel(Mass)
        self.Background_2.setGeometry(QtCore.QRect(550, 420, 351, 281))
        self.Background_2.setStyleSheet("background-color:   rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"color: rgb(0, 0, 0);")
        self.Background_2.setText("")
        self.Background_2.setObjectName("Background_2")
#         self.help_pushButton = QtWidgets.QPushButton(Mass)
#         self.help_pushButton.setGeometry(QtCore.QRect(630, 10, 71, 21))
#         font = QtGui.QFont()
#         font.setFamily("Arial")
#         self.help_pushButton.setFont(font)
#         self.help_pushButton.setStyleSheet("background-color:   rgb(255, 108, 105);\n"
# "border-radius: 5px;\n"
# "color: rgb(0, 0, 0);")
#         self.help_pushButton.setObjectName("help_pushButton")
        self.Arrow = QtWidgets.QLabel(Mass)
        self.Arrow.setGeometry(QtCore.QRect(380, 500, 151, 51))
        self.Arrow.setText("")
        self.Arrow.setPixmap(QtGui.QPixmap("Downloads/red arrow.png"))
        self.Arrow.setScaledContents(True)
        self.Arrow.setObjectName("Arrow")
        self.arrow_explanation = QtWidgets.QLabel(Mass)
        self.arrow_explanation.setGeometry(QtCore.QRect(380, 570, 151, 81))
        self.arrow_explanation.setStyleSheet("background-color:   rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"color: rgb(0, 0, 0);")
        self.arrow_explanation.setScaledContents(False)
        self.arrow_explanation.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.arrow_explanation.setWordWrap(True)
        self.arrow_explanation.setIndent(7)
        self.arrow_explanation.setObjectName("arrow_explanation")
        self.Background_2.raise_()
        self.Background_1.raise_()
        self.material.raise_()
        self.diagram.raise_()
        self.Mass_label.raise_()
        self.Mass_lineEdit.raise_()
        self.Angle_label.raise_()
        self.Angle_lineEdit.raise_()
        self.Object_material_label.raise_()
        self.Slope_material_label.raise_()
        self.Mu_label.raise_()
        self.mass_comboBox.raise_()
        self.angle_comboBox.raise_()
        self.Object_comboBox.raise_()
        self.Slope_comboBox.raise_()
        self.Mu_lineEdit.raise_()
        self.angle_Slider.raise_()
        self.Distance_label.raise_()
        self.comboBox_distance.raise_()
        self.Distance_lineEdit.raise_()
        self.Time_lineEdit.raise_()
        self.Time_label.raise_()
        self.comboBox_time.raise_()
        self.u_lineEdit.raise_()
        self.v_label.raise_()
        self.u_label.raise_()
        self.comboBox_initial_v.raise_()
        self.v_lineEdit.raise_()
        self.comboBox_final_v.raise_()
        self.Additiona_features_label.raise_()
        self.Features_label.raise_()
        self.mass_pushButton.raise_()
        self.Angle_pushButton.raise_()
        self.Mu_pushButton.raise_()
        self.Accelaration_pushButton.raise_()
        self.Answers_scrollArea.raise_()
        self.Compute_down.raise_()
        self.Compute_additional_down.raise_()
        self.Compute_up.raise_()
        self.Compute_additional_up.raise_()
        self.weight.raise_()
        self.mgsin_theta.raise_()
        self.Reaction_force.raise_()
        self.mgcos_theta.raise_()
        self.theta.raise_()
        self.acc_answer.raise_()
        self.frictional_force.raise_()
        self.Suvat_ans_label.raise_()
        self.title_label.raise_()
        # self.help_pushButton.raise_()
        self.Arrow.raise_()
        self.arrow_explanation.raise_()









        #changes
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        self.scrollAreaWidgetContents =  QtWidgets.QTextEdit(Mass)
        # self.scrollAreaWidgetContents.setFont(font)
        self.scrollAreaWidgetContents.setStyleSheet("background-color: transparent;")
        self.scrollAreaWidgetContents.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 501, 151))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.Answers_scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.mass_comboBox.addItems(["kg", "mg", "g", "oz", "lb", "tonne"])
        self.angle_comboBox.addItems(["deg", "rad"])
        self.Object_comboBox.addItems(["wood", "steel", "rubber", "glass", "polyethylene", "concrete"])
        self.Slope_comboBox.addItems(["wood", "steel", "rubber", "glass", "polyethylene", "concrete"])
        self.comboBox_distance.addItems(["m", "mm", "cm", "km", "inch", "yard", "ft", "mile"])
        self.comboBox_time.addItems(["s", "ms", "min", "hour"])
        self.comboBox_initial_v.addItems(["m/s", "cm/s", "km/h", "mile/h", "ft/s"])
        self.comboBox_final_v.addItems(["m/s", "cm/s", "km/h", "mile/h", "ft/s"])
        self.Mu_lineEdit.setText("0.0")

        # self.Angle_lineEdit.returnPressed.connect(self.photoScroll_2)
        self.angle_Slider.valueChanged.connect(self.photoScroll_1)
        self.Compute_down.clicked.connect(self.calc)
        self.Compute_up.clicked.connect(self.calc_going_up)
        self.Compute_additional_down.clicked.connect(self.calc_additional)
        self.Compute_additional_up.clicked.connect(self.calc_additional_going_up)
        self.Object_comboBox.currentTextChanged.connect(self.calc_mu)
        self.Slope_comboBox.currentTextChanged.connect(self.calc_mu)
        self.mass_pushButton.clicked.connect(self.openMassWindow)
        self.Angle_pushButton.clicked.connect(self.openAngleWindow)
        self.Mu_pushButton.clicked.connect(self.openMuWindow)
        self.Accelaration_pushButton.clicked.connect(self.openAccWindow)

        self.retranslateUi(Mass)
        QtCore.QMetaObject.connectSlotsByName(Mass)

    def retranslateUi(self, Mass):
        _translate = QtCore.QCoreApplication.translate
        Mass.setWindowTitle(_translate("Mass", "Force Diagram Calculator"))
        self.Mass_label.setText(_translate("Mass", "Mass"))
        self.Angle_label.setText(_translate("Mass", "Angle"))
        self.Object_material_label.setText(_translate("Mass", "Object Material"))
        self.Slope_material_label.setText(_translate("Mass", "Slope Material"))
        self.Mu_label.setText(_translate("Mass", "Coefficient Of Friction (µ)"))
        self.Distance_label.setText(_translate("Mass", "Distance"))
        self.Time_label.setText(_translate("Mass", "Time"))
        self.v_label.setText(_translate("Mass", "Final Velocity (v)"))
        self.u_label.setText(_translate("Mass", "Initial Velocity (u)"))
        self.Additiona_features_label.setText(_translate("Mass", "SUVAT Calculator"))
        self.Features_label.setText(_translate("Mass", "Force Diagram Calculator"))
        self.mass_pushButton.setText(_translate("Mass", "Mass?"))
        self.Angle_pushButton.setText(_translate("Mass", "Angle?"))
        self.Mu_pushButton.setText(_translate("Mass", "Coefficient of friction?"))
        self.Accelaration_pushButton.setText(_translate("Mass", "Accelaration?"))
        self.Compute_down.setText(_translate("Mass", "Compute acc down"))
        self.Compute_additional_down.setText(_translate("Mass", "Compute Aditional \n"
"Values going down"))
        self.Compute_up.setText(_translate("Mass", "Compute acc up"))
        self.Compute_additional_up.setText(_translate("Mass", "Compute Aditional \n"
"Values going up"))
        self.mgcos_theta.setText(_translate("Mass", "0 (N)"))
        self.Reaction_force.setText(_translate("Mass", "0 (N)"))
        self.weight.setText(_translate("Mass", "0 (N)"))
        self.mgsin_theta.setText(_translate("Mass", "0 (N)"))
        self.theta.setText(_translate("Mass", "0 (degrees)"))
        self.acc_answer.setText(_translate("Mass", "0 (m/s²)"))
        self.frictional_force.setText(_translate("Mass", "0 (N)"))
        self.Suvat_ans_label.setText(_translate("Mass", "SUVAT Answers"))
        self.title_label.setText(_translate("Mass", "Force Diagram Calculator"))
        # self.help_pushButton.setText(_translate("Mass", "Help?"))
        self.arrow_explanation.setText(_translate("Mass", "Once the Accelaration has been calculated, move on to the SUVAT Calculator"))

    def calc_mu(self):
        mu = "0"
        obj = self.Object_comboBox.currentText()
        slope = self.Slope_comboBox.currentText()

        if obj == "wood":
            self.material.setPixmap(QtGui.QPixmap("Downloads/wood.JPG"))

        if obj == "steel":
            self.material.setPixmap(QtGui.QPixmap("Downloads/rust.jpg"))

        if obj == "rubber":
            self.material.setPixmap(QtGui.QPixmap("Downloads/rubber.jpg"))

        if obj == "glass":
            self.material.setPixmap(QtGui.QPixmap("Downloads/glass-2.jpg"))

        if obj == "polyethylene":
            self.material.setPixmap(QtGui.QPixmap("Downloads/plastic.jpeg"))

        if obj == "concrete":
            self.material.setPixmap(QtGui.QPixmap("Downloads/concrete.jpg"))   

        # ["wood", "steel", "rubber", "glass", "polyethylene", "concrete"]
        combinations = [
              ["wood", "wood", 0.1],
              ["wood", "steel", 0.1],
              ["wood", "rubber", 0.5],
              ["wood", "glass", 0.2],
              ["glass", "glass", 0.3],
              ["glass", "rubber", 0.4],
              ["rubber", "rubber", 0.9],
              ["rubber", "polyethylene", 0.9],
              ["rubber", "steel", 0.9],
              ["rubber", "concrete", 0.9],
              ["polyethylene", "polyethylene", 0.9],
              ["polyethylene", "steel", 0.9],
              ["polyethylene", "concrete", 0.9],
              ["polyethylene", "wood", 0.9],
              ["polyethylene", "glass", 0.9],
              ["concrete", "concrete", 0.9],
              ["concrete", "steel", 0.9],
              ["concrete", "glass", 0.9],
              ["concrete", "wood", 0.9],
              ["steel", "glass", 0.9],
              ["steel", "steel", 0.9],

        ]

        for i in combinations:
            if i[0] == obj:
                if i[1] == slope:
                    mu = str(i[2])
            elif i[0] == slope:
                if i[1] == obj:
                    mu = str(i[2])

        self.Mu_lineEdit.setText(str(mu))



    def photoScroll_1(self, value):
        # print("scrolled")
        value = round((value/100)*90)
        if value == 89:
            value = 90

        # print("degrees:", value)
        self.Angle_lineEdit.setText(str(value))

        self.theta.setText(f"{value} (degrees)")
        # self.mgsin_theta.setText(f"{mgsin}")
        # self.mgcos_theta.setText(f"{mgcos}")
        # self.Reaction_force.setText(f"{reaction_F}")
        # self.weight.setText(f"{mass*9.81}")



    def calc(self):
        accelaration = ""
        try:
            #values
            mass = float(self.Mass_lineEdit.text())
            angle = float(self.Angle_lineEdit.text())

            #value correction
            if mass < 0:
                mass = abs(mass)

            if angle < 0:
                angle = abs(angle)

            if angle > 90:
                angle = 90

            #converting the types into their base units
            mass_type = self.mass_comboBox.currentText() 
            angle_type = self.angle_comboBox.currentText()
	    
            mass = convert_mass(mass, mass_type)
            print("converted mass", mass)

            mu = float(self.Mu_lineEdit.text())

            if mu < 0:
                mu = 0
            if mu > 1:
                mu = 1
            # print(mass, angle, mu, "dimentions", mass_dim, angle_type)

            mgcos = mass * 9.81 * cos(radians(angle))
            mgsin = mass * 9.81 * sin(radians(angle))
            reaction_F = mu * mgcos
            accelaration = round((mgsin - reaction_F)/mass, 2)

            print("accelaration", accelaration)
            x = f"Accelaration (m/s²): {accelaration}"
            self.scrollAreaWidgetContents.setText(x)

            self.theta.setText(f"{round(angle, 2)} (degrees)")
            self.mgsin_theta.setText(f"{round(mgsin, 2)} (N)")
            self.mgcos_theta.setText(f"{round(mgcos, 2)} (N)")
            self.Reaction_force.setText(f"{round(reaction_F, 2)} (N)")
            self.weight.setText(f"{round(mass*9.81, 2)} (N)")
            self.acc_answer.setText(f"{round(accelaration, 2)} (m/s²)")
            self.frictional_force.setText(f"{round(mgcos * mu, 2)} (m/s²)")
            return accelaration
        
        except:
            x = f"Accelaration (m/s²): {accelaration}"
            self.scrollAreaWidgetContents.setText(x)
            self.acc_answer.setText(f"{accelaration}")
            return accelaration #round to 2 dp



    def calc_going_up(self):
        accelaration = ""
        try:
            #values
            mass = float(self.Mass_lineEdit.text())
            angle = float(self.Angle_lineEdit.text())

            #value correction
            if mass < 0:
                mass = abs(mass)

            if angle < 0:
                angle = abs(angle)

            if angle > 90: #cant have angle less than 0
                angle = 90

            #converting the types into their base units
            mass_type = self.mass_comboBox.currentText() 
            angle_type = self.angle_comboBox.currentText()
            mass = convert_mass(mass, mass_type)
            print("converted mass", mass)
            mu = float(self.Mu_lineEdit.text())

            if mu < 0:
                mu = 0
            if mu > 1:
                mu = 1

            mgcos = mass * 9.81 * cos(radians(angle))
            mgsin = mass * 9.81 * sin(radians(angle))
            reaction_F = mu * mgcos
            accelaration = round((-mgsin - reaction_F)/mass, )

            print("accelaration", accelaration)
            x = f"Accelaration (m/s²): {accelaration}"
            self.scrollAreaWidgetContents.setText(x)

            self.theta.setText(f"{round(angle, 2)} (degrees)")
            self.mgsin_theta.setText(f"{round(mgsin, 2)} (N)")
            self.mgcos_theta.setText(f"{round(mgcos, 2)} (N)")
            self.Reaction_force.setText(f"{round(reaction_F, 2)} (N)")
            self.weight.setText(f"{round(mass*9.81, 2)} (N)")
            self.acc_answer.setText(f"{round(accelaration, 2)} (m/s²)")
            self.frictional_force.setText(f"{round(mgcos * mu, 2)} (m/s²)")
            return accelaration
        
        except:
            self.scrollAreaWidgetContents.setText(f"Accelaration (m/s²): {accelaration} (m/s²)")
            self.acc_answer.setText(f"{accelaration} (m/s²)")
            return accelaration







    def calc_additional(self):
        print("these are the required forces")
        accelaration_down_slope = self.calc()
        print(accelaration_down_slope)

        #Values
        distance = self.Distance_lineEdit.text()
        time = self.Time_lineEdit.text()
        initial_velocity = self.u_lineEdit.text()
        final_velocity = self.v_lineEdit.text()

        #value correction
        if initial_velocity != "":
            try:
                if float(initial_velocity) > 299792458.0:  #cant be negative
                    initial_velocity = "299792458"

                if float(initial_velocity) < 0:
                    initial_velocity = abs(initial_velocity)
            except ValueError:
                print("Initial velocity has to be a number!")
	    
        if final_velocity != "":
            try:
                if float(final_velocity) > 299792458.0:
                    final_velocity = "299792458"

                # if float(final_velocity) < 0:
                #     final_velocity = abs(final_velocity)
            except ValueError:
                print("Final velocity has to be a number!")
	    
        if time != "":
            try:
                if float(time) < 0.0:
                    time = "0"
            except ValueError:
                print("Time has to be a number!")
	    
        if distance != "":
            try:
                if float(distance) < 0.0:
                    distance = "0"
            except ValueError:
                print("Distance has to be a number!")

        #converting the types into their base units
        dis_type = self.comboBox_distance.currentText() 
        time_type = self.comboBox_time.currentText()
        u_type = self.comboBox_initial_v.currentText()
        v_type = self.comboBox_final_v.currentText()

        if distance != "":
            distance = convert_distance(distance, dis_type)
        
        if time != "":
            time = convert_time(time, time_type)

        if initial_velocity != "":
            initial_velocity = convert_speed(initial_velocity , u_type)

        if final_velocity != "":
            final_velocity = convert_speed(final_velocity, v_type)

        suvat = [distance, initial_velocity, final_velocity, accelaration_down_slope, time]
        count = suvat.count('')
        count = 5-count

        if count == 5:
            #remove 2 things from list, not accelaration
            suvat[0] = ''
            suvat[1] = ''
            pass

        elif count == 4:
            if suvat[0] != '':
                suvat[0] = ''
            else:
                suvat[1] = ''
            #remove something from list, not accelaration
            pass

        if count < 3:
            print("not enought variables!")
        else:
            results = Suvat_calculator(suvat[0], suvat[1], suvat[2], suvat[3], suvat[4])
            names = ["distance (m)", "initial velocity (m/s)", "final velocity (m/s)", "acceleration (m/s²)", "time (s)"]
            tup = merge(names, results)
            x = f"Accelaration (m/s²): {accelaration_down_slope}\n"
            for i in tup:
                value = i[1]
                if value != 0:
                    try:
                        x += f"{i[0]}: {round(float(i[1]), 2)}\n"
                    except:
                        x += f"{i[0]}: {i[1]}\n"
		
            self.scrollAreaWidgetContents.setText(x)
            self.acc_answer.setText(f"{accelaration_down_slope} (m/s²)")
		


    def calc_additional_going_up(self):
        print("these are the required forces")
        accelaration_up_slope = self.calc_going_up() #this is the only change to this function
        print(accelaration_up_slope)

        #Values
        distance = self.Distance_lineEdit.text()
        time = self.Time_lineEdit.text()
        initial_velocity = self.u_lineEdit.text()
        final_velocity = self.v_lineEdit.text()

        #value correction
        if initial_velocity != "":
            try:
                if float(initial_velocity) > 299792458.0:  #cant be negative
                    initial_velocity = "299792458"

                if float(initial_velocity) < 0:
                    initial_velocity = abs(initial_velocity)
            except ValueError:
                print("Initial velocity has to be a number!")
	    
        if final_velocity != "":
            try:
                if float(final_velocity) > 299792458.0:
                    final_velocity = "299792458"

                # if float(final_velocity) < 0:
                #     final_velocity = abs(final_velocity)
            except ValueError:
                print("Final velocity has to be a number!")
	    
        if time != "":
            try:
                if float(time) < 0.0:
                    time = "0"
            except ValueError:
                print("Time has to be a number!")
	    
        if distance != "":
            try:
                if float(distance) < 0.0:
                    distance = "0"
            except ValueError:
                print("Distance has to be a number!")


        #converting the types into their base units
        dis_type = self.comboBox_distance.currentText() 
        time_type = self.comboBox_time.currentText()
        u_type = self.comboBox_initial_v.currentText()
        v_type = self.comboBox_final_v.currentText()

        if distance != "":
            distance = convert_distance(distance, dis_type)
        
        if time != "":
            time = convert_time(time, time_type)

        if initial_velocity != "":
            initial_velocity = convert_speed(initial_velocity , u_type)

        if final_velocity != "":
            final_velocity = convert_speed(final_velocity, v_type)

        suvat = [distance, initial_velocity, final_velocity, accelaration_up_slope, time]
        count = suvat.count('')
        count = 5-count

        if count == 5:
            #remove 2 things from list, not accelaration
            suvat[0] = ''
            suvat[1] = ''
            pass

        elif count == 4:
            if suvat[0] != '':
                suvat[0] = ''
            else:
                suvat[1] = ''
            #remove something from list, not accelaration
            pass

        if count < 3:
            print("not enought variables!")
        else:
            results = Suvat_calculator(suvat[0], suvat[1], suvat[2], suvat[3], suvat[4])
            names = ["distance (m)", "initial velocity (m/s)", "final velocity (m/s)", "acceleration (m/s²)", "time (s)"]
            tup = merge(names, results)
            x = f"Accelaration (m/s²): {accelaration_up_slope}\n"
            for i in tup:
                value = i[1]
                if value != 0:
                    try:
                        x += f"{i[0]}: {round(float(i[1]), 2)}\n"
                    except:
                        x += f"{i[0]}: {i[1]}\n"
		
            self.scrollAreaWidgetContents.setText(x)
            self.acc_answer.setText(f"{accelaration_up_slope} (m/s²)")






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Mass = QtWidgets.QWidget()
    ui = Ui_Mass()
    ui.setupUi(Mass)
    Mass.show()
    sys.exit(app.exec_())
