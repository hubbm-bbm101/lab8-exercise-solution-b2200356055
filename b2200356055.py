# name - İbrahim Enes Köse
# id - 2200356055
# lab 8 exercise

import sys
file = open(sys.argv[1])

data_students = {i.split(":")[0] : (i.split(":")[1].split(",")[0],i.split(":")[1].split(",")[1].strip("\n")) for i in file}

for i in sys.argv[2:]:
    try:
        print("name:{}, University:{},{}".format(i,data_students[i][0],data_students[i][1]),end=" ")
    except:
        print("No record of '{}' was found!".format(i),end=" ")
