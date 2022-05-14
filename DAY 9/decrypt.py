def isPrime(num):
    if num == 0:
        return False
    for n in range(2, int(num**0.5) + 1):
        if num % n == 0:
            return False
    return True

def nextPrime(prime):
    prime += 1
    while isPrime(prime) == False:
        prime += 1
    return prime

def decrypt(message):
    mes_splitted = message.split(',')
    print(mes_splitted)
    
    prime = 1
    ans = []
    for num in mes_splitted:
        prime = nextPrime(prime)
        ans.append(chr(int(int(num)/prime)))
        
    decrypted_mes = ''
    for i in ans:
        decrypted_mes = decrypted_mes+i 
    
    print(decrypted_mes)


mes = '168, 312, 505, 665, 1177, 1313, 2057, 1805, 2415, 3335, 2945, 2479, 4551, 4773, 5264, 5353, 6726, 5917, 7772, 7455, 8103, 8690'
decrypt(mes)
print(isPrime(0))
for i in range(10):
    print(i, nextPrime(i))