Log = []
LogList = []
logsfilled = 0

def Logprocessstart():
    log = []
    print("What is the name of your log?")
    log.append(input(""))
    print("What would you like to put in",log[0],"?")
    log.append(input(""))
    return log

def logprocess(log):
    print(log)
    print("What would you like to put in your log?")
    log += input("")
    return log

def DeskLog(logsfilled):
    while True:
        print("What would you like to do?")
        whattodo = input("")
        if whattodo == "new":
            Log = Logprocessstart()
            logsfilled += 1
            LogList.append(Log)
            Log.append(logsfilled)
        if whattodo == "open":
            print("What log would you like to open?")
            whattodo = input("")
            x = 0
            thislog = ""
            for a in LogList:
                if len(a) != 0:
                    if a[0] == whattodo:
                        thislog = a[1]
                        thislog = logprocess(thislog)
                        LogList[x] = [a[0], thislog, a[2]]
                        break
                x += 1
            if thislog == "":
                print("Error: Log with name:", whattodo, "not found")
        if whattodo == "merge":
            print("What files?(One at a time)")
            fileone = input("")
            filetwo = input("")
            thislog = ""
            x = 0
            for a in LogList:
                if len(a) != 0:
                    if a[0] == whattodo:
                        thislog = a[1]
                        break
                x += 1
            if thislog == "":
                print("Error: log with name", fileone, "not found.")
            thislogone = ""
            for a in LogList:
                if len(a) != 0:
                    if a[0] == whattodo:
                        thislogone = a[1]
                        thislog += thislogone
                        if thislog != "":
                            LogList[x] = [a[0], thislog, a[2]]
                        break
            if thislogone == "":
                print("Error: Log with name",filetwo,"not found.")
        if whattodo == "delete":
            print("What log would you like to delete?")
            fileone = input("")
            x = 0
            for a in LogList:
                if len(a) != 0:
                    if a[0] == fileone:
                        LogList[x] = ""
                x += 1
        if whattodo == "show":
            print("Name                                        ID")
            for a in LogList:
                if len(a) > 2:
                    print(a[0],"                                   ",a[2])
