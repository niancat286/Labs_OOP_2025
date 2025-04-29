class MyClass:

    def __init__(self, value):
        self.value = value

    def print(self):
        print(self.value)

if __name__ == '__main__':
    ob = MyClass(5)

    print("Атрибути класу MyClass:")
    print(dir(MyClass))

    print("\nАтрибути екземпляра obj:")
    print(dir(ob))

    print("\nЧи є метод 'print' у MyClass?")
    print(hasattr(MyClass, 'print'))

    print("\nВикликаємо метод 'print':")
    if hasattr(ob, 'print'):
        method = getattr(ob, 'print')
        method()

    print("\nВидаляємо метод 'print'")
    if hasattr(MyClass, 'print'):
        delattr(MyClass, 'print')

    print("\nЧи є метод 'print' після видалення?")
    print(hasattr(MyClass, 'print'))


    print("\nДодаємо метод '__str__' до класу")

    def custom_str(self):
        return str(self.value)

    setattr(MyClass, '__str__', custom_str)
    print(ob)