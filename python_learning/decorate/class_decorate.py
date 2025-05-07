# Python 2.6 开始添加类装饰器
from functools import wraps


# 类装饰
class MyClass(object):
    def __init__(self, var='init_var', *args, **kwargs):
        self._v = var
        super(MyClass, self).__init__(*args, **kwargs)

    def __call__(self, func):
        # 类的函数装饰器
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            func_name = func.__name__ + " was called"
            print(func_name)
            return func(*args, **kwargs)

        return wrapped_function

obj = MyClass()  #类的实例作为装饰器使用，包装目标函数并在调用时打印日志。

@obj
def myfunc1():
    pass

# 其他经常用在类装饰器的python自带装饰器
# classmethod
# staticmethod
# property


if __name__ == '__main__':
    myfunc1()
