
# 装饰器在模块导入的时候自动运行

def decorate(func):
    print("running in func")
    def inner(*args, **kwargs):
        return func(*args, **kwargs)
    return inner

@decorate
def func2():
    pass

def main():
    func2()

if __name__ == '__main__':
    main()