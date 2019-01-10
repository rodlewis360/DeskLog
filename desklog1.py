LogList = []
Log = []
Logtwo = []
Logthree = []
Logfour = []
Logfive = []
Logsix = []
Logseven = []
Logeight = []
Lognine = []
Logten = []
logsfilled = 0

def Logprocessstart():
    log = []
    print("What is the name of your log?")
    log.append(input(""))
    print("What would you like to put in",log[1],"?")
    
    
while True:
    print("What would you like to do?")
    whattodo = input("")
    if whattodo = "new log":
        Log = Logprocessstart()
        logsfilled += 1
        
