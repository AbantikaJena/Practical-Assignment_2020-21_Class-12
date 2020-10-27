# Que 19

# Write a program to create a binary file ‘result.dat’ with roll number, name and marks of any 5 students then input a roll number and update the marks. Display all the records after updating records.

# In a binary file store, update and display data

def Data():
    file = input("Enter file name : ")

    def MainMenu():
        print("-" * 20)
        print("1. Write Data...")
        print("2. Display Data...")
        print("3. Update Data... ")
        print("4. Quit... ")
        print("-" * 20)


    import pickle

    def Write():
        f = open(file,"wb")
        n = int(input("Enter no of records : "))
        record = []
        for i in range(n):
            rno = int(input("Enter Roll no. : "))
            name = input("Name :")
            marks = float(input("Marks: "))
            data = [rno, name, marks]
            record.append(data)
        pickle.dump(record,f)
        print("Recorded Added...")
        f.close()

    def Display():
        print("Result...")
        print("[RollNo., Name, Marks]")
        f = open(file, "rb")
        try:
            while True:
                s = pickle.load(f)
                for i in s:
                    print(i)
        except Exception:
            f.close()

    def Update():
        f = open(file, "rb+")
        r = int(input("Enter roll no whose details to be updated : "))
        f.seek(0)
        try:
            while True:
                rpos = f.tell()
                s= pickle.load(f)
                for i in s:
                    if i[0] == r:
                        i[2] = float(input("Update Marks : "))
                        f.seek(rpos)
                        pickle.dump(s, f)
        except Exception:
            f.close()

    while True:
        MainMenu()
        ch = int(input("Enter your choice :  "))
        if ch == 1:
            Write()
        elif ch == 2:
            Display()
        elif ch == 3:
            Update()
        elif ch == 4:
            print("Thank You!\nTask Done!")
            break
        else:
            print("No more choice...")
Data()