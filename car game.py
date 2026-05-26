command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("Car has already stopped!")
        else:
            started = False
            print("Car stopped")
    elif command == 'help':
        print("""
 start - start a new car
 stop - stop the car
 quit - exit the program
 """)
    elif command == "quit":
        break
    else:
        print("I don't know what you mean")