def decode(inp):
    if len(inp) == 0 or (len(inp) == 1 and inp[0] == '0'):
        return 0
    return decodeProcess(inp, len(inp))

def decodeProcess(inp, inp_size):
    if inp_size == 0 or inp_size == 1:
        return 1
    count = 0
    if inp[inp_size - 1] > '0':
        count = decodeProcess(inp, inp_size-1)
    if (inp[inp_size - 2] == '1' or (inp[inp_size - 2] == '2' and inp[inp_size - 1] < '7')):
        count += decodeProcess(inp, inp_size - 2)
    return count

seq = '1313121208'
a = decode(seq)
print(a)