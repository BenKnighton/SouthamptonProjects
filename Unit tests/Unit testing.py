import time

from project_incrament_2 import *

time.sleep(3)
print("importing functions")
time.sleep(2)
print("imported functions")

print("\n\n")




print("\n\nall these functions are converted to base units:")
time.sleep(4)
print("\n\n")

print("50 lb in kg should be 22.67962")
time.sleep(2)
print(convert_mass(50, "lb"), "(kg)")
time.sleep(1)
print("\n\n")

print("40 mm in m should be 0.04")
time.sleep(2)
print(convert_distance(40, "mm"), "(m)")
time.sleep(1)
print("\n\n")

print("5 hours in s should be 18000")
time.sleep(2)
print(convert_time(5, "hour"), "(s)")
time.sleep(1)
print("\n\n")

print("4 mile/h in m/s should be 1.78816")
time.sleep(2)
print(convert_speed(4, "mile/h"), "(m/s)")
time.sleep(1)
print("\n\n")












print("\n\nBigger functions:")
time.sleep(3)
print("\n\n")


function = functions()


print("the accelaration down should 1.0 m/s², if mass = 30, angle = 36, mu = 0.6")
time.sleep(2)
print("Accelaration down the slope", function.calc(mass = 30, angle = 36, mu = 0.6), "m/s²\n")
time.sleep(1)
print("\n\n")

print("the accelaration up should -2 m/s², if mass = 50, angle = 5, mu = 0.1")
time.sleep(2)
print("Accelaration up the slope", function.calc_going_up(mass = 50, angle = 5, mu = 0.1), "m/s²\n")
time.sleep(1)
print("\n\n")


print("the accelaration down should be 8.25 m/s² \nthe distance should be : 1.88 \nthe initial velocity should be: -2.25")
time.sleep(2)
print("SUVAT going down", function.calc_additional(mass = 1, angle = 60, mu = 0.05, distance = "-10", time = "1", initial_velocity = "", final_velocity = "6", dis_type = "m", time_type = "s", u_type = "m/s", v_type = "m/s"), "\n")
time.sleep(1)
print("\n\n")

print("the accelaration up should be -12 m/s² \nthe distance should be: 1.0 (m) \nthe final velocity should be: -5.0 (m/s)")
time.sleep(2)
print("SUVAT going up", function.calc_additional_going_up(mass = -1, angle = 70, mu = 0.7, distance = "10", time = "1", initial_velocity = "7", final_velocity = "", dis_type = "m", time_type = "s", u_type = "m/s", v_type = "m/s"), "\n")
time.sleep(1)
print("\n\n")













print("\n\nprint 8 tests\n\n")



if convert_mass(50, "lb") == 22.67962000039049:
    print("test 1 passed")
else: 
    print("test 1 failed")



# print("40 mm in m should be 0.04")
# print(convert_distance(40, "mm"), "(m)")

if convert_distance(40, "mm") == 0.04:
    print("test 2 passed")
else: 
    print("test 2 failed")


# print("5 hours in s should be 18000")
# print(convert_time(5, "hour"), "(s)")

if convert_time(5, "hour") == 18000.0:
    print("test 3 passed")
else: 
    print("test 3 failed")





# print("4 mile/h in m/s should be 1.78816")
# print(convert_speed(4, "mile/h"), "(m/s)")

if convert_speed(4, "mile/h") == 1.7881602334622 :
    print("test 4 passed")
else: 
    print("test 4 failed")









function = functions()


# print("the accelaration down should 1.0 m/s², if mass = 30, angle = 36, mu = 0.6")

if function.calc(mass = 30, angle = 36, mu = 0.6) == 1.0:
    print("test 5 passed")
else: 
    print("test 5 failed")





# print("the accelaration up should -2 m/s², if mass = 50, angle = 5, mu = 0.1")


if function.calc_going_up(mass = 50, angle = 5, mu = 0.1) == -2:
    print("test 6 passed")
else: 
    print("test 6 failed")




# print("the accelaration down should be 8.25 m/s² \nthe distance should be : 1.88 \nthe initial velocity should be: -2.25")

if function.calc_additional(mass = 1, angle = 60, mu = 0.05, distance = "-10", time = "1", initial_velocity = "", final_velocity = "6", dis_type = "m", time_type = "s", u_type = "m/s", v_type = "m/s") == 8.25:
    print("test 7 passed")
else: 
    print("test 7 failed")







# print("the accelaration up should be -12 m/s² \nthe distance should be: 1.0 (m) \nthe final velocity should be: -5.0 (m/s)")

if function.calc_additional_going_up(mass = -1, angle = 70, mu = 0.7, distance = "10", time = "1", initial_velocity = "7", final_velocity = "", dis_type = "m", time_type = "s", u_type = "m/s", v_type = "m/s") == -12:
    print("test 8 passed")
else: 
    print("test 8 failed")


# print(function.calc_additional(mass = 1, angle = 60, mu = 0.05, distance = "-10", time = "1", initial_velocity = "", final_velocity = "6", dis_type = "m", time_type = "s", u_type = "m/s", v_type = "m/s"))
# print(function.calc_additional_going_up(mass = -1, angle = 70, mu = 0.7, distance = "10", time = "1", initial_velocity = "7", final_velocity = "", dis_type = "m", time_type = "s", u_type = "m/s", v_type = "m/s"))