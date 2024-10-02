royhat = []
def foo() :
    print('To Do List')
    add = input('To Do rejalaringizni kirting: ')
    royhat.append(add)
    print(royhat)
    qaytarish = input("Yana nimadir kiritishni hohlaysizmi? ")
    if qaytarish == 'ha':
        return foo()
    elif qaytarish == 'yoq':
        print(f'Siz kiritgan ishalar: {royhat}')
    else:
        print('Sizni tushunmadim!')
foo()