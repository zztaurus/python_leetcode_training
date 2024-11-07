

def isLongPressedName(name, typed):

    i, j = 0, 0
    for i in range(len(typed)):
        if typed[i] == name[j]:
            continue
        else:
            j += 1
            if j < len(name) and typed[i] != name[j]:
                return False
    return True


def isLongPressedName2(name, typed):
    i, j = 0, 0
    while i < len(typed):
        if j < len(name) and name[j] == typed[i]:
            i += 1
            j += 1
        elif i > 0 and typed[i] == typed[i-1]:
            i += 1
        else:
            return False
    return True


if __name__ == '__main__':
    print(isLongPressedName('saeed', 'ssaaedd'))

