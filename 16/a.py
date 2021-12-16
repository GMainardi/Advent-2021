def decode_literal(bin):
    sub_pac_len = 5
    ans = ''
    contin = True
    while contin:
        if bin[0] == '0':
            contin = False
        ans += bin[1:sub_pac_len]
        bin = bin[sub_pac_len:]
    return int(ans, 2), bin

def pack_info(bin):
    ver = int(bin[:3],2)
    pack_id = int(bin[3:6], 2)
    bin = bin[6:]
    return ver, pack_id, bin

def get_sub_pack(bin):
    sub_pac_len = int(bin[1:16],2)
    bin = bin[16:]
    # get de sub_pac
    sub_pac = bin[:sub_pac_len]
    bin = bin[sub_pac_len:]
    return sub_pac, bin

def get_numb_sub_pack(bin):
    numb = int(bin[1:12], 2)
    bin = bin[12:]
    return numb, bin

def decode_operator(bin):
    if bin[0] == '0':
        sub_pac, bin = get_sub_pack(bin)
        process(sub_pac)
    else:
        numb, bin = get_numb_sub_pack(bin)
        bin = process(bin, numb)
    return bin

def process(bin, numb = float('inf')):
    global sum
    while len(bin) > 10 and numb > 0:
        ver, pack_id, bin = pack_info(bin)
        sum += ver
        if pack_id == 4:
            #print('literal', bin)
            value, bin = decode_literal(bin)
            #print('literal value', value)
        else:
            #print('operation', bin)
            bin = decode_operator(bin)
        numb -=1
    return bin

input = [line.strip() for line in open('input.txt', 'r')][0]
bin = bin(int(input, 16))[2:].zfill(4*len(input))
sum = 0
process(bin)
print(sum)