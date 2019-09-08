import Task
import os
if __name__ == '__main__':
    i = 0
    os.system("clear")
    while i == 0:
        userinput = input("waiting...")
        if (userinput == "a" or userinput == "add"):
            dateadd = input("title,note,due...")
            os.system("clear")
            lstdataadd = dateadd.split()
            title = lstdataadd[0]
            notes = lstdataadd[1]
            due = lstdataadd[2]
            month, day = due[:2], due[2:4]
            os.system("clear")
            Task.setTask(title, notes, month, day)
            Task.getTask()
        if (userinput == "s" or userinput == "show"):
            os.system("clear")
            Task.getTask()
        if (userinput == "d" or userinput == "delete"):
            pos = input("id...")
            os.system("clear")
            Task.deleteTask(pos)
            Task.getTask()
        if (userinput == "0"):
            i = 1