
def function(n, k, m):
    num2segments = {0: 6,
                1: 2,
                2: 5,
                3: 5,
                4: 4,
                5: 5,
                6: 6,
                7: 3,
                8: 7,
                9: 6}
    
    num2segments.pop(m) #deletes the undesired number
    
    #finds the segments used by n
    digitsOfn = [int(digit) for digit in str(n)]    
    numOfSegmentsAvailable = 0
    for digit in digitsOfn:
        numOfSegmentsAvailable += num2segments[digit]

    leastSegmentsNeeded = 2*k     #number 1 needs the least num of segments(2) to be displayed

    tempList = []   #contains the digits of our new number
    for i in range(k):
        for num in range(9,-1,-1):
            if num == m:    #skips undesired number
                continue
            if (numOfSegmentsAvailable - num2segments[num]) >= (k-i-1)*2:   #checks if our choice leaves enough segments for the digits left
                tempList.append(num)
                numOfSegmentsAvailable -= num2segments[num]
                break
    #the following formates the answer
    tempList.reverse()
    ans = 0
    for index, digit in enumerate(tempList):
         ans += digit*(10**index)
    print(ans)
    
function(123,3,7)