def divide(first, second):
    if second != 0:
        return first / second
    else:
        return 'Ошибка'

def main():
    v1 = 3
    v2 = 0
    print(f'{v1} / {v2} =', divide(v1, v2), f'\n{v2} / {v1} =', divide(v2, v1))

if __name__ == '__main__':
    main()