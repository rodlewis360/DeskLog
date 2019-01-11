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
    
    
while True:
    print("What would you like to do?")
    whattodo = input("")
    if whattodo == "new log":
        Log = Logprocessstart()
        logsfilled += 1
        LogList.append(Log)
        Log.append(logsfilled)
    if whattodo == "open":
        print("What log would you like to open?")
        whattodo = input("")
        x = 0
        thislog = ""
        for a in Loglist:
            if a == whattodo:
                thislog = LogList[x + 1]
                logprocess(thislog)
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
            if a == whattodo:
                thislog = LogList[x + 1]
            x += 1
        if thislog == "":
            print("Error: Log with name:",fileone,"not found")
        thislogone = ""
        xa = 0
        for a in LogList:
            if a == whattodo:
                thislogone = LogList[xa + 1]
            xa += 1
        if thislogone == "":
            print("Error: Log with name:", filetwo, "not found")
        thislog += thislogone
        LogList[x] = thislog
