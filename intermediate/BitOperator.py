__author__ = 'galo javier'

a = 0b10111011
mask = 0b100
print( bin (a | mask ))
print(a)
print(mask)
print(0b10111011)


b = 0b110 # 6
mask1 = 0b1 # 1
desired =  b | mask1 # 0b111, or 7
print(b)
print (desired)
print(bin(desired))


aa = 0b11101110
mask2 = 0b11110001
print("-------------XOR")
print (bin(aa ^ mask2))