
# Date = Oct 07th, 2021
# Level = Beginner


print("\n ****  Cartesian Robot  **** \n")


Commands_List = [ "UUU", "UP AND DOWN", "UDLRR", "UULULLULDDR" ]



for Text in Commands_List:

    Command = list(Text)
    
    pos_x = 0
    pos_y = 0
    
    for Comm in Command:

        Comm = Comm.lower()

        if(Comm == "u"):
            pos_y = pos_y + 1

        if(Comm == "d"):
            pos_y = pos_y - 1


        if(Comm == "l"):
            pos_x = pos_x - 1

        if(Comm == "r"):
            pos_x = pos_x + 1


    Position = [pos_x, pos_y]

    print(f" > For command sequence {Text}. Final Position = {Position}")


# Closing

print("\n * \n")


