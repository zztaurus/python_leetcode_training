
# 传值还是传地址

def main():
    a = 123
    b = 123
    c = a
    d = b
    print(id(a))
    print(id(b))
    print(id(c))
    print(id(d))

    a = 456
    f = a
    print(id(a))
    print(id(f))

    x = [1, 2, 3]
    y = x
    print(id(x))
    x.append(4)
    print(y)
    print(id(y))


if __name__ == '__main__':
    main()