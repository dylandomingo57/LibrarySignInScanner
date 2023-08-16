import csv
import datetime
import atexit

counter = 0

# print ("Current date and time = %s" % e)
# print ("Today's date:  = %s/%s/%s" % (e.day, e.month, e.year))
# print ("The time is now: = %s:%s:%s" % (e.hour, e.minute, e.second))

def readBarcode(code):
    found = False
    index = None
    with open("SY 22-23 Student Barcodes.csv") as csvfile:
        csv_reader = csv.reader(csvfile)
        #print("started")
        for row in csv_reader:
            #print("in row")
            for val in row:
                #print("in val")
                if code in val:
<<<<<<< HEAD
                    found = True
                    index = val
    if (found):
        return index
    else:
        return "Not found"

def endProgram():
    f = open("Cheesebread.txt", "a")
    f.write(counter)
    f.close()
=======
                    return(val)
>>>>>>> d3f888b1a8159f4cac7fb59a78f95b7a5ec9ce75


if __name__ == "__main__":
    atexit.register(endProgram)

    print("-------------------------------\n|     Library Appender        |\n-------------------------------\n")
    print("To enter a student's name manually, enter their credentials with \"LastName, FirstName\"")
    print("i.e.\"Domingo, Dylan\"\n")
    print("Enter \"!count\" to view the student count")
    print("Enter \"!exit\" to exit the program\n")

    while (True):

        id = input()
        name = readBarcode(id)
        
        e = datetime.datetime.now()

        if id == "!exit":
            endProgram()
            break

        if id == "!count":
            print("Count: ", counter, "\n")

        if name == "Not found":
            if id !="!count":
                print("Not found, please try again.\n")
        else:
            counter += 1

            f = open("Cheesebread.txt", "a")
            f.write(name)

            f.write("\t%s/%s/%s" % (e.month, e.day, e.year))
            f.write("\t%s:%s:%s" % (e.hour, e.minute, e.second))

            f.write("\n")
            f.close()

            f = open("Cheesebread.txt", "r")
            print(f.read())
    quit()
        
