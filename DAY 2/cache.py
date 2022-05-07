def printCache(cache):
    print('Cache: [', end='')
    for i in range(len(cache)-1):
        if cache[i] == 'X':
            print('X', end=', ')
        else:
            print(cache[i], end=', ')
    print(cache[len(cache)-1], end = ']\n')

def cache_emulator():
    # RAM
    print('Give RAM size:')
    ramSize =  input()
    if ramSize.isnumeric():
        ramSize = int(ramSize)
        if ramSize < 1:
            raise ValueError("RAM Size must be more than 1.")
    else:
        raise ValueError("RAM Size must be a positive integer.")
    
    # Cache
    print(f'Give cache size(<RAM size = {ramSize})')
    cacheSize =  input()
    if cacheSize.isnumeric():
        cacheSize = int(cacheSize)
        if cacheSize < 1 or cacheSize > ramSize:
            raise ValueError("Cache Size must be more than 1 and less than RAM size.")
    else:
        raise ValueError("Cache Size must be a positive integer.")
    
    # Number of Addresses
    print('Give number of addresses:')
    numOfAddresses = input()
    if numOfAddresses.isnumeric():
        numOfAddresses = int(numOfAddresses)
        if numOfAddresses < 1:
            raise ValueError("Number of Addresses must be more than 1.")
    else:
        raise ValueError("Number of Addresses must be a positive integer")
        
    # Addresses
    print(f'Give addresses (0-{ramSize-1})')
    listOfAddresses = [None for i in range(numOfAddresses)]
    for i in range(numOfAddresses):
        temp = input()
        if temp.isnumeric():
            temp = int(temp)
            if temp < 0 or temp >(ramSize - 1):
                raise ValueError(f"Adresses must be more than 0 and less than RAM size - 1 = {ramSize-1}.")
        else:
            raise ValueError("Adresses must be positive integers or 0")
        listOfAddresses[i] = temp
            
    cache = ['X' for _ in range(cacheSize)]
    
    for i in range(len(listOfAddresses)):
        index = listOfAddresses[i] % cacheSize
        if cache[index] == listOfAddresses[i]:
            print('hit!')
        else:
            print('miss!')
            cache[index] = listOfAddresses[i]
        printCache(cache)


cache_emulator()