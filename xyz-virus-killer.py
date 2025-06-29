import os
import tkinter as tk





def return_values(value):
    if value == 1:
        return "Success"
    elif value == 128:
        return "Error: Fail"
    else:
        return "Error: Please tell developers!!  Fail"
        os.system()

def dir_E():
    if os.path.exists("E:\\"):
        return True
    else:
        return False
    # return False

def dir_F():
    if os.path.exists("F:\\"):
        return True
    else:
        return False

def dir_G():
    if os.path.exists("G:\\"):
        return True
    else:
        return False



def Kill_Viruses():
    Clean()
    # var.set("Killing Processes")
    # print(var.get())
    t.insert("end", "Killing Processes:\n")
    t.insert("end", str(return_values(os.system("TASKKILL -F -IM Rundll32.exe -T")) + " to kill virus\n"))
    t.insert("end", str(return_values(os.system("TASKKILL -F -IM AvastSvc.exe -T")) + " to kill virus\n"))
    t.insert("end", str(return_values(os.system("TASKKILL -F -IM wscript.exe -T")) + " to kill virus\n"))
    t.insert("end", str(return_values(os.system("TASKKILL -F -IM Autolt3.exe -T")) + " to kill virus\n"))
    t.insert("end", str(return_values(os.system("TASKKILL -F -IM cmd.exe -T")) + " to kill virus\n"))
    t.insert("end", "\n")
    var.set("FINSIH")
    Renaming_Files()

def Renaming_Files():

    # var.set("Renaming Files")
    # print(var)
    t.insert("end", "Renaming Files:\n")
    if dir_E():
        t.insert("end", str(return_values(os.system("ren E:\\*.lnk *.vir"))) + " to rename Files in E-disk\n")
    else:
        t.insert("end", "E-disk not found\n")
    if dir_F():
        t.insert("end", str(return_values(os.system("ren F:\\*.lnk *.vir"))) + " to rename Files in E-disk\n")
    else:
        t.insert("end", "F-disk not found\n")
    if dir_G():
        t.insert("end", str(return_values(os.system("ren G:\\*.lnk *.vir"))) + " to rename Files in E-disk\n")
    else:
        t.insert("end", "G-disk not found\n")
    t.insert("end", "\n")
    var.set("FINSIH")


def Fix_What_Viruses_Make():
    # var.set("Showing Hidden Files")
    t.insert("end", "Showing Hidden Files:\n")
    if dir_E():
        os.system("ATTRIB -S -H E:\\*.* /d /l")
        t.insert("end", "Success to show hidden files in E-disk\n")
    else:
        t.insert("end", "E-disk not found\n")
    if dir_F():
        os.system("ATTRIB -S -H F:\\*.* /d /l")
        t.insert("end", "Success to show hidden files in F-disk\n")
    else:
        t.insert("end", "F-disk not found\n")
    if dir_G():
        os.system("ATTRIB -S -H G:\\*.* /d /l")
        t.insert("end", "Success to show hidden files in G-disk\n")
    else:
        t.insert("end", "G-disk not found\n")

    t.insert("end", "\n")
    # More ATTRIB commands here
    var.set("FINSIH")

def Auto_Kill():
    Kill_Viruses()
    Fix_What_Viruses_Make()

def Clean_Button():
    var.set("")
    t.delete("1.0", tk.END)

def Clean():
    t.delete("1.0", tk.END)




#Main window

root = tk.Tk()
root.title("Title")
root.geometry("1366x720")


var = tk.StringVar()

l = tk.Label(root, textvariable = var, bg = "cyan", width = 45, font = ("Arial", 40), height= 2)
l.pack()

b1 = tk.Button(root, text = "Kill Viruses", font =30, width = 40, height= 2, command= Kill_Viruses)
b1.pack()

b2 = tk.Button(root, text = "Fix What Viruses Make", font =30, width = 40, height= 2, command= Fix_What_Viruses_Make)
b2.pack()

b3 = tk.Button(root, text = "Auto Kill(Do #1 And #2)", font =30, width = 40, height= 2, command= Auto_Kill)
b3.pack()

b4 = tk.Button(root, text = "Clean Screen", font = (30), width = 40, height= 2 , command= Clean_Button)
b4.pack()

l0 = tk.Label(root, width = 10, font =20, height= 2)
l0.pack()

l1 = tk.Label(root, text = "Output:", width = 10, font =20, height= 1)
l1.pack()

t = tk.Text(root, height= 25)
t.pack()


root.mainloop()

"""
Copyright © 2030
© 2024-2030 Arthur_xyz版权所有

如果您意外获取了源码，请联系 Arthur_xyz@outlook.com
"""