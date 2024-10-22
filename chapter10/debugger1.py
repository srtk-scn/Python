import pdb   # import pdb module
#module-python file contains usefull classes and functions wrote
#by developer


#according to wikipedia --debugging is the process of finding and resolving defects or prblems within a  computer program which prevent
#correct operation of computer software or a system

#why debugging
#1.our programs is not running and causing unexpected errors
#2.our program is working fine but not working the same way we want

#steps for debuggng
#1.import pdb then set trace
#2.execute code line by line



pdb.set_trace()
name=input('enter your name')
age =input('enter you age')
age2=int(age) + 5
print(f"{name} you will be {age2} in next five year")
