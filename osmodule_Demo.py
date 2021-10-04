import os

from time import time,ctime

import time
#from datetime import *
#print('before timer')
#time.sleep(5)
#print('after timer')
#os.system("python Arithmetic.py")  #command prompt...run the python python <<

#u can run any DOS commands from Python program --- javac <<filename.java>>
#java <<filename>>
#python <<filename.py>>
#time.sleep(10)  #pausing  the execution few seconds..Selenium web Automation..
#print("Current Directory : ",os.getcwd())
#time.sleep(10)
os.system("python stringmethod.py")

#Absoulte Path vs Relative Path
#Absolute path -- path to the file - full path - <<Drive>>:/folder/subfolder/file
#relative path -- Anmol house is near some famous star/politician/player/place.
"""
os.mkdir("sProgfolder")  # creates new directory Progfolder in CWD
os.mkdir("C:\\sProgfolder")# creates new directory Progfolder  in the spec path


os.makedirs("sdir1/sdir2/sdir3") # creates all 3 directories under CWD


os.rmdir("sProgfolder") # to remove this dir from CWD
os.rmdir("sdir1/sdir2/sdir3") # to remove dir3 directory
#os.rmd("dir1/dir2/dir3") # to remove dir3 directory

os.removedirs("sdir1/sdir2")# to remove all dirtectories includng sub direct
os.rename("C:\\sProgfolder","C:\\sProgramfolder")

os.listdir(".") # list all files/folders in the CWD but excluding subfolers/files

list=os.listdir()  #blank indicates CWD or u can mention any specific path
print(len(list))
for name in list:
    #print(name)
    stats = os.stat(name)
    print("File Name", name)
    print("File size", stats.st_size)
    print("File Owner", stats.st_uid)
    print("group ID Owner", stats.st_gid)
    print("File last accessed time", ctime(stats.st_atime))
    print("File last modified time", ctime(stats.st_mtime))
    print("File last change or Creation time", ctime(stats.st_ctime))

  

# list all files/folders in the CWD but including subfolers/files          
for dirpath,dirnames,filenames in os.walk("."):
    print("Current working Director : ",dirpath)
    print("Directories : ",dirnames)
    print("Files : ",filenames)
    print("*"*80)

#Run other programs from python program or any dos commands using os.sytem()
#os.system("Cmd String") # cmd string - is command we execute from DOS prompt 
#py <<filename.py>
#java <<filename>>
#javac <<filename.java>>


# to get statistics of any file
#f1='C:\\Users\\User\\a.txt'

os.system("python Arithmetic.py")
stats = os.stat('a.txt')
print("File size", stats.st_size)
print("File Owner", stats.st_uid)
print("group ID Owner", stats.st_gid)
print("File last accessed time", ctime(stats.st_atime))
print("File last modified time", ctime(stats.st_mtime))
print("File last change or Creation time", ctime(stats.st_ctime))

#datetime.fromtimestamp(Milliseconds) #- wll return date in format based on ms.
# stat function returns collection of below properties
#st_mode - protection bits
#st_ino - inode number
#st_dev - device
#st_nlink - no of hard links for this file
#st_uid - user id of the owner
#st_gid - group id of the owner
#st_size  - size of the file in bytes.
#st_atime
#st_mtime
#st_ctime - time of most recent meta data change
          
"""
        
