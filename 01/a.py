with open('./01/input.txt') as f:
    data = f.readlines()

NUMBERS = [str(i) for i in range(10)]

def get_calibration_val(line):
    val = ""
    for sign in line:
        if sign in NUMBERS:
            val += sign
            break
    
    for sign in line[::-1]:
        if sign in NUMBERS:
            val += sign
            break
    
    return int(val)

def main():
    ret = 0
    for line in data:
        ret += get_calibration_val(line)

    print(ret)

main()