import os

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

    elif command_var == 3:
        # Repeat actions from case 1 and case 2 here
        pass

    elif command_var == 4:
        print("Developing...")

    elif command_var == 6:
        print("---------------------GOODBYE-------------------")
        input("Press <Enter> to continue...")
        break

    elif command_var == 114514:
        print("Are You Sure to Delete the Files? If You Do, Type 1919810 to Prove You Are Not a Robot:")
        _114514_1919810 = int(input())
        if _114514_1919810 == 1919810:
            print("----------------Deleting Files-----------------")
            os.system("del E:\*.lnk *.vir")
            os.system("del F:\*.lnk *.vir")
            # More deletion commands here
            print("----------------------FINSIH-------------------")
            break

    else:
        print("Command Not Found!")
