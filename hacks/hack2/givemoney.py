import numpy as np

with open("pokeyellow.sav", "rb") as savFile:
    data = bytearray(savFile.read())

moneyAddr = 0x25F3
moneySize = 0x03

for b in range(moneySize):
    data[moneyAddr + b] = 0x99

checksum = np.uint8(255)
checksumInputStart = 0x2598
checksumInputEnd = 0x3523
checksumAddr = 0x3523
for b in range(checksumInputStart, checksumInputEnd):
    checksum -= np.uint8(data[b])
data[checksumAddr] = checksum


with open("pokeyellow.sav.mod", "wb") as savFile:
    savFile.write(data)
