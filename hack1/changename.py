import numpy as np

with open("pokeyellow.sav", "rb") as savFile:
    data = bytearray(savFile.read())

nameAddr = 0x2598
nameSize = 0xB

data[nameAddr + 1] = 0x81
data[nameAddr + 2] = 0x82
data[nameAddr + 3] = 0x83


checksum = np.uint8(255)
checksumInputStart = 0x2598
checksumInputEnd = 0x3523
checksumAddr = 0x3523
for b in range(checksumInputStart, checksumInputEnd):
    checksum -= np.uint8(data[b])
data[checksumAddr] = checksum


with open("pokeyellow.sav.mod", "wb") as savFile:
    savFile.write(data)
