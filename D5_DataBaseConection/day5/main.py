from insert import insertdata
from update import updatedata

obj = insertdata()
obj = updatedata()

print("_____________student Management System__________")
print("For Insertion Press 1, Updation Press 2 \nDelection Press 3, Reading Press 4")

num = int(input("Enter your Option:"))

if num == 1:
    print("Choose 1 for student: \nChoose 2 for Course \nChoose 3 for Transaction")
    n = int(input("Please Enter your option:"))
    if n == 1:
        sid = int(input("Enter your Id:"))
        sname = input("Enter your name:")
        email = input("Enter your email:")
        city = input("Enter your city:")
        obj.insertstudent(sid,sname,email,city)

    elif n == 2:
        cid = int(input("Enter course id:"))
        coursename = input("Enter coursename:")
        sid = int(input("Enter student id:"))
        price = input("Enter price of course:")
        obj.insertcourse(cid,coursename,sid,price)

    else:
        tid = int(input("Enter Transaction id:"))
        sid = int(input("Enter student id:"))
        cid = int(input("Enter course id:"))
        price = input("Enter Transaction price:")
        obj.inserttranscation(tid,sid,cid,price)

elif num == 2:
    print("Choose 1 for Student: \nChoose 2 for Course \nChoose 3 for Transaction")
    n = int(input("Please Enter your option:"))
    if n == 1:
        sid = int(input("Enter your Id:"))
        sname = input("Enter your name:")
        email = input("Enter your email:")
        city = input("Enter your city:")
        obj.updatestudent(sid,sname,email,city)

    elif n == 2:
        cid = int(input("Enter course id:"))
        coursename = input("Enter course name:")
        sid = int(input("Enter student id:"))
        price = input("Enter price:")
        obj.updatecourse(cid,coursename,sid,price)

    else:
        tid = int(input("Enter transaction id:"))
        sid = int(input("Enter student id:"))
        cid = int(input("Enter course id:"))
        price = input("Enter transaction price:")
        obj.updatetranscation(tid,sid,cid,price)