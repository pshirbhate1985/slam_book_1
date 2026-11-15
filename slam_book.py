import sys
def initial_slambook():
    rows, cols = int(input("Please enter number of rows/repetaion: ")), 5
    slam_book = []
    print(slam_book)

    for i in range(rows):
        print("\nEnter contact %d details in the following order (ONLY): " % (i+1))
        print("NOTE: * indicates mandatory fields")
        print ("....................................................................................................................................................")

        temp = []
        for j in range(cols):
            if j == 0:
                temp.append(str(input("Enter name*: ")))
                if temp[j] == '' or temp[j] == ' ':
                    sys.exit("Name is a mandatory field .... exiting due to blank field..." )
            if j == 1:
                temp.append(int(input("Enter phone number*: ")))
                
            if j == 2:
                temp.append(str(input("Enter something about your friend: ")))
                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None

            if j == 3:
                temp.append(str(input("Enter date of birth(dd/mm/yy): ")))
                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None

            if j == 4:
                temp.append(
                    str(input("Enter category(Family/Friends/Work/Others): "))
                )
                       
    print("**********************************************************************")

initial_slambook()