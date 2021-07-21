import time
import os
import shutil as sh

def deleteFiles():
    seconds = time.time()
    p = input("Please Enter the Path of your file folder = ")
    path = str(p)
    a = os.path.exists(path)
    while(a == False):
        print("The Path Does not Exist")
        print("Please Enter the Path Again")
        p = input("Please Enter the Path of your file folder = ")
        path = str(p)
        a = os.path.exists(path)
    d = input("Please Tell that how much days old files you have to keep = ")
    desiredDays = d
    print("Please Conform your Path and Days")
    print("Your Path is " + path)
    c = input("Path is Correct(True/False) = ")
    print("Your Days are " + desiredDays)
    e = input("Days are Correct(True/False) = ")
    if(c == "True" and e == "True"):
        print("Ok and Thankyou for Deatils")
    elif(c == "True" and e == "False"):
        d = input("Ok and Please again Tell that how much days old files you have to keep = ")
        desiredDays = d
    elif(c == "False" and e == "True"):
        p = input("Ok and Please again Enter the Path of your file folder = ")
        path = str(p)
    else:
        print("Ok and Please Enter your Deatils again")
        p = input("Please again Enter the Path of your file folder = ")
        d = input("Please again Tell that how much days old files you have to keep = ")
        desiredDays = d
        path = str(p)
    desiredDays = int(d)
    check = os.path.isdir(path)
    sec = seconds - (desiredDays * 24 * 60 * 60)
    os.path.exists(path)
    os.walk(path)
    os.path.join(path)
    ctime = os.stat(path).st_ctime
    return ctime
    if(ctime > sec):
        if(check == False):
            os.remove(path)
            print("File have been Removed")
        elif(check == True):
            sh.rmtree()
            print("Folder have been Removed")
     else:
            print("There are no files or folder that is that much old")
deleteFiles()
