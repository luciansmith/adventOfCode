import numpy as np
import binascii

example = False

hexval = "020D74FCE27E600A78020200DC298F1070401C8EF1F21A4D6394F9F48F4C1C00E3003500C74602F0080B1720298C400B7002540095003DC00F601B98806351003D004F66011148039450025C00B2007024717AFB5FBC11A7E73AF60F660094E5793A4E811C0123CECED79104ECED791380069D2522B96A53A81286B18263F75A300526246F60094A6651429ADB3B0068937BCF31A009ADB4C289C9C66526014CB33CB81CB3649B849911803B2EB1327F3CFC60094B01CBB4B80351E66E26B2DD0530070401C82D182080803D1C627C330004320C43789C40192D002F93566A9AFE5967372B378001F525DDDCF0C010A00D440010E84D10A2D0803D1761045C9EA9D9802FE00ACF1448844E9C30078723101912594FEE9C9A548D57A5B8B04012F6002092845284D3301A8951C8C008973D30046136001B705A79BD400B9ECCFD30E3004E62BD56B004E465D911C8CBB2258B06009D802C00087C628C71C4001088C113E27C6B10064C01E86F042181002131EE26C5D20043E34C798246009E80293F9E530052A4910A7E87240195CC7C6340129A967EF9352CFDF0802059210972C977094281007664E206CD57292201349AA4943554D91C9CCBADB80232C6927DE5E92D7A10463005A4657D4597002BC9AF51A24A54B7B33A73E2CE005CBFB3B4A30052801F69DB4B08F3B6961024AD4B43E6B319AA020020F15E4B46E40282CCDBF8CA56802600084C788CB088401A8911C20ECC436C2401CED0048325CC7A7F8CAA912AC72B7024007F24B1F789C0F9EC8810090D801AB8803D11E34C3B00043E27C6989B2C52A01348E24B53531291C4FF4884C9C2C10401B8C9D2D875A0072E6FB75E92AC205CA0154CE7398FB0053DAC3F43295519C9AE080250E657410600BC9EAD9CA56001BF3CEF07A5194C013E00542462332DA4295680"
if (example):
    # hexval = "D2FE28"
    hexval = "38006F45291200"
    hexval = "9C0141080250320F1802104A08"

#stole this bit from https://www.geeksforgeeks.org/python-ways-to-convert-hex-into-binary/ method 2.
n = int(hexval, 16) 
binval = ''
while n > 0:
    binval = str(n % 2) + binval
    n = n >> 1    

leading_zeros = '0' * (len(hexval)*4 - len(binval))
binval = leading_zeros + binval

print(binval)

def readOneOperation(binval, index):
    if binval[index:].count('0') == len(binval)-index:
        return (None, None, None, len(binval))
    version = int(binval[index:index+3], 2)
    index += 3
    ptype = int(binval[index:index+3], 2)
    index += 3
    if ptype==4:
        litval = binval[index+1:index+5]
        while binval[index]=='1':
            index += 5
            litval += binval[index+1:index+5]
        index += 5
        # print(litval)
        return (version, ptype, int(litval, 2), index)
    else:
        length = binval[index]
        index += 1
        if length=='0':
            sublength = int(binval[index:index+15], 2)
            index += 15
            subbin = binval[index:index+sublength]
            index += sublength
            subindex = 0
            subpackets= []
            while (subindex < len(subbin)-3):
                subpacket = readOneOperation(subbin, subindex)
                subindex = subpacket[3]
                # print("Sub-packets:", subpacket)
                subpackets.append(subpacket)
            return (version, ptype, subpackets, index)
        else:
            assert(length=='1')
            nsubs = int(binval[index:index+11], 2)
            index += 11
            subpackets = []
            for n in range(nsubs):
                subpacket = readOneOperation(binval, index)
                index = subpacket[3]
                # print("Sub-packets:", subpacket)
                subpackets.append(subpacket)
            return (version, ptype, subpackets, index)

def countVersions(packet):
    total = packet[0]
    if packet[1] != 4:
        for subpacket in packet[2]:
            total += countVersions(subpacket)
    return total

def prod(vec):
    ret = 1
    for val in vec:
        ret = ret*val
    return ret

def calculateValue(packet):
    ptype = packet[1]
    if ptype==0:
        vec = []
        for subpacket in packet[2]:
            vec.append(calculateValue(subpacket))
        print("Sum:", vec, sum(vec))
        return sum(vec)
    elif ptype==1:
        vec = []
        for subpacket in packet[2]:
            vec.append(calculateValue(subpacket))
        print("Product:", vec, prod(vec))
        return prod(vec)
    elif ptype==2:
        vec = []
        for subpacket in packet[2]:
            vec.append(calculateValue(subpacket))
        print("Min:", vec, min(vec))
        return min(vec)
    elif ptype==3:
        vec = []
        for subpacket in packet[2]:
            vec.append(calculateValue(subpacket))
        print("Max:", vec, max(vec))
        return max(vec)
    elif ptype==4:
        print("val:", packet[2])
        return packet[2]
    elif ptype==5:
        vec = []
        for subpacket in packet[2]:
            vec.append(calculateValue(subpacket))
        assert(len(vec)==2)
        print("gt:", vec, vec[0]>vec[1])
        if (vec[0] > vec[1]):
            return 1
        return 0
    elif ptype==6:
        vec = []
        for subpacket in packet[2]:
            vec.append(calculateValue(subpacket))
        assert(len(vec)==2)
        print("lt:", vec, vec[0]<vec[1])
        if (vec[0] < vec[1]):
            return 1
        return 0
    elif ptype==7:
        vec = []
        for subpacket in packet[2]:
            vec.append(calculateValue(subpacket))
        assert(len(vec)==2)
        print("eq:", vec, vec[0]==vec[1])
        if (vec[0] == vec[1]):
            return 1
        return 0
    else:
        raise ValueError("Unknown packet type", ptype)


packet = readOneOperation(binval, 0)
print(packet)
print(countVersions(packet))
print(calculateValue(packet))

