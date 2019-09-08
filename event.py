import Task
import os
if __name__ == '__main__':
    i = 0
    while i == 0:
        userinput = input("waiting...")
        if (userinput == "a"):
            dateadd = input("title,note,due...")
            os.system("clear")
            lstdataadd = dateadd.split()
            title = lstdataadd[0]
            notes = lstdataadd[1]
            due = lstdataadd[2]
            month, day = due[:2], due[2:4]
            Task.setTask(title, notes, month, day)
            os.system("clear")
            print("task seted")
            Task.getTask()
        if (userinput == "s"):
            os.system("clear")
            Task.getTask()
        if (userinput == "d"):
            pos = input("id...")
            os.system("clear")
            Task.deleteTask(pos)
            print("task cleared")
            Task.getTask()
        if (userinput == "0"):
            i = 1