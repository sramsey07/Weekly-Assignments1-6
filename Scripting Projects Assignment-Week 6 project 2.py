code = input("Enter the coded text: ")
distance = int(input("Enter the distance value: "))
plainText = ''
for ch in code:
    ordValue = ord(ch)
    cipherValue = ordValue - distance
    if cipherValue < ord('a'):
        cipherValue = ord('z') - (distance - \
                                  (ordValue - ord('a')) - 1)
    plainText +=  chr(cipherValue)
print (plainText)
