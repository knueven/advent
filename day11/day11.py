import re
import sys

rule2Letters = ["i", "o", "l"]

def increment(pw):
    charlist = list(pw)
    for idx, char in reversed(list(enumerate(pw))):
        # unicode of the character
        utf = ord(char)
        #122 is 'z'
        if utf != 122:
            charlist[idx] = chr(utf + 1)
            break
        else:
            #print("was z")
            while(True):
                charlist[idx] = "a"
                if charlist[idx - 1] != "z":
                    break
                idx = idx - 1
    return "".join(charlist)

def check_password(pw):
    # check rule 2
    if any(letter in pw for letter in rule2Letters):
        return False

    # rule 3
    if len(re.findall(r'(.)\1+', pw)) < 2:
            return False

    # rule 1
    for i in range(0, len(pw)-2):
            if ord(pw[i]) == ord(pw[i+1]) - 1 and ord(pw[i+1]) == ord(pw[i+2]) - 1:
                break
    else:
        return False

    return True

def find_next(pw):
    while(True):
        pw = increment(pw)
        if check_password(pw):
            print(pw)
            break


#gives next password in sequence
if __name__ == "__main__":
    find_next(sys.argv[1])
