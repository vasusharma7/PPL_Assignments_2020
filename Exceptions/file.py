import io
#file handling exeptions


"""NO file exists"""
file = input("Enter file name - ")    #enter file that does not exist
try:
    fp = open(file) 
except IOError as  i:
   print("Oops Error ! ",i) 


"""Trying to do a file operation which is not permitted
   Example - writing a file in /bin/temp.txt directory
"""
file = input("Enter file path in root directory - ") #example input /bin/temp.txt
try:
    fp = open(file,"w")
    fp.write("Overwrire")
except PermissionError as p:
   print("Run with sudo : Operation not permitted !",p) 


"""Open a file  in read  mode and try to write and vice verca"""
file = input("Specify File Path - ")
try:
    fp = open(file,"w")
    contents = fp.read()
    print(contents)
except io.UnsupportedOperation as k:
    print("Unsupported Operation : try opening file in some other mode -:-",k)


"""Some other Exceptions"""

dictionary = {1:"a",2:"b"}

try:
    print(dictionary[3])
except KeyError as k:
    print("Key Doesn't Exist in dictionary",k)
finally:
    print("Adding key ....")
    dictionary[3] = 'c'
    print(dictionary[3])


l = [4,6,8]
try:
    l.pop(4)
except IndexError as e:
    print("No such index to POP! - ",e)

