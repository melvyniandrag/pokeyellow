import numpy as np

with open("pokeyellow.sav", "rb") as savFile:
    data = bytearray(savFile.read())


pikachuOffset = 0x2F34
pikachuCurrentHPOffset = 0x01 # 2 bytes
pikachuMove1Offset = 0x08
pikachuMove2Offset = 0x09
pikachuMove3Offset = 0x0A
pikachuMove4Offset = 0x0B
pikachuMove1PPOffset = 0x1D
pikachuMove2PPOffset = 0x1E
pikachuMove3PPOffset = 0x1F
pikachuMove4PPOffset = 0x20
pikachuLevelOffset = 0x21
pikachuMaxHPOffset = 0x22 # 2 bytes
pikachuAttackOffset = 0x24 # 2 bytes
pikachuDefenseOffset = 0x26 # 2 bytes
pikachuSpeedOffset = 0x28 # 2 bytes
pikachuSpecialOffset = 0x2A # 2 bytes

data[pikachuOffset + pikachuCurrentHPOffset : pikachuOffset + pikachuCurrentHPOffset + 2] = (0x00C8).to_bytes(2, "big")
data[pikachuOffset + pikachuMove1Offset] = 0x57
data[pikachuOffset + pikachuMove2Offset] = 0x8E
data[pikachuOffset + pikachuMove3Offset] = 0x38
data[pikachuOffset + pikachuMove4Offset] = 0x3A
data[pikachuOffset + pikachuMove1PPOffset] = 0x14
data[pikachuOffset + pikachuMove2PPOffset] = 0x14
data[pikachuOffset + pikachuMove3PPOffset] = 0x14
data[pikachuOffset + pikachuMove4PPOffset] = 0x14
data[pikachuOffset + pikachuLevelOffset] = 0x63
data[pikachuOffset + pikachuMaxHPOffset : pikachuOffset + pikachuMaxHPOffset + 2] = (0x00C8).to_bytes(2, "big")
data[pikachuOffset + pikachuAttackOffset : pikachuOffset + pikachuAttackOffset + 2] = (0x00C8).to_bytes(2, "big")
data[pikachuOffset + pikachuDefenseOffset : pikachuOffset + pikachuDefenseOffset + 2] = (0x00C8).to_bytes(2, "big")
data[pikachuOffset + pikachuSpeedOffset : pikachuOffset + pikachuSpeedOffset + 2 ] = (0x00C8).to_bytes(2, "big")
data[pikachuOffset + pikachuSpecialOffset : pikachuOffset + pikachuSpecialOffset + 2] = (0x00C8).to_bytes(2, "big")

checksum = np.uint8(255)
checksumInputStart = 0x2598
checksumInputEnd = 0x3523
checksumAddr = 0x3523
for b in range(checksumInputStart, checksumInputEnd):
    checksum -= np.uint8(data[b])
data[checksumAddr] = checksum


with open("pokeyellow.sav.mod", "wb") as savFile:
    savFile.write(data)
