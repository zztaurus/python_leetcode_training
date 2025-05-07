# version 4
def line_conf(a, b):
    def line(x):
        return a*x + b
    return line

def main():
    print(line_conf(1, 2))
    print(line_conf(1, 2))


if __name__ == '__main__':
    main()

