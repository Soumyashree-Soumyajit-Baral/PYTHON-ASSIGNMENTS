import platform
import sys
#x=dir(platform)
#print ("Platform Details : ", x)

#x=dir(sys)
#print ("Sys Details : ", x)

#a=10
#print(sys.id(a))
print("Platform : ", sys.platform)
print("System: ", platform.system())  # e.g. Windows, Linux, Darwin
print("Arch : " , platform.architecture())  # e.g. 64-bit
print("Machine : ", platform.machine())  # e.g. x86_64
print("Node : ", platform.node())  # Hostname
print("Platform : ", platform.platform()) #OS Details
print("Build  : ",platform.python_build()) #Python Build
print("Compiler : ",platform.python_compiler())#Python Compiler
print("Branch : ", platform.python_branch())
print("Implementation : ",platform.python_implementation())
print("Revision  : " ,platform.python_revision())
print("Version : ", platform.python_version()) #Python Version
print("Release : ", platform.release()) # OS Release
print("Processor :",platform.processor())  # e.g. i386
