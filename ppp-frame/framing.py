def stuffing(bin_str):
    if len(bin_str) % 8 != 0:
        stuffed_bits = 8 - (len(bin_str) % 8)
        bin_str += '0' * stuffed_bits
    return bin_str


def hex_to_bin_str(hex_str):
    dec_num = int(hex_str, 16)
    hex_str_len = len(hex(dec_num)) - 2
    bin_str = bin(dec_num)[2:].zfill(hex_str_len * 4)
    return bin_str


def format_bin_str(bin_str):
    bin_str = stuffing(bin_str)
    xor_key = '00100000'
    for i in range(0, len(bin_str), 8):
        octet = bin_str[i:i + 8]
        if octet == '01111110' or octet == '01111101':
            xor_str = int(octet, 2) ^ int(xor_key, 2)
            stuffing_key = bin(xor_str)[2:].zfill(8)
            bin_str = bin_str[:i] + '01111101' + stuffing_key + bin_str[i + 8:]
            i += 8
    return '01111110' + bin_str + '01111110'


def ppp_framing(msg):
    formatted_bin_str = format_bin_str(hex_to_bin_str(msg))
    result = hex(int(formatted_bin_str, 2))[2:]
    return result


# Test
message = '417d427e507046'
output = ppp_framing(message)
# Will print: 7e417d5d427d5e5070467e
print(output)
