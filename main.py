M = [
    ['32', '88', '31', '20'],
    ['43', '5a', '31', '37'],
    ['76', '30', '98', '07'],
    ['8a', '8d', 'a2', '34']
]
K = [
    ['2b', '28', 'ab', '09'],
    ['7e', 'ae', 'f7', 'cf'],
    ['15', 'd2', '15', '4f'],
    ['1b', 'a6', '88', '3c']
]
"""
def Convertir(x):
    list1=['0','1','2','3','4','5','6','7','8','9']
    list2=['a','b','c','d','e','f']
    pos=10
    r=[]
    c=[]
    if x in list2:
        p=list2.index(x)
        l=pos+p
    else:
        l=int(list1.index(x))
    v=bin(l)
    for char in v:
        r.append(char)
    if len(r)==6:
        for i in range (2,len(r)):
            c.append(r[i])
    elif len(r)==5:
        c.append('0')
        for i in range(2,len(r)):
            c.append(r[i])
    elif len(r)==4:
        c.append('0')
        c.append('0')
        for i in range(2,len(r)):
            c.append(r[i])
    elif len(r)==3:
        c.append('0')
        c.append('0')
        c.append('0')
        for i in range(2,len(r)):
            c.append(r[i])

    return c



print(Convertir('1'))

def AddRoundKey(m1,m2):
    m=len(m1)
    k=len(m2)
    for i in range (0,m):
        for j in range (0,m):
            x=m1[i][j]
            y=m2[i][j]
            for char in x:
                print(char)
                Convertir(char)




 
"""
from Crypto.Cipher import AES

# Choose a key and a message
key = b'Sixteen byte key'
message = b'Attack at dawn'

# Pad the message to a multiple of the block size
padding_length = 16 - (len(message) % 16)
message += b' ' * padding_length

# Initialize the cipher object
cipher = AES.new(key, AES.MODE_ECB)

# Encrypt the message
encrypted_message = cipher.encrypt(message)

# Decrypt the message
decrypted_message = cipher.decrypt(encrypted_message)

# Strip the padding from the decrypted message
decrypted_message = decrypted_message[:-padding_length]

print(f'Original message: {message}')
print(f'Encrypted message: {encrypted_message}')
print(f'Decrypted message: {decrypted_message}')
