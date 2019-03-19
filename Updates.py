def Logprocessstart():
    log = []
    print("What is the name of your log?")
    log.append(input(""))
    print("What would you like to put in",log[0],"?")
    log.append(input(""))
    return log

def logprocess(log):
    print(log)
    print("What would you like to put in",log,"?")
    log += input("")
    return log

def DeskLog():
    import os
    LogList = {}
    if os.path.isfile("DeskLog.txt") == True:
        f = open("DeskLog.txt", "r")
        import ast
        LogList = ast.literal_eval(f)
        f.close()
    while True:
        print("What would you like to do?")
        whattodo = input("")
        if whattodo == "new":
            LogList[input("What name?  ")] = input("What would you like to add?  ")
        if whattodo == "open":
            print("What log would you like to open?")
            whattodo = input("")
            try:
                print(LogList.get(whattodo))
                LogList[whattodo] = LogList.get(whattodo) + "  " + input()
            except NameError:
                print("Error: Log with name:", whattodo, "not found")
        if whattodo == "merge":
            print("What files?(One at a time)")
            fileone = input("")
            filetwo = input("")
            try:
                thislog = LogList.get(fileone)
            except NameError:
                print("Error: log with name", fileone, "not found.")
            try:
                thislogone = LogList.get(filetwo)
            except NameError:
                print("Error: Log with name",filetwo,"not found.")
            try:
                LogList[fileone] = LogList.get(fileone) + Logist.get(filetwo)
            except NameError:
                a = True
            if a == True:
                print("Files succesfully merged!  New name:", fileone, "!")
        if whattodo == "delete":
            print("What log would you like to delete?")
            fileone = input("")
            try:
                del LogList[fileone]
            except NameError:
                print("Error: Log with name", fileone, "not found.)
        if whattodo == "show":
            print("Name")
            for a in LogList:
                print(a)
        if whattodo == "save":
            print("Saving...")
            if os.path.isfile("DeskLog.txt") == True:
                os.remove("DeskLog.txt")
            f = open("DeskLog.txt", "w+")
            f.write(str(LogList))
            os.fsync(f)
            print("File succesfully saved!")
        if whattodo == "exit":
            print("Saving...")
            if os.path.isfile("DeskLog.txt") == True:
                os.remove("DeskLog.txt")
            f = open("DeskLog.txt", "w+")
            f.write(str(LogList))
            os.fsync(f)
            print("File succesfully saved!")
            break
        if whattodo == "cls":
            a = 0
            while a <= 50:
                print(" ")
                a += 1
        if whattodo == 'rename':
            print("What log would you like to rename?")
            whattodo = input()
            x = 0
            LogList[input("What name?  ")] = LogList[whattodo]
            del LogList[whattodo]
    f.close()

DeskLog()
