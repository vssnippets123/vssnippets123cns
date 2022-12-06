import enchant
d = enchant.Dict("en_US")
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
            'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
transAlphabet = {}
f = open("input.txt", 'r')
text = f.read()
f = open("output.txt", 'w')


def createDict(shift):
    for i in range(0, 26):
        letter = alphabet[i]
        transAlphabet[letter] = alphabet[(i-shift+26) % 26]


def decodeText(text, key):
    global Key, CipherText
    total = 0
    cipherText = ''
    for letter in text:
        if letter in transAlphabet:
            cipherText = cipherText+transAlphabet[letter]
        else:
            cipherText = cipherText+letter
    t = cipherText.split()
    for word in t:
        if d.check(word) == True:
            total = total+1
    if total == len(t):
        Key = str(key)
        CipherText = str(cipherText)
    f.writelines(["Key: ", str(key), "\n"])
    f.writelines(["Cipher Text: ", cipherText, "\n"])


f.writelines(["----------Text Combinations----------\n"])
for i in range(0, 26):
    createDict(i)
    decodeText(text, i)

f.writelines(["----------Decrypted Text----------\n"])
f.writelines(["Key: ", str(Key), "\n"])
f.writelines(["Cipher Text: ", CipherText])
