
#This code is a back up, incase you are unable to install pyqt5

from math import radians
from math import sqrt
from math import cos
from math import sin




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




from Modules.window_mass_tkinter import mass
from Modules.window_angle_tkinter import Angle

from Modules.window_mu_tkinter import Mu
from Modules.window_acc_tkinter import Acc

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk





class Ui_Mass(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("912x708")
        self.master.resizable(False, False)
        self.master.title("Mass")
        self.create_widgets()


    def openMassWindow(self):
        mass_app = mass()
        mass_app.mainloop()         


    def openAngleWindow(self):
        angle_app = Angle()
        # angle_app.bind("<Configure>", angle.on_resize)
        angle_app.mainloop()



    def openMuWindow(self):
        Mu_app = Mu()
        Mu_app.mainloop()



    def openAccWindow(self):
        Acc_app = Acc()
        Acc_app.mainloop()




    def create_widgets(self):
        font = ("Arial", 10)
        self.Mass_label = tk.Label(self.master, text="Mass", font=font)
        self.Mass_label.place(x=30, y=450)

        self.Mass_entry = tk.Entry(self.master, font=font)
        self.Mass_entry.place(x=130, y=450, width=113, height=21)

        self.Angle_label = tk.Label(self.master, text="Angle", font=font)
        self.Angle_label.place(x=30, y=490)

        self.Angle_entry = tk.Entry(self.master, font=font)
        self.Angle_entry.place(x=130, y=490, width=113, height=21)

        self.Object_material_label = tk.Label(self.master, text="Object Material", font=font)
        self.Object_material_label.place(x=150, y=550)

        self.Slope_material_label = tk.Label(self.master, text="Slope Material", font=font)
        self.Slope_material_label.place(x=150, y=590)

        self.Mu_label = tk.Label(self.master, text="Mu", font=font)
        self.Mu_label.place(x=30, y=630)

        self.mass_comboBox = ttk.Combobox(self.master, font=font)
        self.mass_comboBox.place(x=250, y=450, width=91, height=21)

        self.angle_comboBox = ttk.Combobox(self.master, font=font)
        self.angle_comboBox.place(x=250, y=490, width=91, height=21)

        self.Object_comboBox = ttk.Combobox(self.master, font=font)
        self.Object_comboBox.place(x=250, y=550, width=91, height=21)

        self.Slope_comboBox = ttk.Combobox(self.master, font=font)
        self.Slope_comboBox.place(x=250, y=590, width=91, height=21)
	








        self.Mu_entry = tk.Entry(self.master, font=font)
        self.Mu_entry.place(x=210, y=630, width=121, height=21)

        self.angle_slider = tk.Scale(self.master, from_=0, to=100, orient='horizontal', font=font)
        self.angle_slider.place(x=30, y=520, width=301, height=25)

        self.Distance_label = tk.Label(self.master, text="Distance", font=font)
        self.Distance_label.place(x=560, y=490)

        self.comboBox_distance = ttk.Combobox(self.master, font=font)
        self.comboBox_distance.place(x=800, y=490, width=91, height=21)

        self.Distance_entry = tk.Entry(self.master, font=font)
        self.Distance_entry.place(x=680, y=490, width=113, height=21)

        self.Time_entry = tk.Entry(self.master, font=font)
        self.Time_entry.place(x=680, y=610, width=113, height=21)

        self.Time_label = tk.Label(self.master, text="Time", font=font)
        self.Time_label.place(x=560, y=610)

        self.comboBox_time = ttk.Combobox(self.master, font=font)
        self.comboBox_time.place(x=800, y=610, width=91, height=21)

        self.u_entry = tk.Entry(self.master, font=font)
        self.u_entry.place(x=680, y=530, width=113, height=21)

        self.v_label = tk.Label(self.master, text="v", font=font)
        self.v_label.place(x=560, y=570)

        self.u_label = tk.Label(self.master, text="u", font=font)
        self.u_label.place(x=560, y=530)







        self.comboBox_initial_v = ttk.Combobox(self.master, font=font)
        self.comboBox_initial_v.place(x=800, y=530, width=91, height=21)

        self.v_entry = tk.Entry(self.master, font=font)
        self.v_entry.place(x=680, y=570, width=113, height=21)

        self.comboBox_final_v = ttk.Combobox(self.master, font=font)
        self.comboBox_final_v.place(x=800, y=570, width=91, height=21)

        self.Additional_features_label = tk.Label(self.master, text="Additional Features", font=font)
        self.Additional_features_label.place(x=560, y=430)

        self.Features_label = tk.Label(self.master, text="Features", font=font)
        self.Features_label.place(x=30, y=430)

        self.mass_button = tk.Button(self.master, text="Mass", font=font, bg="#FF6C69", fg="black")
        self.mass_button.place(x=210, y=10, width=81, height=21)

        self.Angle_button = tk.Button(self.master, text="Angle", font=font, bg="#FF6C69", fg="black")
        self.Angle_button.place(x=300, y=10, width=81, height=20)

        self.Mu_button = tk.Button(self.master, text="Mu", font=font, bg="#FF6C69", fg="black")
        self.Mu_button.place(x=390, y=10, width=171, height=21)

        self.Acceleration_button = tk.Button(self.master, text="Acceleration", font=font, bg="#FF6C69", fg="black")
        self.Acceleration_button.place(x=570, y=10, width=131, height=21)

        self.Answers_frame = tk.Frame(self.master, bg="#F2F4ED")
        self.Answers_frame.place(x=710, y=40, width=191, height=363)

        self.Compute_down_button = tk.Button(self.master, text="Compute Down", font=font, bg="#E980FF", fg="black")
        self.Compute_down_button.place(x=30, y=660, width=151, height=32)

        self.Compute_additional_down_button = tk.Button(self.master, text="Compute Additional Down", font=font, bg="#63DBFF", fg="black")
        self.Compute_additional_down_button.place(x=560, y=640, width=161, height=51)

        self.Compute_up_button = tk.Button(self.master, text="Compute Up", font=font, bg="#81DE91", fg="black")
        self.Compute_up_button.place(x=190, y=660, width=151, height=32)



        self.Compute_additional_up = tk.Button(self.master, text="Compute", font=font, bg='#FFB83E', fg='black', relief='solid', borderwidth=1)
        self.Compute_additional_up.place(x=730, y=640, width=161, height=51)

        self.mgcos_theta = tk.Label(self.master, text="mgcos_theta", font=font)
        self.mgcos_theta.place(x=590, y=310)

        self.Reaction_force = tk.Label(self.master, text="Reaction_force", font=font)
        self.Reaction_force.place(x=360, y=50)

        # self.material = tk.Label(self.master)
        # self.material.place(x=340, y=120, width=181, height=141)
        # material_image = tk.PhotoImage(file="Downloads/rubber.jpg")
        # self.material.config(image=material_image)
        # self.material.image = material_image

        self.material = tk.Label(self.master)
        self.material.place(x=340, y=120, width=181, height=141)
        material_image = Image.open("Downloads/rubber.jpg")
        material_image = material_image.resize((181, 141), Image.ANTIALIAS)
        material_photo = ImageTk.PhotoImage(material_image)
        self.material.config(image=material_photo)
        self.material.image = material_photo




        # self.diagram = tk.Label(self.master)
        # self.diagram.place(x=10, y=40, width=691, height=363)
        # diagram_image = tk.PhotoImage(file="Downloads/final_design.png")
        # # diagram_image_resized = diagram_image.resize((691, 363), Image.ANTIALIAS)
        # self.diagram.config(image=diagram_image_resized)
        # self.diagram.image = diagram_image
	
        image = Image.open("Downloads/final_design.png")
        image = image.resize((691, 363), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)

        # Create a Label widget with the PhotoImage object
        self.diagram = tk.Label(self.master, image=photo)
        self.diagram.image = photo  # Keep a reference to the image to prevent garbage collection
        self.diagram.place(x=10, y=40, width=691, height=363)

        self.weight = tk.Label(self.master, text="weight", font=font)
        self.weight.place(x=340, y=330)

        self.mgsin_theta = tk.Label(self.master, text="mgsin_theta", font=font)
        self.mgsin_theta.place(x=200, y=230)

        self.theta = tk.Label(self.master, text="theta", font=font)
        self.theta.place(x=130, y=360)

        self.acc_answer = tk.Label(self.master, text="acc_answer", font=font)
        self.acc_answer.place(x=150, y=110)

        self.frictional_force = tk.Label(self.master, text="frictional_force", font=font)
        self.frictional_force.place(x=550, y=100)

        self.Suvat_ans_label = tk.Label(self.master, text="Suvat_ans_label", font=font, anchor="center")
        self.Suvat_ans_label.place(x=710, y=10)

        self.title_label = tk.Label(self.master, text="title_label", font=font)
        self.title_label.place(x=10, y=10)

        self.Background_1 = tk.Label(self.master, bg='#FFFFFF', relief='solid', borderwidth=0)
        self.Background_1.place(x=10, y=420, width=351, height=281)

        self.Background_2 = tk.Label(self.master, bg='#FFFFFF', relief='solid', borderwidth=0)
        self.Background_2.place(x=550, y=420, width=351, height=281)

        # self.Arrow = tk.Label(self.master)
        # self.Arrow.place(x=380, y=500, width=151, height=51)
        # arrow_image = tk.PhotoImage(file="Downloads/red arrow.png")
        # self.Arrow.config(image=arrow_image)
        # self.Arrow.image = arrow_image

        self.Arrow = tk.Label(self.master)
        self.Arrow.place(x=380, y=500, width=151, height=51)
        arrow_image = Image.open("Downloads/red arrow.png")
        arrow_image = arrow_image.resize((151, 51), Image.ANTIALIAS)
        arrow_photo = ImageTk.PhotoImage(arrow_image)
        self.Arrow.config(image=arrow_photo)
        self.Arrow.image = arrow_photo

        self.arrow_explanation = tk.Label(self.master, text="arrow_explanation", font=font, bg='#FFFFFF', fg="black", wraplength=135, justify='left')
        self.arrow_explanation.place(x=380, y=570, width=151, height=81)


        # Raise method in Tkinter is called lift()
        self.Background_2.lift()
        self.Background_1.lift()
        self.material.lift()
        self.diagram.lift()
        self.Mass_label.lift()
        self.Mass_entry.lift()
        self.Angle_label.lift()
        self.Angle_entry.lift()
        self.Object_material_label.lift()
        self.Slope_material_label.lift()
        self.Mu_label.lift()
        self.mass_comboBox.lift()
        self.angle_comboBox.lift()
        self.Object_comboBox.lift()
        self.Slope_comboBox.lift()
        self.Mu_entry.lift()
        self.angle_slider.lift()
        self.Distance_label.lift()
        self.comboBox_distance.lift()
        self.Distance_entry.lift()
        self.Time_entry.lift()
        self.Time_label.lift()
        self.comboBox_time.lift()
        self.u_entry.lift()
        self.v_label.lift()
        self.u_label.lift()
        self.comboBox_initial_v.lift()
        self.v_entry.lift()
        self.comboBox_final_v.lift()
        self.Additional_features_label.lift()
        self.Features_label.lift()
        self.mass_button.lift()
        self.Angle_button.lift()
        self.Mu_button.lift()
        self.Acceleration_button.lift()
        self.Answers_frame.lift()
        self.Compute_down_button.lift()
        self.Compute_additional_down_button.lift()
        self.Compute_up_button.lift()
        self.Compute_additional_up.lift()
        self.weight.lift()
        self.mgsin_theta.lift()
        self.Reaction_force.lift()
        self.mgcos_theta.lift()
        self.theta.lift()
        self.acc_answer.lift()
        self.frictional_force.lift()
        self.Suvat_ans_label.lift()
        self.title_label.lift()
        self.Arrow.lift()
        self.arrow_explanation.lift()

        # Create the scrollable text widget using tkinter Text widget
        self.scrollAreaWidgetContents = tk.Text(self.master, wrap=tk.WORD, font=("Arial", 14), bg="white", fg="black", bd=0, padx=4, pady=4)
        self.scrollAreaWidgetContents.place(x=710, y=40, width=191, height=363)
	
        self.mass_comboBox['values'] = ("kg", "mg", "g", "oz", "lb", "tonne")
        self.angle_comboBox['values'] = ("deg", "rad")
        self.Object_comboBox['values'] = ("wood", "steel", "rubber", "glass", "polyethylene", "concrete")
        self.Slope_comboBox['values'] = ("wood", "steel", "rubber", "glass", "polyethylene", "concrete")
        self.comboBox_distance['values'] = ("m", "mm", "cm", "km", "inch", "yard", "ft", "mile")
        self.comboBox_time['values'] = ("s", "ms", "min", "hour")
        self.comboBox_initial_v['values'] = ("m/s", "cm/s", "km/h", "mile/h", "ft/s")
        self.comboBox_final_v['values'] = ("m/s", "cm/s", "km/h", "mile/h", "ft/s")
        self.Mu_entry.insert(0, "0.0")

        self.angle_slider.config(command=self.photoScroll_1)
        self.Compute_down_button.config(command=self.calc)
        self.Compute_up_button.config(command=self.calc_going_up)
        self.Compute_additional_down_button.config(command=self.calc_additional)
        self.Compute_additional_up.config(command=self.calc_additional_going_up)
        # self.Object_comboBox.bind('<<ComboboxSelected>>', self.calc_mu)
        # self.Slope_comboBox.bind('<<ComboboxSelected>>', self.calc_mu)


        self.mass_button.config(command=self.openMassWindow)
        self.Angle_button.config(command=self.openAngleWindow)
        self.Mu_button.config(command=self.openMuWindow)
        self.Acceleration_button.config(command=self.openAccWindow)

        self.retranslateUi()

    def retranslateUi(self):
        self.master.title("Force Diagram Calculator")
        self.Mass_label.config(text="Mass")
        self.Angle_label.config(text="Angle")
        self.Object_material_label.config(text="Object Material")
        self.Slope_material_label.config(text="Slope Material")
        self.Mu_label.config(text="Coefficient Of Friction (µ)")
        self.Distance_label.config(text="Distance")
        self.Time_label.config(text="Time")
        self.v_label.config(text="Final Velocity (v)")
        self.u_label.config(text="Initial Velocity (u)")
        self.Additional_features_label.config(text="SUVAT Calculator")
        self.Features_label.config(text="Force Diagram Calculator")
        self.mass_button.config(text="Mass?")
        self.Angle_button.config(text="Angle?")
        self.Mu_button.config(text="Coefficient of friction?")
        self.Acceleration_button.config(text="Accelaration?")
        self.Compute_down_button.config(text="Compute acc down")
        self.Compute_additional_down_button.config(text="Compute Aditional \nValues going down")
        self.Compute_up_button.config(text="Compute acc up")
        self.Compute_additional_up.config(text="Compute Aditional \nValues going up")
        self.mgcos_theta.config(text="0 (N)")
        self.Reaction_force.config(text="0 (N)")
        self.weight.config(text="0 (N)")
        self.mgsin_theta.config(text="0 (N)")
        self.theta.config(text="0 (degrees)")
        self.acc_answer.config(text="0 (m/s²)")
        self.frictional_force.config(text="0 (N)")
        self.Suvat_ans_label.config(text="SUVAT Answers")
        self.title_label.config(text="Force Diagram Calculator")
        self.arrow_explanation.config(text="Once the Accelaration has been calculated, move on to the SUVAT Calculator")



    # def calc_mu(self):
    #     mu = "0"
    #     obj = self.Object_comboBox.get()
    #     slope = self.Slope_comboBox.get()

    #     if obj == "wood":
    #         self.material.setPixmap(QtGui.QPixmap("Downloads/wood.JPG"))

    #     if obj == "steel":
    #         self.material.setPixmap(QtGui.QPixmap("Downloads/rust.jpg"))

    #     if obj == "rubber":
    #         self.material.setPixmap(QtGui.QPixmap("Downloads/rubber.jpg"))

    #     if obj == "glass":
    #         self.material.setPixmap(QtGui.QPixmap("Downloads/glass-2.jpg"))

    #     if obj == "polyethylene":
    #         self.material.setPixmap(QtGui.QPixmap("Downloads/plastic.jpeg"))

    #     if obj == "concrete":
    #         self.material.setPixmap(QtGui.QPixmap("Downloads/concrete.jpg"))   

    #     # ["wood", "steel", "rubber", "glass", "polyethylene", "concrete"]
    #     combinations = [
    #           ["wood", "wood", 0.1],
    #           ["wood", "steel", 0.1],
    #           ["wood", "rubber", 0.5],
    #           ["wood", "glass", 0.2],
    #           ["glass", "glass", 0.3],
    #           ["glass", "rubber", 0.4],
    #           ["rubber", "rubber", 0.9],
    #           ["rubber", "polyethylene", 0.9],
    #           ["rubber", "steel", 0.9],
    #           ["rubber", "concrete", 0.9],
    #           ["polyethylene", "polyethylene", 0.9],
    #           ["polyethylene", "steel", 0.9],
    #           ["polyethylene", "concrete", 0.9],
    #           ["polyethylene", "wood", 0.9],
    #           ["polyethylene", "glass", 0.9],
    #           ["concrete", "concrete", 0.9],
    #           ["concrete", "steel", 0.9],
    #           ["concrete", "glass", 0.9],
    #           ["concrete", "wood", 0.9],
    #           ["steel", "glass", 0.9],
    #           ["steel", "steel", 0.9],

    #     ]

    #     for i in combinations:
    #         if i[0] == obj:
    #             if i[1] == slope:
    #                 mu = str(i[2])
    #         elif i[0] == slope:
    #             if i[1] == obj:
    #                 mu = str(i[2])

    #     self.Mu_lineEdit.setText(str(mu))



    def photoScroll_1(self, value):
        # print("scrolled")
        value = round((float(value)/100)*90)
        if value == 89:
            value = 90

        # print("degrees:", value)
        # self.Angle_entry.setText(str(value))
        self.Angle_entry.delete(0, 'end')
        self.Angle_entry.insert(0, str(value))

        # self.theta.setText(f"{value} (degrees)")
        self.theta.config(text=f"{value} (degrees)")

        # self.theta.delete(0, 'end')
        # self.theta.insert(0, f"{value} (degrees)")

        # self.mgsin_theta.setText(f"{mgsin}")
        # self.mgcos_theta.setText(f"{mgcos}")
        # self.Reaction_force.setText(f"{reaction_F}")
        # self.weight.setText(f"{mass*9.81}")



    def calc(self):
        accelaration = ""
        try:
            #values
            mass = float(self.Mass_entry.get())
            angle = float(self.Angle_entry.get())

            #value correction
            if mass < 0:
                mass = abs(mass)

            if angle < 0:
                angle = abs(angle)

            if angle > 90:
                angle = 90

            #converting the types into their base units
            mass_type = self.mass_comboBox.get()
            angle_type = self.angle_comboBox.get()
	    
            mass = convert_mass(mass, mass_type)
            print("converted mass", mass)

            mu = float(self.Mu_entry.get())

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
            self.scrollAreaWidgetContents.delete("1.0", "end")
            self.scrollAreaWidgetContents.insert("1.0", x)

            self.theta.config(text=f"{round(angle, 2)} (degrees)")
            self.mgsin_theta.config(text=f"{round(mgsin, 2)} (N)")
            self.mgcos_theta.config(text=f"{round(mgcos, 2)} (N)")
            self.Reaction_force.config(text=f"{round(reaction_F, 2)} (N)")
            self.weight.config(text=f"{round(mass*9.81, 2)} (N)")
            self.acc_answer.config(text=f"{round(accelaration, 2)} (m/s²)")
            self.frictional_force.config(text=f"{round(mgcos * mu, 2)} (m/s²)")
            return accelaration
        
        except:
            x = f"Accelaration (m/s²): {accelaration}"
            self.scrollAreaWidgetContents.delete("1.0", "end")
            self.scrollAreaWidgetContents.insert("1.0", x)
            self.acc_answer.config(text=f"{accelaration}")
            return accelaration #round to 2 dp



    def calc_going_up(self):
        accelaration = ""
        try:
            #values
            mass = float(self.Mass_entry.get())
            angle = float(self.Angle_entry.get())

            #value correction
            if mass < 0:
                mass = abs(mass)

            if angle < 0:
                angle = abs(angle)

            if angle > 90: #cant have angle less than 0
                angle = 90

            #converting the types into their base units
            mass_type = self.mass_comboBox.get()
            angle_type = self.angle_comboBox.get()
            mass = convert_mass(mass, mass_type)
            print("converted mass", mass)
            mu = float(self.Mu_entry.get())

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
            self.scrollAreaWidgetContents.delete("1.0", "end")
            self.scrollAreaWidgetContents.insert("1.0", x)

            self.theta.config(text=f"{round(angle, 2)} (degrees)")
            self.mgsin_theta.config(text=f"{round(mgsin, 2)} (N)")
            self.mgcos_theta.config(text=f"{round(mgcos, 2)} (N)")
            self.Reaction_force.config(text=f"{round(reaction_F, 2)} (N)")
            self.weight.config(text=f"{round(mass*9.81, 2)} (N)")
            self.acc_answer.config(text=f"{round(accelaration, 2)} (m/s²)")
            self.frictional_force.config(text=f"{round(mgcos * mu, 2)} (m/s²)")
            return accelaration
        
        except:
            self.scrollAreaWidgetContents.delete("1.0", "end")
            self.scrollAreaWidgetContents.insert("1.0", f"Accelaration (m/s²): {accelaration} (m/s²)")
            self.acc_answer.config(text=f"{accelaration} (m/s²)")
            return accelaration







    def calc_additional(self):
        print("these are the required forces")
        accelaration_down_slope = self.calc()
        print(accelaration_down_slope)

        #Values
        distance = str(self.Distance_entry.get())
        time = str(self.Time_entry.get())
        initial_velocity = str(self.u_entry.get())
        final_velocity = str(self.v_entry.get())

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
        dis_type = str(self.comboBox_distance.get())
        time_type = str(self.comboBox_time.get())
        u_type = str(self.comboBox_initial_v.get())
        v_type = str(self.comboBox_final_v.get())

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

            self.scrollAreaWidgetContents.delete("1.0", "end")
            self.scrollAreaWidgetContents.insert("1.0", x)
            self.acc_answer.config(text=f"{accelaration_down_slope} (m/s²)")
		


    def calc_additional_going_up(self):
        print("these are the required forces")
        accelaration_up_slope = self.calc_going_up() #this is the only change to this function
        print(accelaration_up_slope)

        #Values
        distance = str(self.Distance_entry.get())
        time = str(self.Time_entry.get())
        initial_velocity = str(self.u_entry.get())
        final_velocity = str(self.v_entry.get())

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
        dis_type = str(self.comboBox_distance.get())
        time_type = str(self.comboBox_time.get())
        u_type = str(self.comboBox_initial_v.get())
        v_type = str(self.comboBox_final_v.get())

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

            self.scrollAreaWidgetContents.delete("1.0", "end")
            self.scrollAreaWidgetContents.insert("1.0", x)
            self.acc_answer.config(text=f"{accelaration_up_slope} (m/s²)")







if __name__ == "__main__":
    root = tk.Tk()
    app = Ui_Mass(master=root)
    app.mainloop()
