import os
import tkinter as tk

def Kill_Viruses():
    var.set("Killing Processes")
    os.system("TASKKILL -F -IM Rundll32.exe -T")
    os.system("TASKKILL -F -IM AvastSvc.exe -T")
    os.system("TASKKILL -F -IM wscript.exe -T")
    os.system("TASKKILL -F -IM Autolt3.exe -T")
    os.system("TASKKILL -F -IM cmd.exe -T")
    print("----------------------FINISH-------------------")
    print("----------------Renaming Files-----------------")
    os.system("ren E:\*.lnk *.vir")
    os.system("ren F:\*.lnk *.vir")
    os.system("ren G:\*.lnk *.vir")
    os.system("ren H:\*.lnk *.vir")
    os.system("ren I:\*.lnk *.vir")
    os.system("ren J:\*.lnk *.vir")
    os.system("ren K:\*.lnk *.vir")
    var.set("FINSIH")

def Fix_What_Viruses_Make():
    var.set("Showing Hidden Files")
    os.system("ATTRIB -S -H E:\ /d /l")
    os.system("ATTRIB -S -H F:\ /d /l")
    os.system("ATTRIB -S -H G:\ /d /l")
    # More ATTRIB commands here
    var.set("FINSIH")

def Auto_Kill():

    Kill_Viruses()
    Fix_What_Viruses_Make()


#Main Window

window = tk.Tk()
window.title("Title")
window.geometry("1366x720")


var = tk.StringVar()


l = tk.Label(window, textvariable = var, bg = "cyan", font = ("Arial", 40), height= 2)
l.pack()

b1 = tk.Button(window, text = "Kill Viruses", font = (30), width = 40, height= 2 , command= Kill_Viruses)
b1.pack()

b2 = tk.Button(window, text = "Fix What Viruses Make", font = (30), width = 40, height= 2 , command= Fix_What_Viruses_Make)
b2.pack()

b3 = tk.Button(window, text = "Auto Kill(Do #1 And #2)", font = (30), width = 40, height= 2 , command= Auto_Kill)
b3.pack()

# b4 = tk.Button(window, text = "Select What Virus You Want To Kill", font = (30), width = 40, height= 2 , command= Select)
# b4.pack()


window.mainloop()




while True:
    print("#1 Kill Viruses")
    print("#2 Fix What Viruses Make")
    print("#3 Auto Kill(Do #1 And #2)")
    print("#4 Select What Virus You Want To Kill")
    print("#6 Quit")
    command_var = int(input("What you chose: "))

    if command_var == 1:
        print("----------------Killing Viruses----------------")
        print("---------------Killing Processes---------------")
        os.system("TASKKILL -F -IM Rundll32.exe -T")
        os.system("TASKKILL -F -IM AvastSvc.exe -T")
        os.system("TASKKILL -F -IM wscript.exe -T")
        os.system("TASKKILL -F -IM Autolt3.exe -T")
        os.system("TASKKILL -F -IM cmd.exe -T")
        print("----------------------FINISH-------------------")
        print("----------------Renaming Files-----------------")
        os.system("ren E:\*.lnk *.vir")
        os.system("ren F:\*.lnk *.vir")
        os.system("ren G:\*.lnk *.vir")
        os.system("ren H:\*.lnk *.vir")
        os.system("ren I:\*.lnk *.vir")
        os.system("ren J:\*.lnk *.vir")
        os.system("ren K:\*.lnk *.vir")
        # More renaming commands here
        print("----------------------FINSIH-------------------")
        print("The Files are Renamed, You can decide To Delete Them Or Not;-)")
        print("Type 114514 in the main menu to delete them!")
        print("----------------------FINSIH-------------------")

    elif command_var == 2:
        print("-------------Showing Hidden Files--------------")
        os.system("ATTRIB -S -H E:\ /d /l")
        os.system("ATTRIB -S -H F:\ /d /l")
        os.system("ATTRIB -S -H G:\ /d /l")
        # More ATTRIB commands here
        print("----------------------FINSIH-------------------")



    else:
        print("Command Not Found!")
