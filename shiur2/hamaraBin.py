x = int(input("Enter a number: "))
y = int(input("Enter bit length: "))

def memir_le_binar(num, bits):
    if num >= pow(2,bits):
        return "Error: number too large for given bit length"

    binary = ""
    for i in range(bits - 1, -1, -1):
        power = pow(2,i)
        if num >= power:
            binary += "1"
            num -= power
        else:
            binary += "0"
    return binary

binary_numog = memir_le_binar(x, y)
print(binary_numog)
binary_numtemp = binary_numog.replace('1', '5').replace('0', '1').replace('5', '0')
print(binary_numtemp)

def add_one(binary_str):
    binary_list = list(binary_str)
    carry = 1
    for i in range(len(binary_list) - 1, -1, -1):
        if binary_list[i] == '1' and carry == 1:
            binary_list[i] = '0'
            carry = 1
        elif binary_list[i] == '0' and carry == 1:
            binary_list[i] = '1'
            carry = 0
        else:
            break
    return ''.join(binary_list)

binary_result = add_one(binary_numtemp)
print("After adding 1:", binary_result)

