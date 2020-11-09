import os
import getpass


print("\n\t\t**....................##.........................**")
os.system("tput setaf 3")
print("\n\t*****************WELCOME In MY AUTOMATION TOOL*****************")
os.system("tput setaf 7")
print("\n\t\t**....................##.........................**")


passwd = getpass.getpass("\nEnter your password: ")

if passwd != "root":
    print("\n password is incorrect.Please enter right password. ")
    exit()
os.system("tput setaf 3")
print("\n\tThank You...")
print("\n\t############ You locally logged in successfully  ###########")
os.system("tput setaf 7")


def printme(): 
        ch = int(input(''' 
        \n
        ..............#WELCOME IN MENU LIST#.................
        
        \n
        Press 1 : To see Hard disk information..
        Press 2 : To create a Physical Volume (PV)..
        Press 3 : To create a Volume Group (VG)..
        Press 4 : To create a Logical Volume (LV)..
        Press 5 : To format the Logical Volume (LV)..
        Press 6 : To create a Folder and Mount Logical Volume..
        Press 7 : Exit..
        \n
        What can I help you : '''))
        print("\t\n.........................###...........................\n")
        
        if ch == 1:
           os.system("\n fdisk -l")
           os.system("tput setaf 3")
           anykey=input("\n\t Press Enter to go main menu...>>")
           os.system("tput setaf 7")
           printme()

        elif ch == 2:
           os.system("\n fdisk -l")
           Disk1= input("\n\n\tEnter name of 1 st harddisk that you want >> " )
           os.system("pvcreate {}".format(Disk1))
           os.system("pvdisplay {}".format(Disk1))
           Disk2= input("\n\t Enter name of 2 nd harddisk that you want >> ")
           os.system("pvcreate {}".format(Disk2))
           os.system("pvdisplay {}".format(Disk2))
           os.system("tput setaf 3")
           print("\n\n\t>>>>>>>>>Your two physical volume(PV) created successfully<<<<<<<<<<")
           anykey=input("\n\t Press Enter to go main menu...>>")
           os.system("tput setaf 7")
           printme()

        elif ch == 3:
           os.system("\n fdisk -l")
           Disk1= input("\n\n\tEnter name of 1 st harddisk that you want >> ")
           Disk2= input("\n\tEnter name of 2 nd harddisk that you want >> ")
           name1= input("\n\tGive name to your Volume Group(VG) >> ")
           os.system("pvdisplay {}".format(Disk1))
           os.system("pvdisplay {}".format(Disk2))
           os.system("vgcreate {} {} {}".format(name1,Disk1,Disk2))
           os.system("vgdisplay {}".format(name1))
           os.system("tput setaf 3")
           print("\n\n\t>>>>>>>>>>Your Volume Group(VG) {} created successfully<<<<<<<<< ".format(name1))
           anykey=input("\n\t Press Enter to go main menu...>>")
           os.system("tput setaf 7")
           printme()

        elif ch == 4:
           os.system("\n fdisk -l")
           #Disk1= input("\n\n\t Enter name of 1 st harddisk that you want >> ")
           #Disk2= input("\n\t Enter name of 2 nd harddisk that you want >> ")
           size1= input("\n\t Enter size for your Logical Volume >> ")
           name1= input("\n\t Enter your Volume Group(VG) name >> ")
           name2= input("\n\t Give name to your Logical Volume(LV) >> ")
           #os.system("pvcreate {}".format(Disk1))
           #os.system("pvcreate {}".format(Disk2))
           #os.system("vgcreate {} {} {}".format (name1,Disk1,Disk2))
           os.system("vgdisplay {}".format(name1))
           os.system("lvcreate --size {}G --name {} {} ".format(size1,name2,name1))
           os.system("lvdisplay {}/{}".format(name1,name2))
           os.system("tput setaf 3")
           print("\n\n\t>>>>>>>>>Your Logical Volume(LV) {} created successfully<<<<<<<<<".format(name2))
           anykey=input("\n\t Press Enter to go main menu...>>")
           os.system("tput setaf 7")
           printme()

        elif ch == 5:
           name2= input("\n\n\tEnter the name of Volume Group >> ")
           name3= input("\n\n\tEnter the name of Logical Volume >> ")
           os.system("mkfs.ext4 /dev/{}/{}".format(name2,name3))
           os.system("tput setaf 3")
           print("\n\n\t>>>>>>>>>Your Logical Volume Formated<<<<<<<<")
           anykey=input("\n\t Press Enter to go main menu...>>")
           os.system("tput setaf 7")
           printme()

        elif ch == 6:
           folder1= input("\n\n\t Enter folder name that you want >> ")
           os.system("mkdir {}".format(folder1))
           name2= input("\n\tEnter the name of Volume Group >> ")
           name3= input("\n\tEnter the name of Logical Volume >> ")
           os.system("mount /dev/{}/{} {}".format(name2,name3,folder1))
           os.system("df -hT")
           os.system("tput setaf 3")
           print("\n\n\t>>>>>>>>Your Logical Volume mounted<<<<<<<<")
           anykey=input("\n\t Press Enter to go main menu...>> ")
           os.system("tput setaf 7")
           printme()

        elif ch == 7:
           os.system("exit")
           os.system("tput setaf 3")
           print("\n\n\t#########..THANK YOU..See you soon..#########")
           os.system("tput setaf 7")
           print("\n")


        else:
           print("Incorrect Choice,select correct option..")
           anykey =input("\n\t Press Enter to go main menu")
           printme()
printme()
     






