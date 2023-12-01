with open('./01/input.txt') as f:
    data = f.readlines()

NUMBERS_DICT = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

def replace_strings(line):
    length = len(line) # \n is included!

    line_front = line
    for step in range(length):
        for word in NUMBERS_DICT.keys():
            word_length = len(word)
            if step + word_length <= length and line_front[step:step + word_length] == word:
                line_front = line_front[0:step] + NUMBERS_DICT[word] + line_front[step + word_length:]
                break
    
    line_back = line[::-1]
    for step in range(length):
        for word in NUMBERS_DICT.keys():
            word_length = len(word)
            if step + word_length <= length and line_back[step:step + word_length] == word[::-1]:
                line_back = line_back[0:step] + NUMBERS_DICT[word] + line_back[step + word_length:]
                break

    return line_front, line_back
    
def get_calibration_val(line):
    line_front, line_back = replace_strings(line)
    val = ""
    for sign in line_front:
        if sign in NUMBERS_DICT.values():
            val += sign
            break
    
    for sign in line_back:
        if sign in NUMBERS_DICT.values():
            val += sign
            break

    return int(val)

def main():
    ret = 0
    for line in data:
        ret += get_calibration_val(line)

    print(ret)

main()