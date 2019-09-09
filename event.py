import Task
import googlecarender
import os
import datetime
if __name__ == '__main__':
    i = 0
    starttime = ""
    endtime = ""
    os.system("clear")
    while i == 0:
        # googlecarender.main()
        userinput = input("waiting...")
        if (userinput == "a" or userinput == "add"):
            dateadd = input("title,note,due...")
            os.system("clear")
            lstdataadd = dateadd.split()
            if len(lstdataadd) == 3:
                title = lstdataadd[0]
                notes = lstdataadd[1]
                due = lstdataadd[2]
                month, day = due[:2], due[2:4]
            elif len(lstdataadd) == 2:
                title = lstdataadd[0]
                due = lstdataadd[1]
                month, day = due[:2], due[2:4]
                notes = " "
            else:
                continue
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
        if (userinput == "st" or userinput == "start"):
            starttime = datetime.datetime.utcnow().isoformat() + 'Z'
            print("start your task->"+starttime)
        if (userinput == "end" or userinput == "e"):
            endtime = datetime.datetime.utcnow().isoformat() + 'Z'
            title = input("input title...") 
            googlecarender.main(starttime,endtime,title)