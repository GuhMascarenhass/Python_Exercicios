def BinaryToDecimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return (decimal)


bin_data = '011000010111001100100000011100110111010101100001011100110010000001100010011011110110110101100010011000010111001100100000011100000110010101110010011101000110010101101110011000110110010101101101001000000110000100100000011011101111001101110011'

print("The binary value is:", bin_data)

str_data = ' '

for i in range(0, len(bin_data), 7):
    temp_data = int(bin_data[i:i + 7])

    decimal_data = BinaryToDecimal(temp_data)

    str_data = str_data + chr(decimal_data)

print("The Binary value after string conversion is:",
      str_data)