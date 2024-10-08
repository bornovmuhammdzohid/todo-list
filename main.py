todo = []
number = 0
while True:
    add_todo = input('Bugungi ishni kiriting: ')
    todo.append(add_todo)
    question = input('Yana malumot kirgazasizmi (h) or (y): ')
    if question == 'y':
        break
print('Bugungi ishlar')
for todo in todo:
    number +=1
    print(f'{number}.{todo}')