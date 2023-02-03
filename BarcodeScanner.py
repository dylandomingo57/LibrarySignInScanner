import csv
import datetime

# print ("Current date and time = %s" % e)
# print ("Today's date:  = %s/%s/%s" % (e.day, e.month, e.year))
# print ("The time is now: = %s:%s:%s" % (e.hour, e.minute, e.second))

def readBarcode(code):
    with open("SY 22-23 Student Barcodes.csv") as file:
        csv_reader = csv.reader(file)
        #print("started")
        for row in csv_reader:
            #print("in row")
            for val in row:
                #print("in val")
                if code in val:
                    return(val)


if __name__ == "__main__":
    print("-------------------------------\n|     Library Appender        |\n-------------------------------\n")
    print("To enter a student's name manually, enter their credentials with \"LastName, FirstName\"")
    print("i.e.\"Domingo, Dylan\"\n")
    print("Enter \"!exit\" to exit the program\n")
    while (True):
        id = input()
        name = readBarcode(id)

        e = datetime.datetime.now()

        if type(id) == None:
            print("Not found, please try again.")

        if id == "!exit":
            break

        f = open("Cheesebread.txt", "a")
        f.write(name)
        f.write("\t%s/%s/%s" % (e.month, e.day, e.year))
        f.write("\t%s:%s:%s" % (e.hour, e.minute, e.second))
        f.write("\n")
        f.close()

        print("Student inputted!\n")
    quit()
        