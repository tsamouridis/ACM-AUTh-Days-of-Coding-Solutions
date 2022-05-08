import csv

# returns a list with the data from the csv file provided as input. It ignores the headers of the csv
def takeInfo(file):
    infoFile = open(file)
    csvreader = csv.reader(infoFile)
    next(csvreader, None)
    
    info = []
    for row in csvreader:
        info.append(row)
    infoFile.close()
    return info

# Returns True if the email provided is fake
def emailIsFake(email):
    verifiedEmails = ['gmail.com', 'outlook.com', 'hotmail.com', 'yahoo.com', 'icloud.com']
    if email == '':
        return False
    else:
        for index, element in enumerate(email):
            if element == '@':
                if email[(index+1):len(email)] in verifiedEmails:
                    return False
        return True
           
     
# Returns True if the phone provided is fake      
def phoneIsFake(phoneNumber, region, phoneCodes):
    for row in phoneCodes:
        if row[0] == region:
            VerifiedCode = row[1]
    if VerifiedCode == phoneNumber[0:len(VerifiedCode)] and len(phoneNumber) == len(VerifiedCode)+10:
        return False
    else:
        return True
    
# returns a list with the users detected as being fake
def findFakeUsers(usersFile):
    usersInfo = takeInfo(usersFile)
    phoneCodes = takeInfo('Phone numbers.csv')
    fakeUsersList = []
    
    for user in usersInfo:
        userIsFake = False
        name = user[0]
        region = user[1]
        email = user[2]
        phoneNumber = user[3]
        
        if emailIsFake(email) or phoneIsFake(phoneNumber, region, phoneCodes):
            UserIsFake = True
            fakeUsersList.append(name)
    
    return fakeUsersList
            
            
usersFile = 'users.csv'
ans = findFakeUsers(usersFile)
print(ans)
