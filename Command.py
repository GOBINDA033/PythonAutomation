    #Automatic command system
command=input("Enter your command:")
match command:
            case "Start":
                print("System is Starting..........")
            case "Shutdown":
                print("System is shutting down..........")
            case "Restart":
                print("System is restarting..........")
            case "Lock":
                print("System is Locking..........")
            case "Sleep":
                print("System is going to sleep mode..........")
            case _:
                print("Command not recognized")