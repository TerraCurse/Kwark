import sys
import string
def interprete(cont):
    bits = [0, 0, 0, 0]
    char_table = string.digits + string.ascii_uppercase + string.ascii_lowercase + string.punctuation
    max_bit_val = len(char_table)
    active_bit = 1
    for key in cont:
        if key == "i":
            if (bits[active_bit-1] + 1) <= max_bit_val:
                    bits[active_bit-1] += 1
            else:
                bits[active_bit] = 0
        elif key == "I":
            if (bits[active_bit-1] + 2) <= max_bit_val:
                bits[active_bit-1] += 2
            else:
                bits[active_bit] = 0
        elif key == "d":
            if (bits[active_bit-1] - 1) > 0:
                bits[active_bit-1] -= 1
            else:
                bits[active_bit] = max_bit_val
        elif key == "D":
            if (bits[active_bit-1] - 2) > 0:
                bits[active_bit-1] -= 2
            else:
                bits[active_bit] = max_bit_val
        elif key == "n":
            if (active_bit + 1) != 5:
                active_bit += 1
            else:
                active_bit = 1
        elif key == "p":
            if (active_bit - 1) != -1:
                active_bit = 4
        elif key == "o":
                print(char_table[bits[active_bit-1]],end="")

if (sys.argv[1]) != None:
    file_cont = open(sys.argv[1], "r").read().replace("\n", "")
    interprete(file_cont)
    k = input("\nPress enter to close this window or stop the process.")
              