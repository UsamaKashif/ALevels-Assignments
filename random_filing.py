import os

RECORDSIZE = 20
DATAFILE = 'members.dat'
SECONDFILE = "newFile.dat"

class SportClub:
    def __init__(self):
        self.name = ''
        self.memberId = ''
    
    def preparedata(self, args):
        ''' generate comma separated string of data fields'''
        return ','.join(arg.ljust(10) for arg in args)

    def addrecord(self, data, fileName):
        ''' add record to file '''
        try:
            file = open(fileName,'r+b')
            print("opening in r+b mode")
        except IOError:
            print("opening in wb mode ")
            file = open(fileName,'wb')            

        try:
            print("  adding {}".format(data))
            data = self.preparedata(data)
            name = data.split(",")[0]
            pointer = self.getHash(name)
            
            file.seek(pointer)
            file.write(data.encode())            
            file.close()
        except Exception as e:
            raise e

    def getHash(self, name):
        ''' generate hash to store record at random pointer in file'''
        return sum([ord(n) for n in name.lower()]) * RECORDSIZE + 1


def add_new_record():
    ''' add new record '''
    toadd = "y"
    while toadd != "n":
        val = input("Press Enter to add new record. Press 'n' to exit ")
        if val == "n":
            return
        else:
            name = input("Enter Name: ")
            memberid = input("Enter MemberID ")
            record = SportClub()
            record.addrecord([name, memberid], DATAFILE)

def findrecord(name):
    ''' find record in data file '''
    record = SportClub()
    pointer = record.getHash(name.ljust(10))

    file = open(DATAFILE, "rb")

    file.seek(pointer)
    data = file.read(RECORDSIZE).decode('ascii')
    
    if data and name in data:        
        print(data)
    else:
        print("Record not found ")
    return

def getallrecords():
    ''' get all records stored in the file '''
    file = open(DATAFILE, "rb")
    ctr = 0
    file.seek(ctr)
    data = file.read(RECORDSIZE).decode('ascii')
    
    while data:
        if "," in data:
            print(data)
        ctr += 1
        file.seek(RECORDSIZE * ctr)
        data = file.read(RECORDSIZE).decode('ascii')


def additionalInfo ():
    try:
        file = open(DATAFILE, "rb")
    except IOError:
        print("File not found")
    ctr = 0
    file.seek(ctr)
    data = file.read(RECORDSIZE).decode('ascii')
    
    while data:
        if "," in data:
            try:
                newFile = open(SECONDFILE, "rb+")
            except IOError:
                newFile = open(SECONDFILE, "wb")
            member = SportClub()
            name,memberId = data.split(",")
            membershipStartDate = input(f'Enter membership start date for {data[12:]}: ')
            telephoneNum = input(f'Enter Telephone number: ')
            member.addrecord([name,memberId,telephoneNum,membershipStartDate],SECONDFILE)
            newFile.close()
        ctr += 1
        file.seek(RECORDSIZE * ctr)
        data = file.read(RECORDSIZE).decode('ascii')

if __name__ == "__main__":
    
    # add records
    add_new_record()

    # find record by name
    choice = input("Find record by name y/n: ").lower()

    while choice[0] != "n":
        name = input("enter name to find: ")
        findrecord(name)
        choice = input("Find record by name y/n: ").lower()

    print("")
    print("Printing all records from the file..")
    getallrecords()
    print("")
    additionalInfo()
    

