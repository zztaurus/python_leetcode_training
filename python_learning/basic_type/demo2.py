

def main():

    a = [1, 2, 3]
    b = a
    a = [4, 5, 6]
    print(a)
    print(b)
    print(id(a))
    print(id(b))

    a = [1, 2, 3]
    b = a
    a[0], a[1], a[2] = 4, 5, 6
    print(a)
    print(b)
    print(id(a))
    print(id(b))

    x = [1, 2, "asdf"]
    print(x)




if __name__ == '__main__':
    main()