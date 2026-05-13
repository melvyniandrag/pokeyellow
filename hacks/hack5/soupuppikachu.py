import numpy as np

with open("../../pokeyellow.sav", "rb") as savFile:
    data = bytearray(savFile.read())

#data[0x2f2d] = 0x3D
#data[0x2f34] = 0x3D

def modPokemon(savedata, offset, w_hp, b_move1, b_move2, b_move3, b_move4,
               b_move1pp, b_move2pp, b_move3pp, b_move4pp,
               b_level, tw_exp, w_maxHP, w_attack, w_defense, w_speed, w_special):
    data = savedata.copy()
    currentHPOffset = 0x01 # 2 bytes
    move1Offset = 0x08
    move2Offset = 0x09
    move3Offset = 0x0A
    move4Offset = 0x0B
    expPointOffset = 0x0E
    move1PPOffset = 0x1D
    move2PPOffset = 0x1E
    move3PPOffset = 0x1F
    move4PPOffset = 0x20
    levelOffset = 0x21
    maxHPOffset = 0x22 # 2 bytes
    attackOffset = 0x24 # 2 bytes
    defenseOffset = 0x26 # 2 bytes
    speedOffset = 0x28 # 2 bytes
    specialOffset = 0x2A # 2 bytes
    
    data[offset + currentHPOffset : offset + currentHPOffset + 2] = w_hp 
    data[offset + move1Offset] = b_move1 
    data[offset + move2Offset] = b_move2
    data[offset + move3Offset] = b_move3 
    data[offset + move4Offset] = b_move4 
    data[offset + move1PPOffset] = b_move1pp 
    data[offset + move2PPOffset] = b_move2pp 
    data[offset + move3PPOffset] = b_move3pp 
    data[offset + move4PPOffset] = b_move4pp 
    data[offset + levelOffset] = b_level 
    data[offset + expPointOffset : offset + expPointOffset + 3] = tw_exp 
    data[offset + maxHPOffset   : offset + maxHPOffset + 2] = w_maxHP 
    data[offset + attackOffset  : offset + attackOffset + 2] = w_attack 
    data[offset + defenseOffset : offset + defenseOffset + 2] = w_defense
    data[offset + speedOffset   : offset + speedOffset + 2 ] = w_speed
    data[offset + specialOffset : offset + specialOffset + 2] = w_special 
    return data


data = modPokemon( savedata = data, offset = 0x2F34, w_hp=(200).to_bytes(2, "big"),
                  b_move1=0x07, b_move2=0x01, b_move3=0x02, b_move4=0x03,
                  b_move1pp=0x14, b_move2pp=0x14, b_move3pp=0x14, b_move4pp=0x14, b_level=0x41,
                  w_maxHP=(200).to_bytes(2, "big"), w_attack=(200).to_bytes(2, "big"),
                  w_defense=(200).to_bytes(2, "big"), w_special=(200).to_bytes(2, "big"),
                  w_speed=(200).to_bytes(2, "big"), tw_exp=(278000).to_bytes(3, "big"))

checksum = np.uint8(255)
checksumInputStart = 0x2598
checksumInputEnd = 0x3523
checksumAddr = 0x3523
for b in range(checksumInputStart, checksumInputEnd):
    checksum -= np.uint8(data[b])
data[checksumAddr] = checksum


with open("pokeyellow.sav", "wb") as savFile:
    savFile.write(data)
