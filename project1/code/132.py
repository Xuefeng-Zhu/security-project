def wha(in_str):
    bin_array = bytearray(in_str)

    hexdata1 = int('CC', 16)
    hexdata2 = int('33', 16)
    hexdata3 = int('AA', 16)
    hexdata4 = int('55', 16)

    mask = int('3FFFFFFF', 16)
    out_hash = 0

    for byte in bin_array:
        intermediate_value = ((byte ^ hexdata1) << 24) | (
            (byte ^ hexdata2) << 16) | ((byte ^ hexdata3) << 8) | (byte ^ hexdata4)
        out_hash = (out_hash & mask) + (intermediate_value & mask)
    return hex(out_hash)

if __name__ == '__main__':
    assert wha("Hello world!") == "0x50b027cf"
    assert wha("I am Groot.") == "0x57293cbb"
