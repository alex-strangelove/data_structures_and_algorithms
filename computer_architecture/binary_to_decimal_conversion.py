
def to_decimal(bin_num, trace):

    decimal = 0
    count = 0
    binary_num = bin_num[::-1]

    if trace:
        for y in binary_num:
            buffer = 2 ** count
            print(buffer, y)
            if y == '1':
                decimal += buffer
            count += 1
    else:
        for k in binary_num:
            if k == '1':
                buffer = 2 ** count
                decimal += buffer
            count += 1

    return decimal


def main():
    # print(f"52345 = {bin(52345)} in binary.\n\n")
    # print(f"1100110001111001 = {int(0b1100110001111001)} in decimal.")

    bin_num = '1111011110011'
    trace = True

    print(to_decimal(bin_num, trace))

if __name__ == '__main__':
    main()