'''Домашнее задание по уроку "Пространство имен"

Создайте новый проект в PyCharm
Запустите созданный проект
Ваша задача:
Создайте новую функцию def test_function
Создайте другую функцию внутри функции inner_function,
функция должна печатать значение "Я в области видимости функции test_function"
Вызовите функцию inner_function внутри функции test_function
Попробуйте вызывать inner_function вне функции test_function и посмотрите на результат выполнения программы
Полученный код напишите в ответ к домашнему заданию'''

def test_function():
    # определяем внутреннюю функцию:
    def inner_function():
        print('Я в области видимости функции test_function')

    # вызываем внутреннюю функцию:
    inner_function()

def main():
    test_function()
    #inner_function()
    # Реакция -> NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?

if __name__ == '__main__':
    main()
